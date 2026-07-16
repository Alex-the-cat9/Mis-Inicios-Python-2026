from requests import get, post
url = "http://127.0.0.1:8000"
#codigo 200 por bienvenida get
print(get(url).text)
#los datos qeu meteremos
paqueteDE_Datos = {
    "combustible":100,
    "marca":"vinguini",
    "velocidad":100,
    "clave":"Alex10"
}
#error 400 por la clave corta
admin = post(f"{url}/creacion", json={"combustible":100, "marca":"vinguini", "velocidad":100, "clave":"Alex"})
print(admin.json())
#error 400 por exeso de combustible
admin = post(f"{url}/creacion", json={"combustible":1000, "marca":"vinguini", "velocidad":100, "clave":"Alex1021"})
print(admin.json())
#error 429 por exceso de velocidad
admin = post(f"{url}/creacion", json={"combustible":100, "marca":"vinguini", "velocidad":1000, "clave":"Alex211"})
print(admin.json())
#error 400 por copiarse de una marca
admin = post(f"{url}/creacion", json={"combustible":100, "marca":"Volvo", "velocidad":100, "clave":"Alex1111"})
print(admin.json())
#codigo 201 por creacion del carro sin errores
admin = post(f"{url}/creacion", json={"combustible":100, "marca":"vinguini", "velocidad":100, "clave":"Alex11111"})
print(admin.json())