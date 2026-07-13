from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.db_connection import get_db
from app.schemas.schema_registro_comida import (
    RegistroComidaCreate,
    RegistroComidaResponse,
    RegistroComidaDetalladoResponse
)
from app.controllers.controller_registro_comida import RegistroComidaController

# Creamos la instancia del router
router = APIRouter(
    prefix="/registro_comida",
    tags=["registro_comida"],
)

#  Endpoint para crear un nuevo registro de comida
@router.post("/", response_model=RegistroComidaResponse, status_code=status.HTTP_201_CREATED)
def crear_registro_comida(payload: RegistroComidaCreate, db: Session = Depends(get_db)):
    resultado = RegistroComidaController.crear_registro_comida(db, payload)
    return resultado

#  Endpoint para obtener lo que estará en el frontend
@router.get("/", response_model=List[RegistroComidaDetalladoResponse])
def obtener_todos_los_registros(db: Session = Depends(get_db)):
    return RegistroComidaController.get_all_registro_comida(db)

#  Endpoint para obtener un registro único por su ID
@router.get("/{rgtcomida_id}", response_model=RegistroComidaDetalladoResponse)
def obtener_registro_por_id(rgtcomida_id: int, db: Session = Depends(get_db)):
    comida = RegistroComidaController.get_registro_comida_by_id(db, rgtcomida_id)
    if not comida:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El registro de comida solicitado no existe."
        )
    return comida

 #eliminar un registro de comida
@router.delete("/{rgtcomida_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_registro_comida(rgtcomida_id: int, db: Session = Depends(get_db)):
    comida = RegistroComidaController.get_registro_comida_by_id(db, rgtcomida_id)
    if not comida:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El registro de comida no existe."
        )
    # Lógica directa para eliminar en la BD
    db.delete(comida)
    db.commit()
    return None
