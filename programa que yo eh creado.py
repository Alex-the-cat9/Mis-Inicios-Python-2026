banco = {
    "Alex":200,
    "Alexa":0,
    "jefe":1000
}
print("eres Alex lograste hacer tu trabajo ahora tu jefe te va remconpensar")
banco["jefe"] -= 200
banco["Alex"] += 200
print("alexa (tu ia asistente virtual) te pide dinero /")
while banco["Alex"] > 0:
    dar = int(input("cuanto basa trasferir? y pon 0 para acabar de trasferir: "))
    if dar == 0:
      break
    if dar <= 20:
     banco["Alex"] -= dar
     print("Alexa:gracias igualmente no te importo") 
    elif dar <= 100:
      banco["Alex"] -= dar
      print("Alexa:muchas gracias querido amo")
    elif dar <= 200:
      banco["Alex"] -= dar
      print("WOW gracias me comprare muchas cosas")
    elif dar == 400:
      banco["Alex"] -= dar
      print("Alexa:gracias señor estoy plenamente agradecido con usted le juro que le servire asta mi muerte")
if banco["Alex"] == 0:
  print("te quedaste sin dinero pendejo")
elif banco["Alex"] > 300:
  print("bien almenos ahorraste muy bien")
if banco["Alex"] == 400:
    print("muy bien no dependes de nadie senior Alex")
 
