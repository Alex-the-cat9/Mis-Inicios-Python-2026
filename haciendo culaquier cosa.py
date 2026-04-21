#🛡️ EL RETO: "EL ARCHIVERO DEL BCP"
##El Escenario:
#Tienes una lista de archivos que son los pilares del banco. Un hacker va a intentar meter un virus, pero tú no vas a usar [:]. Vas a usar la técnica de Reconstrucción de Lista que aprendimos hoy.
#Tu Misión:
#Crea una lista llamada seguros con: "dinero", "clientes", "empleados".
#Crea una lista llamada servidor con esos mismos 3 elementos.
#Simula un ataque añadiendo "Hacker_Virus" al servidor.
#Crea una función llamada limpiar_banco() que:
#Cree una lista nueva vacía llamada limpieza.
#Use un for para recorrer el servidor.
#Si el archivo está en la lista de seguros, lo añade a limpieza.
#Si no está, imprime: "🚨 Peligro detectado, eliminando...".
#Al final, iguala el servidor = limpieza.
#Imprime el servidor final para demostrar que el virus ya no existe.
#🕵️ Reglas del Tech Lead:
#NO usar [:]. Queremos ver tu lógica de "caja nueva".
#Uso de not in o in: Tú decides cuál te acomoda mejor para el if.
#Mensaje Final: El programa debe terminar diciendo que el banco está seguro.
#python
# Alex-the-cat9 | Reto de Graduación Fase 1
# Día 15 de racha - Lunes 20 de Abril

seguros = ["dinero", "clientes", "empleados"]
servidor = ["dinero", "clientes", "empleados"]

# [TU CÓDIGO AQUÍ: Simular ataque y crear función]
servidor.append("HACKER_VIRUS")
limpieza = []
def limpiar_banco():
    global servidor
    for archivo in servidor:
        if archivo in seguros:
            limpieza.append(archivo)
        else:
            print(f"el intruso fue detectado y es:{archivo}")
    servidor = servidor = limpieza
limpiar_banco()
print(servidor)