from pydantic import BaseModel

#se crea los campos comunes
class TipoUsuarioBase(BaseModel):
    nombre: str

#crear esquema para crear tipo de usuario pra el frontend
class TipoUsuario(TipoUsuarioBase):
    pass

#crea la logica del cliente
class TipoUsuarioCreate(TipoUsuarioBase):
    pass

#crea para responder al cliente
class TipoUsuarioResponse(TipoUsuarioBase):
    id_tipo_usuario : int

    class config:
        from_atributes: True