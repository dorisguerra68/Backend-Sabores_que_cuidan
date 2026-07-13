from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.db_connection import get_db
from app.schemas.schema_alimento import AlimentoCreate, AlimentoRead, AlimentoUpdate
from app.controllers.controller_alimento import AlimentoController

router = APIRouter(
    prefix="/alimento",
    tags=["alimento"],
)

# Aquí se muestra la lista de alimentos
@router.get("/", response_model=List[AlimentoRead])
def listar_alimentos(db: Session = Depends(get_db)):
    return AlimentoController.get_all_alimentos(db)

# Buscar alimento por id
@router.get("/{id_alimento}", response_model=AlimentoRead)
def obtener_alimento(id_alimento: int, db: Session = Depends(get_db)):
    db_alimento = AlimentoController.get_alimento(db, id_alimento)
    if not db_alimento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alimento no encontrado",
        )
    return db_alimento

# Crear un nuevo alimento
@router.post("/", response_model=AlimentoRead, status_code=status.HTTP_201_CREATED)
def crear_alimento(payload: AlimentoCreate, db: Session = Depends(get_db)):
   
    resultado = AlimentoController.create_alimento(db, payload)

    if resultado == "duplicado":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El alimento ya existe"
        )
    return resultado

# Actualizar un alimento
@router.put("/{id_alimento}", response_model=AlimentoRead)
# CORREGIDO: Cambiado 'init' por 'int'
def actualizar_alimento(id_alimento: int, payload: AlimentoUpdate, db: Session = Depends(get_db)):
    resultado = AlimentoController.update_alimento(db, id_alimento, payload)
    if resultado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alimento no encontrado"
        )
    if resultado == "duplicado":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El alimento ya existe"
        )
    return resultado
