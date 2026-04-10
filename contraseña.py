#este codigo lo ise yo mismo con lo que reconosco de mi mismo


intentos = 3#intentos le quedan 3
contraseña = 2255#esta es la contraseña
while intentos > 0:#si intentos llega a 0 entonces el while se detendra
    print(f"Te quedan {intentos}/3 intentos")#le recordamos que le quedan intentos
    vereficar = int(input("ingrese su contraseña: "))#nueva variable vereficar un int para numeros y input para preguntar
    if vereficar == contraseña:#si vereficar es igual a contraseña que es 2255 entonces:
        print("Bienvenido")#le diremos que es bienvenido y:
        break#saldremos del bucle
    else:#si el if no es correcto vendra a el else pude usar elif pero el else me favorece mas ademas no tiene sentido usar elif xd nose sigamos con el codigo
        print("contraseña incorrecta")#le recordamos que la contraseña es incorrecta
        intentos = intentos - 1#hacemos que intentos se reste para que el while intentos > 0: se cumpla y si intentos llega a 0 dara false
if intentos == 0:#si salio del bucle por los intentos y no porque puso la contraseña correcta entonces le diremos un mensaje:
    print(f"tienes {intentos} intentos vuelve a intentarlo mañana posiblemente no eres el dueño")#el mensaje
#bueno gracias regrese con ganas ayer uvo un apagon y no pude subir codigos lamento que mi cuadro en mi perfil este gris no volvera a pasar
#me gusta que este en verde mis cuadros en mi perfil hoy dare un viaje que durara 24 horas pero estoy bien no se precupen amigos de git hub