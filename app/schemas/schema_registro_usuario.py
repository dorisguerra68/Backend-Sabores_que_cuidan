from datetime import date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.models.registro_usuario import tipoUsuario

# BASE: Campos comunes para crear y leer
class RegistroUsuarioBase(BaseModel):
    nombre_completo: str
    fecha_registro: date
    edad: Optional[int] = None
    sexo: Optional[str] = None
    altura: Optional[Decimal] = None
    tipo_persona: tipoUsuario
    estado: str
    email: str


# CREATE: Para POST (incluye password en texto plano)
class RegistroUsuarioCreate(RegistroUsuarioBase):
    password: str   # Solo se recibe, NO se devuelve


# READ: Para GET (lo que se devuelve al frontend)
class RegistroUsuarioRead(RegistroUsuarioBase):
    id_usuario: int

    model_config = ConfigDict(from_attributes=True)


# UPDATE: Para PUT/PATCH
class RegistroUsuarioUpdate(BaseModel):
    nombre_completo: Optional[str] = None
    edad: Optional[int] = None
    sexo: Optional[str] = None
    altura: Optional[Decimal] = None
    tipo_persona: Optional[tipoUsuario] = None
    estado: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None  # Se recibe, luego se hashea


# LOGIN: Para iniciar sesión
class LoginUsuario(BaseModel):
    email: str
    password: str
