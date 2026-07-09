from fastapi.testclient import TestClient
from fastapi import status
from main import app



client = TestClient(app)

# 1. Test para verificar que se crea un tipo de usuario con éxito (Create)
def test_crear_tipo_usuario_exitoso():
    response = client.post(
        "/tipos-usuario/",
        json={"nombre": "Resistencia a la insulina"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["nombre"] == "Resistencia a la insulina"
    assert "id_tpu" in response.json()  # Verifica que la base de datos asignó un ID

# 2. Test para verificar nuestra regla de negocio en español (Error 400 - Duplicado)
def test_crear_tipo_usuario_duplicado():
    # Intentamos crear el mismo que ya existe en el entorno de pruebas
    response = client.post(
        "/tipos-usuario/",
        json={"nombre": "Resistencia a la insulina"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    # Verificamos que devuelva el mensaje exacto en español que programaste
    assert "ya está registrado en el sistema" in response.json()["detail"]

# 3. Test para buscar un ID que no existe (Error 404 - Not Found)
def test_obtener_tipo_usuario_inexistente():
    response = client.get("/tipos-usuario/99999")  # Un ID falso
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "No se encontró ningún tipo de usuario" in response.json()["detail"]
