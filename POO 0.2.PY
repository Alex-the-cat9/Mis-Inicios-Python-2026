#Alex:dame un reto de POO
#maestro.IA:¡Aceptado! Vamos a subir el nivel. Ya pasamos el Día 1 (el molde) y el Día 2 (instancias masivas).
#Ahora vamos al Reto de los Superpoderes (Métodos). 🦸‍♂️⚡Tu misión es crear una clase llamada Heroe.
#No quiero que sea solo una lista de datos; quiero que el objeto haga cosas basadas en sus estadísticas.
#📝 Especificaciones del Reto:El Molde (class Heroe):Debe nacer (__init__) con: nombre, rango (ej: S, A, B)
#y energia (un número del 1 al 100).El Poder (def entrenar):Cada vez que el héroe entrena, su energia debe subir
#+10.Si la energía llega a 100, imprime: "¡{nombre} está al máximo poder!".La Acción (def mision)
#:Debe recibir un parámetro llamado dificultad.Si la energia es mayor a la dificultad, imprime: "Misión cumplida".
#Si la energia es menor, imprime: "Misión fallida, {nombre} necesita descansar".
class heroe():#esto es una clase especificamente una de heroes
    def __init__(self,nombre, Rango,energia):#aqui ponemos __init__(self, por cierto el self es el nombre de la variable nombre,nombre es el nombre del heroe, Rango,el rango que nivel esta el heroe, y por ultimo ponemos su energia)
        self.nombre = nombre#aqui activamos el nombre
        self.Rango = Rango#aqui activamos el rango
        self.energia = energia#aqui activamos la energia
        #activamos esto porque sino no funciona
    def entrenar(self):#aqui hacemos una funcion de entrenar para que el heroe entrene junto con (self)
        #osea que estamos especificando que esta funcion solo funcione a la variable que se va meter arriba
        self.energia += 10
        #cada vez que se active su energia subira un 10 lo hacemos con {+=} mas para que suba = para que se guarde
        if self.energia > 100:#si energia supera la maxima cantidad que es 100
            print("energia limite 100 su heroe merece descanso")#heroe tiene que descansar
            self.energia = 100#y heroe no puede superar mas de 100
        else:#else si el if no funciona significa que heroe no tiene 100 de energia por lo tanto:
            #le hacemos saber que subio energia  le mostramos la energia con una barrita significando la energia maxima
            print(f"SUBIO 10 DE ENERGIA SU ENERGIA :{self.energia}/100")
        #tambien le decimos que su energia esta subiendo este print no es tan importante
        print(f"su energia esta subiendo")

        if self.energia >= 100:#aqui hacemos saber que su energia esta al maximo si la energia supera ya el 100 a 110 o mas le dira el primer if de arriba
            print(f"{self.nombre} su energia esta al MAXIMO")
    def luchar(self, dificultad):#aqui ponemos un self y una dificultad que pronto vamos a poner su nombre
        if dificultad >= self.energia:#si la dificultad supera  a energia entonces:
            print("mision fallida se necesita descansar..")#mision fallida heroe
            ganar = False#ponemos ganar = Falso/False porque no gano
        elif dificultad < self.energia:#y si dificultad no supera a energia entonces:SS
            print("mision cumplida")#mision cumplida heroe
            ganar = True#ganar = verdadero/True porque si gano
        return ganar#devolvemos la variable ganar que return lo vote afuera
nombre_heroe = input("diga su nombre heroe: ")#le pedimos al usuario que ingrese su nombre
Rango_heroe = input("diga su rango: ")#su rango
energia = 0#todos los heroes empiezan con 0 de energia
heroe1 = heroe(nombre_heroe, Rango_heroe,energia)#y aqui ya uzamos la clase el heroe numero 1 es igual clase heroe(su nombre, su rango, su energia) todo eso lo que puso el usuario lo metemos
while True:#while true un bucle que va al infinito y solo le para un error de codigo oh un break
    entrenar = input("desea entrenar? [si] [no]: ").lower()#le decimos si quiere entrenar con [] que simulan ser botones.lower() ya veran porque:
    if entrenar == "si":#aqui funciona.lower() como estamos poniendo == que es en matematica un = algo parecido entonces solo dejara entrar al si
        #no importa si es mayuscula solo deve ser si en minuscula alponer lower haces que tambien deje entrar a las mayusculas pero con la misma letra entoces si puso SI o Si o sI no entrara aqui
        #y se ira al else que el elif si el if no funciona se va al elif y si el elif no funciona se va al else que ay para su rumbo
        heroe1.entrenar()#pero como si funciono ponemos que el heroe1 quiere entrenar llamamos a la funcion
    elif entrenar == "no":#si dice que no es porque ya quiere luchar
        print("entonces supongo que estaras listo para luchar")
        ganamos = heroe1.luchar(80)#se recuerdan que return tiro la variable ganar? pues ahora ganamos lo atrapado ponemos la dificultad 80
        if ganamos:#si ganamos es True/verdadero se entrara aqui
            print("GANAMOS")
        else:#y si no se entrara aqui:
            print("PERDIMOS")

    else:
        print("heroe diga una opcion")#y si heroe no dijo ni si ni no entonces ira al else que le recuerda que diga una opcion
#niño de 10años.cloud.IA:"Oye... entiendo que heroe1 es un héroe, pero...
#¿por qué la clase se llama heroe() con paréntesis vacíos? ¿qué va ahí dentro?
#Y eso del __init__... dijiste que ahí 'ponemos' las cosas, pero ¿por qué se llama así con esos rayitos? ¿qué significa init?"
#AleX:heroe() dentro no va nada es como habrir y cerrar la clae y __init__ 
#es como iniciar clases init es como que primero se ejecute esta primera funcion y las demas se ejecuten cuando las llamemos
#niño de 10años.cloud.IA:"Okey entiendo lo de init que es como que va primero... pero dijiste que los paréntesis de heroe() están vacíos y no va nada..."
#¿Entonces para qué sirven? ¿por qué no escribimos solo class heroe sin paréntesis?
#Alex:Dios mio me falta aprender sobre herencias tendre que aprenderlo...
#Alex:por cierto ya me siento un profesor es mas divertido explicar mi codigo
#maestro.IA:¡Exactamente, Profesor Alex! Explicar el código es el nivel más alto de aprendizaje;
#si puedes explicárselo a un niño, es porque tu cerebro ya lo tiene dominado. 🧠🔥Ese "niño de 10 años"
#te ha hecho la pregunta que te va a llevar a la Herencia. Aquí tienes la respuesta técnica para que se
#la expliques y cierres esa duda:🕵️ Informe de los Paréntesis Misteriosos¿Por qué escribirlos?: En Python,
#poner class heroe() (con paréntesis) es como dejar un enchufe vacío. Por ahora no hay nada, pero ese espacio
# está reservado para decirle de quién es hijo. 🔌¿Por qué no escribir nada?: Como tú bien dijiste, al ser la clase
# "Jefa", no necesita heredar de nadie.¿Por qué algunos escriben class heroe:
#(sin paréntesis)?: Es la forma moderna. Python 3 entiende que si no hay paréntesis, es una clase independiente.