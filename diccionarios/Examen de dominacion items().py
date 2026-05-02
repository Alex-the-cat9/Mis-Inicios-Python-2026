#Alex:okay despues de hacer ese examen esta es nuestra meta:return → try/except → archivos → JSON → proyecto agenda porque quiero aprender cyberseguridad crear mi IA y sotware para mi web
#Maestro.IA:# Alex-the-cat9 | Operación Nebula
# Día 23 de racha - 26 de Abril
#El Escenario:
#Has interceptado la base de datos de una red enemiga llamada "Nebula".
#Tienes un diccionario con los dispositivos y sus estados de seguridad (puntos de vulnerabilidad). Tu misión es generar un reporte de ataque.
red_nebula = {
    "Firewall_Centro": 0,
    "Servidor_Web": 15,
    "Base_Datos": 50,
    "PC_Secretaria": 5,
    "Router_Principal": 0
}

objetivos_criticos = 0

print("--- 🛰️ INICIANDO ESCANEO DE VULNERABILIDADES ---")

# --- TU MISIÓN ---
# 1. Usa for llave, valor in red_nebula.items():
# 2. Aplica los filtros de 0, 1-20 y > 20.
# 3. Suma a 'objetivos_criticos' cuando sea crítico.

for llave, valor in red_nebula.items():
    # AQUÍ TU LÓGICA SENIOR
    if valor == 0:
        print(f"no tienen puntos criticos:{llave}")
    elif valor < 20:
        print(f"tiene ataque pequeño pero critico:{llave}")
        objetivos_criticos += 1
    else:
        print(f"punto critico GRAVE:{llave}")
        objetivos_criticos += 1


print("\n--- 📊 REPORTE FINAL ---")
# Imprime aquí el conteo de objetivos críticos
print(f"ay en total:{objetivos_criticos} objetivos criticos")
#Maestro.IA:¡EJECUCIÓN IMPECABLE, Senior Alex! 🏆 Has pasado el examen con honores.
#Tu lógica de incluir tanto los ataques pequeños como los graves en el contador de objetivos_criticos es muy buena para Ciberseguridad,
#porque en la vida real, una grieta pequeña (como la de 5 o 15 puntos) es suficiente para que un hacker se meta al sistema.