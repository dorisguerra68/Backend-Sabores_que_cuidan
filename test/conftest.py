import sys
import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

# Añadir la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from app.database.base_class import Base
from app.database.db_connection import get_db

# Crear base de datos SQLite en memoria
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear y destruir tablas para cada test
@pytest.fixture(scope="function", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Sesión de DB para cada test
@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

# Cliente de pruebas con override de DB
@pytest.fixture(scope="module")
def client():

    def override_get_db():
        connection = engine.connect()
        session = TestingSessionLocal(bind=connection)
        try:
            yield session
        finally:
            session.close()
            connection.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
