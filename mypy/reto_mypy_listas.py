#El Reto: El Historial de TransaccionesDebes
#escribir un módulo en Python que procese un historial de transacciones bancarias utilizando listas y tuplas, 
#asegurándote de que sea 100% compatible con la verificación estricta de mypy --strict.Las Reglas del Negocio:
#Crea una función llamada filtrar_y_convertir.Debe recibir una lista de transacciones. Cada transacción es una tupla con tres
#elementos obligatorios: (id_transaccion: int, monto: float, divisa: str).
#La función debe:Filtrar y eliminar las transacciones con montos negativos o iguales a cero.
#Convertir los montos de las transacciones restantes que estén en dólares ("USD") a euros ("EUR"), 
#multiplicando el monto por 0.92.Devolver una nueva lista que contenga únicamente los montos finales
#(números decimales) ya convertidos o aprobados
def filtrar_y_convertir(lista_de_trasacciones):
    if lista_de_trasacciones[1] <= 0:
        print("el monto es 0")
        lista_de_trasacciones[1] *= 0.92
    return lista_de_trasacciones
trassaciones: list[int| float | str] = []
print("codigo de trassacion:999")
trassaciones.append(999)
trassaciones.append(0)
print("monto:0")
trassaciones.append("tiked:100")
print("tiken:100")
filtrar_y_convertir(trassaciones)
print(f"final:{trassaciones}")