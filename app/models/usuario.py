from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db_connection import Base

class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True, index=True)
    id_tpu = Column(Integer, ForeignKey('tipo_usuario.id_tpu'))
    fecha_registro= Column(Date)
    nombre_completo = Column(String(140))
    edad = Column(Integer, nullable=True)
    sexo = Column(String(12), nullable=True)
    altura = Column(Numeric(5,2), nullable=True)
    estado = Column(String(20), default="activo")
    #email = Column(String(130), unique=True,nullable=False)
    #password_hash = Column(String, nullable=False)

    tipo_usuario = relationship("TipoUsuario")