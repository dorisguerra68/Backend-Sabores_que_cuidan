from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional  # 👈 Importante: Añadimos Optional para el parámetro de búsqueda

from app.database.db_connection import get_db
from app.schemas.schema_alimento import AlimentoCreate, AlimentoRead, AlimentoUpdate
from app.controllers.controller_alimento import AlimentoController
from app.models.alimento import Alimento

router = APIRouter(
    prefix="/alimento",
    tags=["alimento"],
)


# 🌟 NUEVO: Endpoint unificado para listar todo o filtrar por término si viene en la URL (?buscar=pan)
@router.get("/", response_model=List[AlimentoRead])
def listar_alimentos(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    # 1. Si el frontend envía el parámetro de búsqueda
    if buscar:
        # Filtramos directamente usando ilike (ignora mayúsculas/minúsculas)
        # El formato f"{buscar}%" obliga a que el texto EMPIECE estrictamente por ese término
        alimentos_filtrados = db.query(Alimento).filter(
            Alimento.nombre.ilike(f"{buscar}%")
        ).all()
        return alimentos_filtrados

    # 2. Si el buscador está vacío, por defecto llama a tu controlador y trae la lista completa
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


# Eliminar alimento:
@router.delete("/{id_alimento}", status_code=status.HTTP_200_OK)
def eliminar_alimento(id_alimento: int, db: Session = Depends(get_db)):
    eliminado = AlimentoController.delete_alimento(db, id_alimento)
    if not eliminado:
        raise HTTPException(404, "El alimento no encontrado")
    return {"message": "alimento eliminado"}