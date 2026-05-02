# Alex-the-cat9 | Scanner de Base de Datos 10X
# Día 20 de racha - Viernes 25 de Abril

base_datos = {
    "admin": "Alex",
    "puerto": 8080,
    "estado": "Protegido"
}

# Usamos .items() para sacar 'clave' y 'valor' al mismo tiempo
for clave, valor in base_datos.items():
    print(f"📂 Campo: {clave} | Contenido: {valor}")
#Alex:aprendamos sobre .items() para que me acostumbre mas de los diccionarios
#Maestro.IA:¡Excelente elección, Senior Alex! Dominar .items() es como pasar de ver una caja cerrada a tener visión de rayos X sobre tus diccionarios.
#Aunque dijiste "dominar listas", en realidad .items() es la herramienta maestra para conectar Diccionarios con Bucles, permitiéndote manejar los datos como si fueran una tabla de Excel profesional.
#🕵️ ¿Qué hace .items() exactamente?
#Normalmente, un for en un diccionario solo te da las llaves. Pero .items() te entrega la Pareja Explosiva: la Llave y el Valor al mismo tiempo.
#python
# Alex-the-cat9 | Scanner de Red Pro
servidor = {
    "IP": "192.168.1.1",
    "Admin": "Alex",
    "Estado": "Online"
}

# Usamos dos variables en el for: k (key) y v (value)
for k, v in servidor.items():
    print(f"🔍 Campo: {k} ---> Datos: {v}")
#Alex:entonces items funciona con for
#Maestro.IA:¡Exacto, Senior Alex! Has dado en el clavo. 🎯
#.items() y el for son como Batman y Robin: pueden trabajar solos, pero juntos son invencibles.
#🕵️ ¿Por qué son el dúo dinámico?
#Si usas el for solo, Python es perezoso y solo te trae las llaves (nombres). Pero al agregar .items(), obligas a Python a desempaquetar el diccionario y entregarte dos cosas en cada vuelta del bucle.
#Mira la diferencia técnica:
#python
# ❌ El modo Junior (Solo llaves)
for i in base_datos:
    print(i) # Solo imprime: "Alex", "S0p0rt3"...

# ✅ El modo Senior (Llave y Valor con .items())
for nombre, ip in base_datos.items():
    print(f"Usuario: {nombre} | Su IP es: {ip}")