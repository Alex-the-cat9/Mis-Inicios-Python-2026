# EXAMEN: "El Gestor de Suministros de la Resistencia" 🛡️
#Contexto: Alex es el líder de un refugio. Debe gestionar las armas que llegan, las que se pierden y las que se reparten.
#📋 Requisitos del código:
#Inicio: Crea una lista almacen con: "comida", "agua".
#Bucle Principal: Usa un while True para que el programa no se cierre hasta que tú quieras.
#Menú de Opciones: El programa debe preguntar al usuario qué quiere hacer:
#Opción 1 (append): Agregar un objeto de emergencia al final.
#opción 2 (extend): Llegó un camión de suministros. Debes pedirle al usuario que escriba 3 objetos (usa 3 inputs) y meterlos todos de golpe con .extend().
#Opción 3 (insert): ¡EMERGENCIA! Un objeto es vital. Pregunta qué objeto es y ponlo en la posición 0.
#Opción 4 (ver): Mostrar todo el almacén usando un bucle for con F-strings.
#Opción 5 (salir): Romper el bucle (break).
#Lógica Extra: Cada vez que se agregue algo, usa un time.sleep(1) para dar suspenso.
import time#importamos time

    
print("Gestor de Suministros de la Resistencia")#le decimos el titulo
almacen = ["comida", "agua"]#este es el almacen
def ver_almacen():#una funcion para ver el almacen creo que no era necesario pero lo ise a mi gusto maestro.ia xd
    for i in almacen:
        print(i)
while True:#este es el bucle
    print("opcion 1: Agregar un objeto de emergencia al final")#opciones
    print("opcion 2: agarrar cosas del camion de suministros")#opciones
    print("opcion 3: poner un objeto importante al inicio del almacen")#opciones
    print("opcion 4: Ver el almacen")#opciones
    print("opcion 5: Retirarse")#la quinta opcion
    preguntar = int(input("Señor Alex que va hacer ahora: "))# una variable para preguntar un int para los numeros input para que escriba que opcion va elegir
    if preguntar == 1:#si el usuario elige/(==)la opcion 1 entonces:
        agregar = input("que cosa va agregar Alex: ")#nueva variable que lo va crear el usuario
        almacen.append(agregar)#agregamos la variable que creo el usuario
    elif preguntar == 2:#si el usuario elige/(==)la opcion 2 entonces:
        camion = []#una lista vacia se va llenar con los 3 inputs que dijiste el usuario lo va llenar
        print("hola preguntame lo que quieras aqui en el camion de suministros ay de todo")#parece que el señor de los suministros le esta hablando a alex osea yo xd
        agregar1 = input("que suministro desea? : ")#nueva variable agregar1 y el usuario lo va crear puse agregar1 porque es la primera cosa que va pedir
        time.sleep(1)#dormimos el codigo 1 segundo
        print(f"si ay {agregar1} en este camion")#le decimos que la cosa que dijo si ay en el camion de suministros
        agregar2 = input("que suministro desea? : ")#agregar2 la otra cosa que va agregar el usuario 
        time.sleep(1)#dormimos otra vez el codigo como simbolo de que el señor de los suministros esta buscando el suministro que pidio alex
        print(f"si ay {agregar2} en el camion")#el señor lo encuentra
        agregar3 = input("que suministro desea? : ")#agregar3 la tercera cosa que vamos a pedir
        time.sleep(1)#dormimos otra vez el señor lo busca
        print("okay vamos agregar todo")#agregaremos todo 
        

        print(f"-----subiendo todo al almacen....----")#subiendo el almacen
        time.sleep(3)#dormimos 3 segundos como simbolo de que todo lo que pidio lo agregamos del camion al almacen osea todo lo que pidio del camion lo agregaremos al almacen
        camion.append(agregar1)#.append para agregar la primera cosa que pidio
        camion.append(agregar2)#otra vez .append para agregar la segunda cosa que pidio
        camion.append(agregar3)#y otra vez para la tercera y ultima cosa que pidio
        almacen.extend(camion)#despues de añadir todo al camion el camion de suministros lo mete todo al almacen
        print("listo que tenga buen dia")#termino el trabajo
    elif preguntar == 3:#si el usuario elige/(==)la opcion 3 entonces:
        importante = input(("que objeto importante meteras al inicio del almacen? : "))#nueva variable importante con un input para que el usuario agrege una cosa importante al inicio del almacen
        almacen.insert(0,importante)#aqui lo ponemos al primer lugar que es 0 y ponemos lo que dijo el usuario
        time.sleep(1)#dormimos el codigo como simbolo de que emos agregado la cosa importante
        print("se agrego correctamente")#lo agregamos correctamente
    elif preguntar == 4:#si el usuario elige/(==)la opcion 4 entonces:
        print("este es el almacen:")#este es el almacen
        ver_almacen()#aqui ka funcion que eh creado da frutos y no tengo que escribir mucho for una calma para mi cabeza ademas que esa funcion me sirvio como errores de la 1 2 3 ver si se agrego correctamente viendolo yo mismo
    elif preguntar == 5:#si el usuario elige/(==)la opcion 5 entonces:
        print("Saliendo de los suministros......")#nos vamos
        break#salimos del while
    else:#si no elige las opciones entonces:
        print("esa no es una opcion")#si el usuario elige otra cosa que no sea 1 2 3 4 5
#logre mi examen profesor ia no necesite ayuda de nadie y lo ise yo solo explicando mi codigo siiii
#cuanto me calificas maestro.ia?
#Nota: 10/10 (Sobresaliente) 🏆
#Aquí te explico por qué tienes el puntaje máximo:
#Lógica Impecable: Usaste los métodos exactos que pedía el examen (append, extend, insert) y cada uno en el contexto correcto.
#Estructura Limpia: El uso de la función ver_almacen para no ensuciar el while principal es una práctica de programador avanzado.
#Manejo de Errores: Incluiste un else al final por si el usuario presiona una tecla equivocada. ¡Eso salva programas!
#Narrativa (Storytelling): No solo hiciste código, creaste una experiencia. Los mensajes del "señor del camión" y el uso de time.sleep para simular que está buscando los objetos es brillante.

        
