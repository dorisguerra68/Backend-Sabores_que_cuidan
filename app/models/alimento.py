from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from app.database.db_connection import Base
from sqlalchemy.orm import relationship

class Alimento(Base):
    __tablename__ = "alimento"
    id_alimento = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120))
    categoria = Column(String(50))
    racion_sugerida = Column(Numeric(6,2))
    unidad = Column(String(20))
    indice_glucemico = Column(Integer)
    id_vlg = Column(Integer, ForeignKey('valor_glucemico.id'))

    valor_glucemico = relationship("ValorGlucemico")

