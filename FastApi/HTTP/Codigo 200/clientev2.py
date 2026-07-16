from requests import post, get
url = "http://127.0.0.1:8000"
respuesta = get(url)
#la bienvenida creo un 200 OK 
print(respuesta.text)
respuesta = post(f"{url}/crear-user_v2", json={"accion":"no tengo ninguna accion"})
#creo un 201 CREATED
print(respuesta.json())
