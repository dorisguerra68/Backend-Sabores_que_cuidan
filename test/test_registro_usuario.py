# test/test_registro_usuario.py

def test_registro_usuario(client):
    payload = {
        "nombre_completo": "Doris García",
        "fecha_registro": "2026-07-14",
        "edad": 30,
        "sexo": "Femenino",
        "altura": 1.65,
        "tipo_persona": "Sano",
        "email": "doris@example.com",
        "password": "MiClaveSegura123"
    }

    response = client.post("/usuario/", json=payload)

    # 1. Código de estado correcto
    assert response.status_code == 201

    data = response.json()

    # 2. El backend devuelve el usuario creado
    assert data["nombre_completo"] == "Doris García"
    assert data["email"] == "doris@example.com"

    # 3. El ID debe existir
    assert "id_usuario" in data

    # 4. El estado debe ser "activo"
    assert data["estado"] == "activo"

    # 5. La contraseña NO debe devolverse
    assert "password" not in data
    assert "password_hash" not in data
