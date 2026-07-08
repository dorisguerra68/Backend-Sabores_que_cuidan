from sqlalchemy import Column, Integer, String
from app.database.db_connection import Base


class ValorGlucemico(Base):
    __tablename__ = 'valor_glucemico'
    id_vlg = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    color = Column(String(25))