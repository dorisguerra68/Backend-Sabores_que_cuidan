from sqlalchemy.orm import Session
from app.models.tipo_usuario import TipoUsuario
from app.schemas.schema_tipo_usuario import TipoUsuarioCreate


class TipoUsuarioController:

    # Obtener todos los tipos de usuario
    def get_all(self, db: Session):
        return db.query(TipoUsuario).all()

    # Obtener un tipo de usuario por su ID
    def get_by_id(self, db: Session, id_tipo_ussuario: int):
        return db.query(TipoUsuario).filter(TipoUsuario.id_tipo_ussuario == id_tipo_ussuario).first()

    # Crear un nuevo tipo de usuario
    def create(self, db: Session, obj_in: TipoUsuarioCreate):
        db_obj = TipoUsuario(nombre=obj_in.nombre)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


# Instancia lista para usar en los routers
tipo_usuario_controller = TipoUsuarioController()
