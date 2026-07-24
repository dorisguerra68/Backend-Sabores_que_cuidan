from decimal import Decimal
from pydantic import BaseModel, ConfigDict, field_validator

# Los campos base de alimento
class Alimento(BaseModel):
    nombre: str
    categoria: str
    racion_sugerida: Decimal
    unidad: str
    indice_glucemico: int

# Validación: la ración sugerida debe ser positiva
    @field_validator("racion_sugerida")
    def validar_racion_sugerida(cls, value):
        if value <= 0:
            raise ValueError("La ración sugerida debe ser un número positivo")
        return value

# Hereda de Alimento para poder recibir estos datos al crear uno nuevo
class AlimentoCreate(Alimento):
    pass

class AlimentoRead(Alimento):
    id_alimento: int
    nivel_glucemico: str


    model_config = ConfigDict(from_attributes=True)

# Actualizar alimento (campos opcionales)
class AlimentoUpdate(BaseModel):
    nombre: str | None = None
    categoria: str | None = None
    racion_sugerida: Decimal | None = None
    unidad: str | None = None
    indice_glucemico: int | None = None

    @field_validator("racion_sugerida")
    def validar_racion_sugerida(cls, value):
        if value is not None and value <= 0:
            raise ValueError("La ración sugerida debe ser un número positivo")
        return value