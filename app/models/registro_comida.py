from sqlalchemy import Column, Integer, Numeric, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db_connection import Base


class RegistroComida(Base):
    __tablename__ = "registro_comida"

    id_rgtcomida = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), nullable=False)
    id_alimento = Column(Integer, ForeignKey('alimento.id_alimento'), nullable=False)
    id_momentoc = Column(Integer, ForeignKey('momentoc.id_momentoc'), nullable=False)
    id_tpu = Column(Integer, ForeignKey('tipo_usuario.id_tpu'), nullable=False)
    fecha= Column(TIMESTAMP, nullable=False)
    racion = Column(Numeric(6,2), nullable=False)
    observacion = Column(Text, nullable=True)

    usuario=relationship("Usuario")
    alimento=relationship("Alimento")
    momento_comidate=relationship("MomentoComida")
    tipo_usuario=relationship("Tpu")
