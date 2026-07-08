from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.db_connection import get_db
from app.schemas.schema_tipo_usuario import TipoUsuarioCreate, TipoUsuarioResponse
from app.controllers.controller_tipo_ussuario import tipo_usuario_controller

router = APIRouter(
    prefix="/tipos-usuario",
    tags=["Tipos de Usuario"]
)

@router.get("/", response_model=List[TipoUsuarioResponse])
def listar_tipos_usuario(db: Session = Depends(get_db)):
    """Obtiene la lista de todos los tipos de usuario."""
    return tipo_usuario_controller.get_all(db)

@router.post("/", response_model=TipoUsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_tipo_usuario(payload: TipoUsuarioCreate, db: Session = Depends(get_db)):
    """Crea un nuevo tipo de usuario (ej: 'Sano' o 'Resistencia a la insulina')."""
    return tipo_usuario_controller.create(db, payload)
