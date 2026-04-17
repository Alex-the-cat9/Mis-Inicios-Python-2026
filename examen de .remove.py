# Alex-the-cat9 | Examen de Seguridad de Datos
# El objetivo es limpiar la lista sin que el sistema colapse.

# 1. LA BASE DE DATOS
servidor = ["Alex", "Hacker", "Gato_Ninja", "Spam", "Hacker"]

# --- RETO 1: EL HACKER FANTASMA ---
# El jefe quiere que borres al "Hacker". 
# Tu mision: Escribe la linea de codigo que borre al PRIMER Hacker 
# que aparece en la lista.
# [TU CODIGO AQUI]
print("primero detectamos al hacker agamonos de cuenta que no sabemos si esta")
#veremos cuantos hackers ay
for i in servidor:
    print("Hacker" in i)
print("Nos dijo que si ay y la uvicacion de estos 2 entonces")
servidor.remove(servidor.pop(1))
#listo
for i in servidor:
    print("Hacker" not in i)
#ahora estamos asalvo


print("es importante saber cuantos ay sino remove arruinara el codigo como este reto de aqui abajo")
# --- RETO 2: EL ERROR QUE MATA EMPRESAS ---
# Un novato trato de borrar a un usuario que NO existe:
# servidor.remove("Robot_Malvado") <-- ESTO EXPLOTARIA EL SISTEMA.
# Tu mision: Escribe un codigo SEGURO que intente borrar a 
# "Robot_Malvado" pero que use un IF para que el programa no muera.
# [TU CODIGO AQUI]
if "Robot_Malvado" in servidor:
    servidor.remove("Robot_Malvado")
#easy

# --- RETO 3: LA TRAMPA DEL POP + REMOVE ---
# Tenemos esta lista de precios:
precios = [100, 50, 100, 20]
# El Supervisor Alex lanza este comando: 
precios.remove(precios.pop(0))
#
# Pregunta de examen: ¿Cual sera el resultado FINAL de la lista 'precios'?
# A) [50, 100, 20]
# B) [50, 20]
# C) [100, 50, 20]
# [TU RESPUESTA AQUI]
print("seria la B [50, 20] porque el pop elimina al 100 pero deja informacion de el y el rmeove ve la informacion que dejo el pop y elimina al otro 100")


# --- RESULTADO FINAL ---
print(f"Estado del servidor: {servidor}")
print(f"Precios finales: {precios}")