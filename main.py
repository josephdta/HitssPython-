#Programa para convertir dolares a pesos
ARS=202.91
COL=4849.99
MEX= 18.74

nombre= input("Ingrese su nombre: ")

def menu():
    print(f"Hola {nombre}, Bienvenido al conversor de monedas")
    print("Seleccione una de las siguientes opciones de conversión")
    print("1. Dolares estadounidenses a pesos argentinos")
    print("2. Dolares estadounidenses a pesos colombianos")
    print("3. Dolares estadounidenses a pesos mexicanos")
    print("4. Salir del programa")
    #return opcion
def validacion():
    opt=int(input("Seleccione la opción: "))
    if opt==1:
        dolares= int(input("Cuantos dolares tiene: "))
        pesos= dolares * ARS
        print(f"Tienes {pesos} pesos argentinos")
        #menu()
    elif opt==2:
        dolares= int(input("Cuantos dolares tiene: "))
        pesos= dolares * COL
        print(f"Tienes {pesos} pesos colombianos")
        #menu()
    elif opt==3:
        dolares= int(input("Cuantos dolares tiene: "))
        pesos= dolares * MEX
        print(f"Tienes {pesos} pesos colombianos")
        #menu()
    elif opt==4:
        print("¡Gracias por usar nuestro programa!")
    else:
        print("Opcion incorrecta")
        #menu()
menu()
validacion()

    

