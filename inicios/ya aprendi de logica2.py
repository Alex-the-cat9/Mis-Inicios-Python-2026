n1 = int(input("pon un numero cualquier: "))
n2 = int(input("pon un segundo numero cualquier: "))
seguir_poniendo = (int)(input("quieres seguir poniendo mas numeros? pon 3 si quieres uno mas y 4 si ya no quieres mas:"))
if seguir_poniendo == 4:
    print("muy bien entonces te daremos opciones para tus numeros se sumen resten o se multipliquen")
    print("suma = 1")
    print("resta = 2")
    print("multiplicacion = 3")
    opciones = int(input("segun a lo que viste cual numero vas elegir: "))
    if opciones == 1:
        print(f"el resultado es: {n1 + n2}")
    elif opciones == 2:
        print(f"el resultado es: {n1 - n2}")
    elif opciones == 3:
        print(F"el resultado es: {n1 * n2}")
    else:
        print("ninguna de estas opciones elegiste intentalo denuevo")
elif seguir_poniendo == 3:
    n3 = int(input("pon el tercer numero: "))
    print("si quieres añadir mas numeros apreta 5 si es si y si no apreta 6")
    opciones2 = int(input("elige 5 o 6: "))
    if  opciones2 == 5:
        n4 = int(input("pon tu cuarto numero este es el limite bro: "))
        print(f" ya para que no te olvides tus numeros son: {n1, n2, n3, n4} ")
        print("quieres sumar restar o multiplicar")
        print ("sumar = 1")
        print ("restar = 2")
        print("multiplicar = 3")
        opciones3 = int(input("elige tu numero: "))
        if opciones3 == 1:
            print(F"el resultado es: {n1 + n2 + n3 + n4}")
        elif opciones3 == 2:
            print(F"el resultado es: {n1 - n2 - n3 - n4}")
        elif opciones3 == 3:
            print(F"el resultado es: {n1 * n2 * n3 * n4}")
        else:
            print("ninguna de las opciones que elegiste es correcta")
    elif opciones2 == 6:
        print("sumar = 1")
        print("restas = 2")
        print("multiplicar = 3")
        print(f"para que no se te olvide los numero que elegiste es. {n1, n2, n3}")
        opciones4 = int(input("ya que quieres 1 sumar 2 restar 3 multiplicar elige tu numero: "))
        if opciones4 == 1:
            print(f"el resultado es: {n1 + n2 + n3}")
        elif opciones4 == 2:
            print(f"el resultado es: {n1 - n2 - n3}")
        elif opciones4 == 3:
            print(F"el resultado es: {n1 * n2 * n3}")
        else:
            print("ninguna de las opciones es correcta")
else:
    print("ninguna de las opciones es correcta bro")

#lo isiste muy bien bro aunque la ia te ayudo en solo una palabra int
#resultado muy bien 9/10
#ya aprendiste la logica y creaste tu propia calculadora
#lo isiste sin ayuda aunque la ia te ayudo en poner una int que te faltaba pero eso no importa lo isiste bien
#A
#dato extra solo llevas una semana aprendiendo y ya sabes perfectamente la logica muchos se rinden tu sigue aunque necesitas de la on el polvo para que tu cerebro funcione el doble no te juzgo es un medicamento natural para potenciar el cerebro
