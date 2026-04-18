#EXAMEN FINAL: "EL CAOS DEL INVENTARIO RPG"
#El Problema:
#Tienes una lista de items de tu juego, pero el servidor los mezcló. Hay nombres con mayúsculas locas y números que son texto.
#Tu Misión:
#Ordena la lista de tal manera que el "10_Pociones" aparezca al final (porque el 10 es mayor que el 2) y que "espada" no se quede al último solo por ser minúscula.
#Pista: Tienes que usar la "Magia Negra" que domina tanto el texto como el número.
#python
# Alex-the-cat9 | Examen de Graduación .sort()
# Objetivo: Ordenar ignorando mayúsculas y tratando todo como texto.

items = ["espada", "2_Escudos", "Arco", "10_Pociones"]

# [TU CÓDIGO AQUÍ]
# Pista: Usa el 'key' que convierte TODO a texto y a minúsculas.
items.sort(key=str.lower)


# --- EL RESULTADO ESPERADO ---
# La lista debe quedar así: ['2_Escudos', '10_Pociones', 'Arco', 'espada']
# (Porque en ASCII los números van antes que las letras)

print(f"Inventario Organizado: {items}")