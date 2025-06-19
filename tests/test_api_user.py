import requests

# def test_get_users_status_code():
#     """
#     Verifica que la API de usuarios devuelva un codigo de estado 200 (ok)
#     """
#     response = requests.get("https://reqres.in/api/users?page=2")
#     assert response.status_code == 200

# def test_get_users_contains_data():
#     """
#     Verifica que la respuesta contiene una clave "data" con la respuesta de al menos un usuarios
#     """
#     response = requests.get("https://reqres.in/api/users?page=2")
#     json_data = response.json()
#     assert "data" in json_data
#     assert len(json_data["data"]) > 0

# ✅ Test 1: Verificar que obtener un usuario específico funciona
def test_get_single_user():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert data["data"]["id"] == 2

# ❌ Test 2: Obtener un usuario inexistente debería devolver 404
def test_get_user_not_found():
    response = requests.get("https://reqres.in/api/users/999")
    assert response.status_code == 404

# 🧪 Test 3: Crear un usuario correctamente
def test_create_user():
    payload = {
        "name":"Dayan",
        "job":"QA Engineer"
    }        
    response = requests.post("https://reqres.in/api/users",json = payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Dayan"
    assert data["job"] == "QA Engineer"
    assert "id" in data
    assert "createdAt" in data

# 🧪 Test 4: Borrar un usuario
def test_delete_user():
    response = requests.delete("https://reqres.in/api/users?page=1")
    assert response.status_code == 204

# 🔄 Test 5: Verificar que la estructura de datos del listado de usuarios sea consistente
def test_users_data_structure():
    response = requests.get("https://reqres.in/api/users?page=1")
    data = response.json()
    assert isinstance(data["data"],list)
    for user in data["data"]:
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
        assert "avatar" in user