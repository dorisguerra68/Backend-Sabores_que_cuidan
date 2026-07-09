from pydantic import BaseModel, ConfigDict
from typing import Optional

#se crea los campos comunes
class TipoUsuarioBase(BaseModel):
    nombre: str
    color: Optional[str] = None

#crea para responder
class TipoUsuarioRead(TipoUsuarioBase):
    id_tpu: int

    model_config = ConfigDict(from_attributes=True)

#crea la logica de creación hereda el nombre y color
class TipoUsuarioCreate(TipoUsuarioBase):
    pass

class TipoUsuarioUpdate(TipoUsuarioBase):
    nombre: Optional[str]=None
    color:Optional[str]=None

