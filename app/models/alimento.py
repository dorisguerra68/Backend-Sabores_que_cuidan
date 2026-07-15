from decimal import Decimal
from typing import List, TYPE_CHECKING
from sqlalchemy import String, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base_class import Base

# Se usa  el bloque TYPE_CHECKING de Python (que solo sirve para el autocompletado del IDE y no afecta la ejecución).
if TYPE_CHECKING:
    from app.models.registro_comida import RegistroComida

class Alimento(Base):
    __tablename__ = "alimento"

    id_alimento: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    categoria: Mapped[str] = mapped_column(String(50), nullable=False)
    racion_sugerida: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False)
    unidad: Mapped[str] = mapped_column(String(20), nullable=False)
    indice_glucemico: Mapped[int] = mapped_column(Integer, nullable=False)

    #  Relación bidireccional con RegistroComida (Para cerrar el circuito con el archivo anterior)
    registro_comida: Mapped[List["RegistroComida"]] = relationship(back_populates="alimento")

    # Una propiedad dinámica, calculamos los valores de cada nivel glucemico
    @property
    def nivel_glucemico(self) -> str:
        if self.indice_glucemico <= 30:
            return "Muy bajo"
        elif self.indice_glucemico <= 55:
            return "Bajo"
        elif self.indice_glucemico <= 69:
            return "Medio"
        else:
            return "Alto"