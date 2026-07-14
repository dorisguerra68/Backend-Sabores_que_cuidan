from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext

from app.models.registro_usuario import Usuario
from app.schemas.schema_registro_usuario import RegistroUsuarioCreate, RegistroUsuarioUpdate
from app.schemas.schema_registro_usuario import LoginUsuario

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class RegistroUsuarioController:

    # Función interna para hashear contraseña
    #Hashear una contraseña significa transformarla en una cadena irreconocible
    # usando un algoritmo matemático especial (como bcrypt)
    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    # 1. Crear un nuevo registro de usuario
    @staticmethod
    def crear_registro_usuario(db: Session, registro_usuario_in: RegistroUsuarioCreate):
        try:
            db_registro_usuario = Usuario(
                nombre_completo=registro_usuario_in.nombre_completo,
                fecha_registro=registro_usuario_in.fecha_registro,
                edad=registro_usuario_in.edad,
                sexo=registro_usuario_in.sexo,
                altura=registro_usuario_in.altura,
                tipo_persona=registro_usuario_in.tipo_persona,
                estado="activo",

                # NUEVO
                email=registro_usuario_in.email,
                password_hash=RegistroUsuarioController.hash_password(registro_usuario_in.password)
            )

            db.add(db_registro_usuario)
            db.commit()
            db.refresh(db_registro_usuario)
            return db_registro_usuario

        except IntegrityError:
            db.rollback()
            raise ValueError("El email ya está registrado. Usa otro email.")

    # 2. Obtener todos los registros de usuarios
    @staticmethod
    def get_all_registro_usuario(db: Session):
        return db.query(Usuario).all()

    # 3. Obtener un registro de un usuario específico por su ID
    @staticmethod
    def get_registro_usuario(db: Session, id_usuario: int):
        return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

    # 4. Eliminar un usuario de la base de datos (Físico)
    @staticmethod
    def eliminar_registro_usuario(db: Session, db_usuario: Usuario):
        db.delete(db_usuario)
        db.commit()
        return True

    #si al iniciar session funciona
    @staticmethod
    def login(db: Session, email: str, password: str):
        usuario = db.query(Usuario).filter(Usuario.email == email).first()

        if not usuario:
            raise ValueError("El email no encontrado")

        if not pwd_context.verify(password, usuario.password_hash):
            raise ValueError("Contraseña incorrecta")

        return usuario

