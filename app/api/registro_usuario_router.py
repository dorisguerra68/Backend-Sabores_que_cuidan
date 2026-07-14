from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.db_connection import get_db
from app.schemas.schema_registro_usuario import (
    RegistroUsuarioCreate,
    RegistroUsuarioRead
)
from app.controllers.controller_registro_usuario import RegistroUsuarioController
from app.schemas.schema_registro_usuario import LoginUsuario

router = APIRouter(
    prefix="/usuario",
    tags=["usuario"],
)

# 1. Registrar un nuevo usuario
@router.post("/", response_model=RegistroUsuarioRead, status_code=status.HTTP_201_CREATED)
def crear_registro_usuario(payload: RegistroUsuarioCreate, db: Session = Depends(get_db)):
    try:
        resultado = RegistroUsuarioController.crear_registro_usuario(db, payload)
        return resultado
    except ValueError as e:
        # Error cuando el email ya existe
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# 2. Obtener todos los usuarios
@router.get("/", response_model=List[RegistroUsuarioRead])
def obtener_todos_los_registros(db: Session = Depends(get_db)):
    return RegistroUsuarioController.get_all_registro_usuario(db)


# 3. Obtener un usuario por ID
@router.get("/{id_usuario}", response_model=RegistroUsuarioRead)
def obtener_registro_por_id(id_usuario: int, db: Session = Depends(get_db)):
    usuario = RegistroUsuarioController.get_registro_usuario(db, id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El registro de usuario no existe."
        )
    return usuario


# 4. Eliminar un usuario
@router.delete("/{id_usuario}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_registro_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = RegistroUsuarioController.get_registro_usuario(db, id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El registro de usuario no existe."
        )

    RegistroUsuarioController.eliminar_registro_usuario(db, usuario)
    return None
# 5. Inicio de session
@router.post("/login")
def login_usuario(payload: LoginUsuario, db: Session = Depends(get_db)):
    try:
        usuario = RegistroUsuarioController.login(db,payload.email,payload.password)
        return {"mensaje":"Login correcto","id_usuario":usuario.id_usuario}
    except ValueError as e:
        raise HTTPException(status_code=401,detail=str(e))