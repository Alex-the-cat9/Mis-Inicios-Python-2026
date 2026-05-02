# Objetivo: Demostrar dominio de lógica y listas

# --- 1. MEDICIÓN (len) ---
# Tienes una lista de archivos en el servidor. 
# Muestra cuántos archivos hay en total usando la cinta métrica.
servidor = ["db.sql", "index.php", "config.py", "passwords.txt"]
total_archivos = len(servidor)
print(f"Archivos detectados: {total_archivos}")
#easy
# --- 2. ORDENAMIENTO (sort y reverse) ---
# El hacker desordenó los códigos de acceso. 
# Ordénalos de MAYOR a MENOR para encontrar la llave maestra.
codigos = [404, 102, 500, 200, 303]
# [TU CÓDIGO AQUÍ: Ordenar de mayor a menor]
codigos.sort(reverse=True)
print(f"Llave maestra (primera de la lista): {codigos[0]}")


# --- 3. BUCLE Y LÓGICA (for, and, or) ---
# Tienes una lista de usuarios. 
# Si el usuario es "ADMIN" o "ROOT", imprime "ACCESO TOTAL".
# Si el usuario es "INVITADO" and tiene nivel 0, imprime "ACCESO LIMITADO".
usuarios = ["ADMIN", "INVITADO", "ROOT"]
nivel = 0
for i in usuarios:
    if "ADMIN" == "ADMIN" and "ROOT" == "ROOT":
        print("ACCESO TOTAL")
    if "INVITADO" in i and nivel == 0:
        print("ACCESO LIMITADO")
print(f"\nEstado final del servidor: {servidor} (Debe estar vacío)")
