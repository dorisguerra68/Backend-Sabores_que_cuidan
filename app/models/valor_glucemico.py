from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base_class import Base

# 🔄 Esto evita el bucle de importaciones infinitas en Python
if TYPE_CHECKING:
    from app.models.alimento import Alimento

class ValorGlucemico(Base):
    __tablename__ = 'valor_glucemico'

    id_valorg: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    color: Mapped[str] = mapped_column(String(25))


    # Como un rango de valor glucémico puede tener MUCHOS alimentos asociados, usamos List.
    alimentos: Mapped[List["Alimento"]] = relationship(back_populates="valor_glucemico")
