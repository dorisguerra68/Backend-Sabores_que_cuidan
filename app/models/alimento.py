from decimal import Decimal
from typing import List, Optional,TYPE_CHECKING
from sqlalchemy import String, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base_class import Base

# Se usa  el bloque TYPE_CHECKING de Python (que solo sirve para el autocompletado del IDE y no afecta la ejecución).
if TYPE_CHECKING:
    from app.models.valor_glucemico import ValorGlucemico
    from app.models.registro_comida import RegistroComida

class Alimento(Base):
    __tablename__ = "alimento"

    id_alimento: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    categoria: Mapped[str] = mapped_column(String(50), nullable=False)
    racion_sugerida: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False)
    unidad: Mapped[str] = mapped_column(String(20), nullable=False)
    indice_glucemico: Mapped[int] = mapped_column(Integer, nullable=False)
    id_valorg: Mapped[Optional[int]] = mapped_column(ForeignKey('valor_glucemico.id_valorg'), nullable=False)

    #  Relación con ValorGlucemico (Ajustado para usar back_populates si deseas)
    valor_glucemico: Mapped[Optional["ValorGlucemico"]] = relationship(back_populates="alimentos")

    #  Relación bidireccional con RegistroComida (Para cerrar el circuito con el archivo anterior)
    registro_comida: Mapped[List["RegistroComida"]] = relationship(back_populates="alimento")
