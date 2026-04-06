#Crea una lista llamada tesoros con estos 4 elementos: "Cáliz", "Anillo", "Corona", "Espejo".
#Usa un bucle for directo (puedes usar for objeto in tesoros: o la letra que quieras).
#Dentro del bucle, imprime una frase que diga: juan encontró un: [nombre del objeto].
#El Reto de Lógica: Agrega un if dentro del for. Si el objeto es la "Corona", imprime debajo: ¡ATENCIÓN! Este objeto pertenece al Rey.
#gracias maestro(ia) are lo mejor que pueda
tesoros  = ["caliz", "anillo", "espejo", "corona",]#cambie la posicion para que el resultado diga:ATENCION este objeto pertene al rey:corona
for objetos in tesoros:
    print(f" juan encontro un:{objetos}")
    print("-------------------------")
    if objetos == "espejo":#puse espejo para que el resultado dijiera que el objeto pertenece al rey y luego diga juan encontro un:corona
        print("ATENCION este objeto pertenece al rey")
    