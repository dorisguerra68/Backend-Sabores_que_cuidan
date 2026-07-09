from sqlalchemy.orm import Session
from app.models.tipo_usuario import TipoUsuario
from app.schemas.schema_tipo_usuario import TipoUsuarioCreate, TipoUsuarioUpdate

class TipoUsuarioController:

    # 1. Crear un nuevo tipo de usuario
    @staticmethod
    def create_tipo_usuario(db: Session, tipo_usuario_in: TipoUsuarioCreate):

        existing_tipo_usuario = db.query(TipoUsuario).filter(TipoUsuario.nombre == tipo_usuario_in.nombre).first()
        if existing_tipo_usuario:
            return "duplicado"

        # Si no está duplicado, creamos el objeto mapeando los datos de Pydantic a SQLAlchemy
        db_tipo_usuario = TipoUsuario(
            nombre=tipo_usuario_in.nombre
        )

        db.add(db_tipo_usuario)
        db.commit()
        db.refresh(db_tipo_usuario)
        return db_tipo_usuario

    # 2. Obtener todos los tipos de usuario (Opcional, te lo agregué por si lo necesitas)
    @staticmethod
    def get_all_tipos_usuario(db: Session):
        return db.query(TipoUsuario).all()

    # 3. Obtener un tipo de usuario por ID
    @staticmethod
    def get_tipo_usuario(db: Session, tipo_usuario_id: int):

        return db.query(TipoUsuario).filter(TipoUsuario.id_tpu == tipo_usuario_id).first()

    # 4. Actualizar un tipo de usuario
    @staticmethod
    def update_tipo_usuario(db: Session, tipo_usuario_id: int, tipo_usuario_in: TipoUsuarioUpdate):
        # Primero buscamos si el registro que se quiere actualizar existe
        db_tipo_usuario = db.query(TipoUsuario).filter(TipoUsuario.id_tpu == tipo_usuario_id).first()
        if not db_tipo_usuario:
            return None

        # Si el usuario envía un nuevo nombre, validamos que no se duplique con OTRO registro
        if tipo_usuario_in.nombre is not None:
            duplicate = db.query(TipoUsuario).filter(
                TipoUsuario.nombre == tipo_usuario_in.nombre,
                TipoUsuario.id_tpu != tipo_usuario_id  # Que no sea él mismo
            ).first()
            if duplicate:
                return "duplicado"
            db_tipo_usuario.nombre = tipo_usuario_in.nombre


        db.commit()
        db.refresh(db_tipo_usuario)
        return db_tipo_usuario
