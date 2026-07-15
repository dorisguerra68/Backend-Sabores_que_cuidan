from decimal import Decimal
from pydantic import BaseModel, ConfigDict

# Los campos base de alimento
class Alimento(BaseModel):
    nombre: str
    categoria: str
    racion_sugerida: Decimal
    unidad: str
    indice_glucemico: int

# Hereda de Alimento para poder recibir estos datos al crear uno nuevo
class AlimentoCreate(Alimento):
    pass

class AlimentoRead(Alimento):
    id_alimento: int
    nivel_glucemico: str


    model_config = ConfigDict(from_attributes=True)

class AlimentoUpdate(Alimento):
    pass
