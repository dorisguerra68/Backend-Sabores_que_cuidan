def test_login_usuario(client):
    # 1. Registrar usuario primero
    registro_payload = {
        "nombre_completo": "Doris García",
        "fecha_registro": "2026-07-14",
        "edad": 30,
        "sexo": "Femenino",
        "altura": 1.65,
        "tipo_persona": "Sano",
        "email": "login@example.com",
        "password": "ClaveSegura123"
    }

    response_registro = client.post("/usuario/", json=registro_payload)
    assert response_registro.status_code == 201

    # 2. Intentar login correcto
    login_payload = {
        "email": "login@example.com",
        "password": "ClaveSegura123"
    }

    response_login = client.post("/usuario/login", json=login_payload)
    assert response_login.status_code == 200

    data = response_login.json()
    assert data["mensaje"] == "Login correcto"
    assert "usuario_id" in data


def test_login_usuario_password_incorrecta(client):
    # Registrar usuario
    registro_payload = {
        "nombre_completo": "Doris García",
        "fecha_registro": "2026-07-14",
        "edad": 30,
        "sexo": "Femenino",
        "altura": 1.65,
        "tipo_persona": "Sano",
        "email": "errorpass@example.com",
        "password": "ClaveSegura123"
    }

    client.post("/usuario/", json=registro_payload)

    # Login con contraseña incorrecta
    login_payload = {
        "email": "errorpass@example.com",
        "password": "ClaveIncorrecta"
    }

    response_login = client.post("/usuario/login", json=login_payload)
    assert response_login.status_code == 401
    assert response_login.json()["detail"] == "Contraseña incorrecta"


def test_login_usuario_email_no_existe(client):
    login_payload = {
        "email": "noexiste@example.com",
        "password": "123456"
    }

    response_login = client.post("/usuario/login", json=login_payload)
    assert response_login.status_code == 401
    assert response_login.json()["detail"] == "Email no encontrado"
