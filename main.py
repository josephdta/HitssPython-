#Comentario
"""
aqui va un comentario de varias lineas
first_name="Joseph"
last_name="Tomala"
print(f"Mi nombre es {first_name} {last_name}")
#pass #Luego agregar mas codigo; es como una pausa
"""
#Convertir dolares a pesos
ARS=202.91
COL=4849.99
MEX= 18.74

nombre= input("Ingrese su nombre: ")

print(f"Hola {nombre}, Bienvenido al conversor de monedas")

print("Seleccione una de las siguientes opciones de conversión")

print("1. Dolares estadounidenses a pesos argentinos")
print("2. Dolares estadounidenses a pesos colombianos")
print("3. Dolares estadounidenses a pesos mexicanos")

opcion=int(input("Seleccione la opción: "))

if opcion==1:
    dolares= int(input("Cuantos dolares tiene: "))
    pesos= dolares * ARS
    print(f"Tienes {pesos} pesos argentinos")
elif opcion==2:
    dolares= int(input("Cuantos dolares tiene: "))
    pesos= dolares * COL
    print(f"Tienes {pesos} pesos colombianos")
elif opcion==3:
    dolares= int(input("Cuantos dolares tiene: "))
    pesos= dolares * MEX
    print(f"Tienes {pesos} pesos colombianos")
else:
    print("Opcion incorrecta")

