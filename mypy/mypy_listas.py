#📋 EL PLANO DE INGENIERÍA: El Validador de Manifiestos de Carga
#Vas a diseñar un sistema que reciba una lista de cargas que entran al puerto.
#El truco es que las cargas pueden venir en dos formatos: un texto simple con el nombre del producto,
#o un reporte detallado que puede fallar y devolver None.
#1. El Tipo de Dato Mixto Avanzado (Optional / | None)En la vida real, los sensores del puerto fallan.
#Una carga puede ser un string (str) con el nombre del producto,
#o puede ser un None (si el escáner falló).Crea una lista que acepte únicamente textos o valores vacíos.
#Pista Senior: Para que Mypy acepte el None, debes usar la barra vertical:
#str | None.2. La Función Procesadora Estricta
#Diseña una función llamada procesar_manifiesto.
#Entrada: Debe recibir obligatoriamente la lista mixta
# que creaste en el paso 
#1.Salida: Debe prometer que devolverá una nueva lista que solo contenga textos (list[str]).
#¡Prohibido que salgan None de aquí!
#3. La Lógica Interna (Filtrado Seguro) Dentro de la función, debes recorrer la lista de entrada con un bucle.
#Si el elemento es un texto válido, pásalo a mayúsculas usando .upper() y guárdalo en la lista de salida.
#Si el elemento es None, ignóralo (no lo metas en la lista de salida) y haz un 
#print("🚨 Alerta: Carga corrupta detectada").
#🥷 La Regla Marcial de Mypy Estricto
#Si intentas hacer elemento.upper() directamente dentro del bucle sin poner antes un if elemento is not None:
#Mypy te pintará la pantalla de rojo de inmediato. Mypy te obliga a demostrarle que el dato es seguro antes de aplicarle
#métodos de texto.
lista:list[str | None] = ["manzana", None, "IA", None, "XD", None, None, None , None, "animal"]
def procesar_manifiesto(lista:list[str | None]) -> list[str]:
    lista_prueba:list[str] = []
    for i in lista:
        if isinstance(i, str):
            lista_prueba.append(i.upper())
        else:
            print("Alerta:carga corrupta detectada")
    return lista_prueba
aguila = procesar_manifiesto(lista)
print(aguila)



