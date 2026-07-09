from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
#Nota en cada router, donde se crea el CRUD
from app.database.db_connection import get_db
from app.schemas.schema_tipo_usuario import TipoUsuarioCreate, TipoUsuarioRead, TipoUsuarioUpdate
from app.controllers.controller_tipo_usuario import TipoUsuarioController

router = APIRouter(
    prefix="/tipos-usuario",
    tags=["Tipos de Usuario"]
)

#vemos los tipos de usuarios
@router.get("/", response_model=List[TipoUsuarioRead])
def listar_tipos_usuario(db: Session = Depends(get_db)):

    return TipoUsuarioController.get_all_tipos_usuario(db)


@router.get("/{id_tpu}", response_model=TipoUsuarioRead)
def obtener_tipo_usuario(id_tpu: int, db: Session = Depends(get_db)):

    db_tipo = TipoUsuarioController.get_tipo_usuario(db, id_tpu)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tipo de usuario no encontrado"
        )
    return db_tipo


@router.post("/", response_model=TipoUsuarioRead, status_code=status.HTTP_201_CREATED)
def crear_tipo_usuario(payload: TipoUsuarioCreate, db: Session = Depends(get_db)):

    resultado = TipoUsuarioController.create_tipo_usuario(db, payload)

    # Manejamos la respuesta lógica que programamos en el controlador si está duplicado
    if resultado == "duplicado":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un tipo de usuario con ese nombre"
        )
    return resultado


@router.put("/{id_tpu}", response_model=TipoUsuarioRead)
def actualizar_tipo_usuario(id_tpu: int, payload: TipoUsuarioUpdate, db: Session = Depends(get_db)):

    resultado = TipoUsuarioController.update_tipo_usuario(db, id_tpu, payload)

    if resultado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tipo de usuario no encontrado para actualizar"
        )
    if resultado == "duplicado":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nuevo nombre ya está siendo utilizado por otro registro"
        )
    return resultado
