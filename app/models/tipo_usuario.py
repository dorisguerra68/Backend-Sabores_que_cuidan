from sqlalchemy import Column,Integer,String
from app.database.db_connection import Base



class TipoUsuario(Base):
    __tablename__ = 'tipo_usuario'
    id_tpu = Column(Integer,primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)


