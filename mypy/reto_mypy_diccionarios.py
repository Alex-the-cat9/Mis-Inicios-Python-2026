#🏛️ EL EXPEDIENTE DEL RETO: matriz_base.py
#Pica tus bloques de código en texto plano siguiendo estrictamente este plano de ingeniería de datos :
#1. Los Dos Planos de Hierro (TypedDict)Ve al piso de arriba e importa TypedDict y List . Vas a construir una estructura anidada
#de dos pisos :Plano 1 (PlanoCargamento): Debe tener exactamente estas 2 llaves fijas:item: Texto plano (str) .peso_kg:
#Número entero (int) .Plano 2 (PlanoHangar): Debe tener exactamente estas 3 llaves fijas:nombre_hangar: Texto plano (str)
#en_servicio: Valor booleano (bool) .inventario:Debe ser una lista de diccionarios basados estrictamente en el PlanoCargamento
#que diseñaste arriba (list[PlanoCargamento]) . ¡Aquí está la trampa de alta fidelidad!2. La Instanciación (Tu Diccionario Real)
#Crea un diccionario vivo llamado hangar_central aplicando tu estructura principal: hangar_central:
#PlanoHangar = { ... } .La Inyección de Sabotaje Voluntario (Tu Misión) 🧪:
#Dentro de la lista de tu inventario, vas a agregar dos cargamentos legítimos (ej. Uranio, Misiles con sus enteros correspondientes)
#Pero al tercer cargamento le vas a meter un cable corrupto a propósito para probar el radar:
#en su llave peso_kg, en lugar de inyectar un entero, le vas a cascar un texto plano (ejemplo: "300kg" o "veinte") .
#3. El Motor de Cómputo (Tu Función Pura de la Letra L)Crea una función pura llamada calcular_peso_total .
#La Aduana de Entrada: Obliga a su parámetro a recibir un diccionario que respete estrictamente el molde mayor
#escribiendo base_datos: PlanoHangar .La Promesa de Retorno: Debe jurarle al receptor que la salida será sí o sí un número entero
#(-> int) .La lógica interna: La función debe usar un bucle for para recorrer la lista de inventario, extraer los pesos y retornar
#la suma total en el silicio.
from typing import TypedDict, List
class PlanoCargamento(List):
    [str | int]
class PlanoHangar(TypedDict):
    nombre_hangar:str
    en_servicio:bool
lista:list[str | int] = []
Plano_central:PlanoHangar = {
    "nombre_hangar":"supremo",
    "en_servicio":True
}
lista.append("00")
#lista.append(None)