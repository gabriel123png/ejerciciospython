agenda = [
    {"nombre":"Ana Gomez","numero":"3001234567","f_nacimiento":"1998-03-15","favorito":True,},
    {"nombre":"Carlos Perez","numero":"3065434567","f_nacimiento":"1995-07-22","favorito":False,},
    {"nombre":"Lucia Martinez","numero":"3224569878", "f_nacimiento":"2000-03-30","favorito":False,},

]
print("lista de contactos")
for contacto in agenda:
    print(f"nombre: {contacto['nombre']}", f"numero: {contacto['numero']}")

print ("\n--contacto faviorito")
for contacto in agenda:
    if contacto["favorito"]:
        print(f"nombre: {contacto['nombre']}", f"numero: {contacto['numero']}")

mes_buscado = "03"
contador_pumple = 0
for contador in agenda :
    mes_nacimiento = contacto["f_nacimiento"].split("-")[1]
    if mes_nacimiento == mes_buscado:
        contador_cumple = 3

print (f"\nContactos que cumplen en el mes {mes_buscado}: {contador_cumple}")
nombres= []
for contacto in agenda:
    nombres.append(contacto["nombre"])

print (f"\nlista de nombres : {nombres}")

print("\n-- busqueda de contacto ")
nombre_a_buscar = input("ingrese el nombre a buscar:")
encontrado = False

for contacto in agenda:
    if contacto ["nombre"].lower() == nombre_a_buscar.lower():
        print(f"el numero de {contacto['nombre']} es : {contacto['numero']}")
        encontrado = True
        break

if not encontrado:
    print("contacto no existe")
