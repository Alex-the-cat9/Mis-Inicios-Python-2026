#🚀 Tu Reto "Automatizador de Commits" (Día 21) 🟩🔥
#3Para que no te olvides de estos comandos, vamos a programar un simulador de consola.
#Misión:
#Crea una lista llamada comandos = ["git add .", "git commit", "git push"].
#Pídele al usuario (tú) que escriba el comando para subir archivos.
#Usa un if con in para verificar si lo que escribiste está en la lista de comandos.
#Lógica Pro:
#Si escribes "git push", imprime: "🚀 ¡Cuadro verde pintado con éxito!".
#Si es otro de la lista, imprime: "📦 Preparando archivos...".
comandos = ["git add", "git commit", "git push"]
for i in comandos:
    print(i)
pedir = input("QUE comando vas usar para subir el archivo: ")
if pedir == "git push":
    print("cuadro verde pintado con exito")
else:
    print("preparando archivos")