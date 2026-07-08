from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import config

# 2. Configuración del motor de la base de datos con PostgreSQL
engine = create_engine(
    config.database_url,
    echo=True,       # Muestra las consultas SQL en la terminal (ideal para desarrollo)
    future=True      # Asegura compatibilidad con SQLAlchemy 2.0
)

# 3. Creación de la fábrica de sesiones (Limpia y unificada)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True
)

# 4. Clase Base para que hereden todos tus modelos
Base = declarative_base()

# 5. Dependencia para inyectar la sesión en los endpoints de FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
