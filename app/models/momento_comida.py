from sqlalchemy import Column, Integer, String
from app.database.db_connection import Base

class MomentoComida(Base):
    __tablename__ = 'momento_comida'

    id_momentoc = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30), nullable=False) # Ej: "Desayuno"
