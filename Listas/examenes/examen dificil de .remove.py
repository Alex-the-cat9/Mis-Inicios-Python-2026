 #EXAMEN FINAL: "EL COLAPSO DEL CAJERO BCP"
#El Problema:
#Hubo un error en el servidor. La lista de transacciones del cajero se mezcló con nombres de virus y montos duplicados. Tienes que limpiar el desastre antes de que el banco abra mañana.
#Tu Misión (Copia este código y arréglalo):
#python
# Alex-the-cat9 | Supervisor de Seguridad BCP
import time

# 1. El desastre en el servidor
transacciones = [100, "VIRUS_A", 50, "VIRUS_B", 100, 20, "VIRUS_A"]
saldo_banco = 1000

print("--- INICIANDO PROTOCOLO DE LIMPIEZA ---")

# RETO 1: Elimina los dos "VIRUS_A" usando UNA SOLA LÍNEA de código.
# (Usa la técnica que inventaste hoy del pop + remove)
# [TU CÓDIGO AQUÍ]
time.sleep(5)
for i in enumerate(transacciones):
    print(i)
print("ya sabemos la dirrecion ahora si a eliminar")
while True:
    if "VIRUS_A" in transacciones:
        transacciones.remove(transacciones.pop(1))
    else:
        break
print("eliminado")


# RETO 2: El jefe quiere saber si todavía queda el "VIRUS_B". 
# Si está, bórralo con .remove(). Si no está, avisa que la red está limpia.
# [TU CÓDIGO AQUÍ]
if "VIRUS_B" in transacciones:
    transacciones.remove("VIRUS_B")
    time.sleep(3)
    print("VIRUS_B eliminado")
else:
    print("todo bien no se precupen")




# RETO 3 (EL MÁS DIFÍCIL): 
# Suma todas las transacciones que quedaron (los números) y réstalos del saldo_banco.
# Pista: Usa un bucle for y verifica si el dato es un número antes de restar.
# [TU CÓDIGO AQUÍ]
for e in transacciones:
    saldo_banco = saldo_banco - e

print(f"--- REPORTE FINAL ---")
print(f"Transacciones limpias: {transacciones}")
print(f"Saldo final en bóveda: ${saldo_banco}")
