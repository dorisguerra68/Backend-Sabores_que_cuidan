def test_registro_usuario_email_duplicado(client):
    payload = {
        "nombre_completo": "Doris García",
        "fecha_registro": "2026-07-14",
        "edad": 30,
        "sexo": "Femenino",
        "altura": 1.65,
        "tipo_persona": "Sano",
        "email": "duplicado@example.com",
        "password": "Clave123"
    }

    # Primer registro: debe funcionar
    response1 = client.post("/usuario/", json=payload)
    assert response1.status_code == 201

    # Segundo registro con el mismo email: debe fallar
    response2 = client.post("/usuario/", json=payload)
    assert response2.status_code == 400

    data = response2.json()
    assert data["detail"] == "El email ya está registrado."
