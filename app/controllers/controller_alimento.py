from sqlalchemy.orm import Session
from app.models.alimento import Alimento
from app.schemas.schema_alimento import AlimentoCreate, AlimentoUpdate

class AlimentoController:

    # 1. Crear un nuevo alimento (Mapeando los datos de Pydantic a SQLAlchemy)
    @staticmethod
    def create_alimento(db: Session, alimento_in: AlimentoCreate):
        # Validar si ya existe
        existing_alimento = db.query(Alimento).filter(Alimento.nombre == alimento_in.nombre).first()
        if existing_alimento:
            return "duplicado"

        db_alimento = Alimento(
            nombre=alimento_in.nombre,
            categoria=alimento_in.categoria,
            racion_sugerida=alimento_in.racion_sugerida,
            unidad=alimento_in.unidad,
            indice_glucemico=alimento_in.indice_glucemico
        )

        db.add(db_alimento)
        db.commit()
        db.refresh(db_alimento)
        return db_alimento

    # 2. Obtener todos los alimentos (El que usaremos para listar tus 78 alimentos)
    @staticmethod
    def get_all_alimentos(db: Session):
        return db.query(Alimento).all()

    # 3. Obtener un alimento por su ID
    @staticmethod
    def get_alimento(db: Session, alimento_id: int):
        return db.query(Alimento).filter(Alimento.id_alimento == alimento_id).first()

    # 4. Actualizar un alimento
    @staticmethod
    def update_alimento(db: Session, alimento_id: int, alimento_in: AlimentoUpdate):
        db_alimento = db.query(Alimento).filter(Alimento.id_alimento == alimento_id).first()
        if not db_alimento:
            return None

        # Si viene un nombre nuevo, validamos que no se duplique con otro alimento diferente
        if alimento_in.nombre is not None:
            duplicate = db.query(Alimento).filter(
                Alimento.nombre == alimento_in.nombre,
                Alimento.id_alimento != alimento_id
            ).first()
            if duplicate:
                return "duplicado"
            db_alimento.nombre = alimento_in.nombre

        # Actualizamos los demás campos si vienen en la petición
        if alimento_in.categoria is not None:
            db_alimento.categoria = alimento_in.categoria
        if alimento_in.racion_sugerida is not None:
            db_alimento.racion_sugerida = alimento_in.racion_sugerida
        if alimento_in.unidad is not None:
            db_alimento.unidad = alimento_in.unidad
        if alimento_in.indice_glucemico is not None:
            db_alimento.indice_glucemico = alimento_in.indice_glucemico

        db.commit()
        db.refresh(db_alimento)
        return db_alimento
