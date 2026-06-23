#¡Perfecto! Vamos a practicar con choice (en singular). Recuerda sus dos reglas de oro:
#No acepta probabilidades (weights). Todos tienen la misma oportunidad.
#Te devuelve el elemento directo y limpio, así que ya no tienes que escribir el `` al final.
#Vamos a modificar tu programa de los alumnos. Esta vez, haremos algo divertido: crearemos un diccionario con 3
#premios diferentes (un punto extra, una golosina o salvarse del examen). Usaremos choice para asignarle un premio sorpresa
#al alumno que salga suertudo.Aquí tienes el código para practicar:

# Tu diccionario original de alumnos
from random import choice
#Alex:yo documentare el codigo y lo traducire
alumnos = {#diccionario variable alumno atrapa todo este texto
    "Gabriel": 15,
    "Alex": 10,
    "Pepe": 20,
    "Pepito": 12,
    "Alexis": 10
}#ya vimos todo sus nombres  y notas

# Lista de premios sorpresa
premios = ["Un punto extra", "Una caja de chocolates", "Borrar su peor nota"]

reprobados: list[str] = []#lista de reprovados pero lo voy a corregir porque mypy me pone en rojo Antes: reprobados = []

# Clasificamos a los reprobados igual que en tu código
for nombre, nota in alumnos.items():#llave y valor usa el metodo items para separarlos en dos partes
    if nota < 15:#si el valor es menos que int(15) entonces este if se activa
        reprobados.append(nombre)#la lista de antes que yo puse str para guardar los nombres la IA separa la llave y los mete en reprovados

print(f"Alumnos reprobados: {reprobados}\n")

# --- AQUÍ USAMOS CHOICE ---

# 1. Elegimos un alumno al azar (salida limpia, sin)
alumno_suertudo = choice(reprobados)#aqui esta la magia ise from random import choice le dije vaya al archivo random y traime choice
#lo que hace es solo elegir un reprovado de esta lista que creamos elegira un nombre y lo guardara en alumno_suertudo

# 2. Elegimos un premio al azar de la otra lista
premio_ganado = choice(premios)
#elegira un premio y lo guardara en premio_ganado la lista de premios esta arriba con tres premios
print("=== RESULTADO DEL SORTEO ===")
print(f"¡El alumno suertudo es: {alumno_suertudo}!")
print(f"Se ha ganado el siguiente premio: ✨ {premio_ganado} ✨")
#Usa el código con precaución.💡 Fíjate en estos dos detalles:Mira las líneas de choice:
#choice(reprobados) y choice(premios). Al no llevar la "s", no generan listas con corchetes, por lo que las variables guardan
#directamente los textos ("Pepito", "Un punto extra", etc.).Al imprimir, pudimos usar las variables directo en el texto
#(f"{alumno_suertudo}") sin que aparezcan corchetes feos en la pantalla.