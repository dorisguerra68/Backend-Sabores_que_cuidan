import pytest

#Prueba crear un alimento y que calcule bien su nivel glucémico.
def test_crear_y_leer_alimento(client):

    payload = {
        "nombre": "Manzana Verde",
        "categoria": "Frutas",
        "racion_sugerida": 100.0,
        "unidad": "g",
        "indice_glucemico": 35
    }

    # 1. Probar Creación (POST)
    response_post = client.post("/alimento/", json=payload)
    assert response_post.status_code == 201
    data = response_post.json()
    assert data["nombre"] == "Manzana Verde"
    assert data["nivel_glucemico"] == "Bajo"  # Verifica la @property dinámica

    # 2. Probar Listado (GET)
    response_get = client.get("/alimento/")
    assert response_get.status_code == 200
    lista = response_get.json()
    assert len(lista) == 1
    assert lista[0]["nombre"] == "Manzana Verde"

# Prueba que el sistema no permita dos alimentos idénticos.
def test_crear_alimento_duplicado(client):

    payload = {
        "nombre": "Brócoli",
        "categoria": "Verduras",
        "racion_sugerida": 150.0,
        "unidad": "g",
        "indice_glucemico": 15
    }

    # Primera inserción exitosa
    resp1 = client.post("/alimento/", json=payload)
    assert resp1.status_code == 201

    # Segunda inserción debe fallar
    resp2 = client.post("/alimento/", json=payload)
    assert resp2.status_code == 400
    assert resp2.json()["detail"] == "El alimento ya existe"

#   Prueba que buscar un id inexistente devuelva No Encontrado.
def test_obtener_alimento_404(client):

    response = client.get("/alimento/9999")
    assert response.status_code == 404
