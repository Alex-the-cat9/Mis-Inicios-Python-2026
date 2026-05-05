import json
#📝 EXAMEN DE CERTIFICACIÓN JSON (NIVEL SENIOR)FASE 1: Teoría de Combate (Conceptos)Responde
# con tus propias palabras:¿Qué diferencia hay entre usar "r" y "w" en el open?
# Si tengo un diccionario en mi código y quiero que se convierta en un archivo físico, 
# ¿uso load o dump?¿Por qué es buena idea usar indent=4?FASE 2:
#  Localización de Errores (Debug)Mira este código. Tiene 2 errores fatales que harán que explote
#  o que no guarde nada. ¿Cuáles son? 🕵️‍♂️pythonimport json
#mochila = {"pocion": 3, "cuchillo": 1}
#
#with open("mochila.json", "r") as archivo:
#    json.dump(archivo, mochila)#aqui esta los errores archivo y mochila van al revez y "r"no se usa para dump sino para load
#Usa el código con precaución.FASE 3: El Gran Reto Práctico (El Código) 🟩🔥Crea un único script de Python que cumpla esta misión:
#Cargar: Intenta abrir un archivo llamado mision.json y carga los datos en una variable. Si el archivo no existe (usa try/except),
#crea un diccionario que diga: {"estado": "inicio", "puntos": 0}.Modificar: Pide al usuario que escriba cuántos puntos ganó hoy.
#Súmaselos a los puntos que ya tenías en el diccionario.Tatuar: Guarda el diccionario actualizado en el mismo archivo mision.json
#con indent=4 y ensure_ascii=False.🕵️ Reglas del Senior Alex:Puedes consultar tus notas o tus archivos anteriores 
#(un buen programador sabe dónde buscar).Cuando termines la Fase 3, pégame el código aquí abajo.Alex, si logras
#que los puntos se acumulen cada
#Alex:"w" es para borrar todo
#Alex:"r" r es para revisar si queremos modificar se usan los dos primero el r
#Alex:deves usar dump para que se convierta en un json porque load es si ya tienes el archivo
#Alex:es buena idea usar indent=4 para darle espacio a los diccionariosel
try:
  mochila = {"pocion": 3, "cuchillo": 1}

  with open("mochila.json", "r") as archivo:
     json.dump(archivo, mochila)
except FileNotFoundError:
   memoria = {
      "estado":"Inicio",
      "puntos":0
   }
while True:
   try:
      puntos = int(input("cuantos puntos isiste hoy?: "))
   except ValueError:
      print("solo numeros porfavor")
   else:
      print("guardando puntos....")
      memoria["puntos"] += puntos
      memoria["estado"] = "progreso"
      if memoria["puntos"] >= 0:
         memoria["estado"] = "inicio"
      with open("progreso de puntos.json", "w", encoding="utf-8") as f:
         json.dump(memoria, f, indent=4, ensure_ascii=False)
