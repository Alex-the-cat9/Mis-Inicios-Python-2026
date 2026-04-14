#aprendiendo .pop mi m aestro ia me explica como se usa y para que cosas sirve yo aqui dare resultados
#ya sabia antes de .pop elimina lo ultimo de la lista a lo que tengo entendido pero hoy lo dominaremos por completo
# ============================================================
# DISCUSIÓN TÉCNICA: .REMOVE() VS .POP() - EL DEBATE MAESTRO
# Participantes: Alex-the-cat9 y su Socio de Código (IA)
# Fecha: Martes 14 de Abril (Día de la Gran Recuperación)
# ============================================================

# DISCUSIÓN:
# Alex: ¿En funcionamiento cuál es mejor para que la PC corra rápido, .pop o .remove?
# Socio IA: Para la computadora, .pop() al final es el rey. No tiene que buscar nada.
# .remove() es más pesado porque tiene que mirar "cara por cara" cada objeto hasta encontrar el nombre.

# Alex: ¿Y qué pasa con la "Magia Negra" de .remove()?
# Socio IA: Imagina que Alex está en un bosque oscuro y un Orco Invisible le roba algo. Alex no sabe en qué posición de la mochila está su "amuleto", solo sabe que tiene que deshacerse de la "piedra maldita" porque pesa mucho.
#Con .pop(): Alex tendría que prender una linterna, contar los bolsillos (0, 1, 2...), encontrar la piedra y luego sacarla. ¡Mucho trabajo!
#Con .remove("piedra maldita"): Alex solo dice el nombre y Python, como si tuviera un imán mágico, recorre toda la mochila en la oscuridad, encuentra la piedra y la desintegra.
# Alex: entonces puede servir para input porque el programador si sabe la pocision pero el usuario no entonces le decimos que quiere eliminar con la variable preguntar y como no sabe la pocision
#  entonces el pone en texto lo que quiere borrar y yo lo ago mochila.remove(preguntar) y ya se elimina
#Socio IA: ¡Exactamente! Has dado en el clavo del Diseño de Experiencia de Usuario. 🎯 

#mi maestro me explicaba cosas de .pop todo empezo por este codigo:
#mochila = ["madera", "piedra", "diamante"]
#mochila.insert(0, mochila.pop(2))
#print(f"Mochila teletransportada: {mochila}")
#no le entendi de donde sacaba diamante porque el insert se queda sin nada de texto y el .pop elimina el diamante entonces como magia negra aparecia diamante me explico a profundo y entendi que:
mochila = ["madera", "piedra", "diamante"]#esta es la mochila inicial
mochila.insert(0,mochila.pop(2))#.remove mata a diamante de imediato sin piedad pero .pop lo deja vivir por un tiempo .pop tambien lo mata a diamante pero lo deja medio muerto pero si lo mata despues viene .insert que revive a diamante
#y completa su funcion insert(0, diamante) no me refiero a que insert revive codigo sino a que .pop hace que lo que elimino tenga la posibilidad de revivir pero no en su mismo lugar y tiene poco tiempo de revivir ya que en la siguiente linea el codigo "diamante"muere
#a lo que me refiero esque .pop lo saca de su lugar y le da una oportunidad si alguien interfiere pero si nadie interifere en el segundo codigo muere el texto pero si alguien si interfiere como insert entonces .pop lo deja
#es como si lo dejara libre pero ya en el vacio y insert lo pone en un lugar si quiere puede ponerlo en su mismo lugar saben a lo que me refiero xd
print(f"en el primer lugar esta:{mochila[0]}")#entendi que lo cambia de lugar pero lo que hace es eliminarlo de su lugar y ponerlo a otro
for i in mochila:#for inecesario pero para ver los lugares exactamente de la mochila
    print(i)
print("cambiaron de lugar a diamante y lo pusieron en el primer lugar")
#tambien se que .pop sirve igual que remove .pop(1) eliminas si solo poner .pop()solo entonces eliminara lo ultimo de la lista