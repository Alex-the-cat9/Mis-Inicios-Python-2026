from requests import get, post
url = "http://127.0.0.1:8000"
bienvenida = get(url)
print(bienvenida.text)
usuario = input("di el usuario que quieres buscar: ")
funcion = post(f"{url}/buscar", json={"User":usuario})
print(funcion.text)