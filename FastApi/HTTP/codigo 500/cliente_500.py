from requests import get, post
url = "http://127.0.0.1:8000"
base = {
    "calculo":"division",
    "primer":0,
    "segundo":0
}
#principal del servidor
print(get(url).text)
#servidor fallando pero se arregla solo
respuesta = post(f"{url}/numerar", json={"operacion":"division", "primer":0, "segundo":0})
print(respuesta.text)
#servidor funciona
respuesta = post(f"{url}/numerar", json={"operacion":"sumar", "primer":7, "segundo":10})
print(respuesta.text)