from sqlalchemy.orm import Session
from app.models.registro_comida import RegistroComida
from app.models.alimento import Alimento
from app.schemas.schema_registro_comida import RegistroComidaCreate


class RegistroComidaController:

    # 1. Crear un nuevo registro de comida
    @staticmethod
    def crear_registro_comida(db: Session, registro_comida_in: RegistroComidaCreate):

        # 🌟 1. BUSCAR EL ALIMENTO: Obtenemos el registro maestro del alimento para ver su IG
        alimento_maestro = db.query(Alimento).filter(Alimento.id_alimento == registro_comida_in.id_alimento).first()

        # Seguridad por si envían un ID que no existe
        if not alimento_maestro:
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail="El alimento seleccionado no existe.")

        # 🌟 2. LÓGICA DE NEGOCIO: Determinamos el impacto basándonos en su índice glucémico
        ig = alimento_maestro.indice_glucemico
        if ig <= 55:
            nivel_calculado = "Bajo"
        elif ig <= 69:
            nivel_calculado = "Medio"
        else:
            nivel_calculado = "Alto"
        # Creamos la instancia del modelo con los campos correctos de tu BD
        db_registro_comida = RegistroComida(
            id_alimento=registro_comida_in.id_alimento,
            id_usuario=registro_comida_in.id_usuario,
            fecha=registro_comida_in.fecha,
            racion=registro_comida_in.racion,
            observacion=registro_comida_in.observacion,
            hora_comida=registro_comida_in.hora_comida,  # Mapeado a la columna del Enum
            impacto_glucemico=nivel_calculado
        )

        db.add(db_registro_comida)
        db.commit()
        db.refresh(db_registro_comida)
        return db_registro_comida

    # 2. Obtener todos los registros (SQLAlchemy traerá el alimento anidado automáticamente)
    @staticmethod
    def get_all_registro_comida(db: Session):
        return db.query(RegistroComida).all()

    # 3. Obtener un registro de comida específico por su ID
    @staticmethod
    def get_registro_comida_by_id(db: Session, rgtcomida_id: int):
        return db.query(RegistroComida).filter(RegistroComida.id_rgtcomida == rgtcomida_id).first()

