from datetime import date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.models.registro_usuario import tipoUsuario

# 1. Los campos base del usuario
class RegistroUsuarioBase(BaseModel):
    nombre_completo: str
    fecha_registro: date
    edad: Optional[int] = None
    sexo: Optional[str] = None
    altura: Optional[Decimal] = None
    tipo_persona: tipoUsuario  # Valida que sea exactamente "Sano" o "ResistenteInsulina"

# 2. Esquema para la creación (Peticiones POST)
class RegistroUsuarioCreate(RegistroUsuarioBase):
    email: str
    password: str

# 3. Esquema para leer o retornar datos (Peticiones GET)
class RegistroUsuarioRead(RegistroUsuarioBase):
    id_usuario: int
    estado: str
    email: str

    # Configuración nativa de Pydantic para leer modelos de SQLAlchemy
    model_config = ConfigDict(from_attributes=True)

# 4. Esquema para actualizar datos (Peticiones PUT/PATCH
class RegistroUsuarioUpdate(BaseModel):
    nombre_completo: Optional[str] = None
    edad: Optional[int] = None
    sexo: Optional[str] = None
    altura: Optional[Decimal] = None
    tipo_persona: Optional[tipoUsuario] = None
    estado: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

#5 Esquema para comprobar inicio de session con email+password
class LoginUsuario(BaseModel):
    email: str
    password: str