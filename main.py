#Programa para convertir dolares a pesos
ARS=202.91
COL=4849.99
MEX= 18.74
PREGUNTA="Cuantos dolares tiene: "
nombre= input("Ingrese su nombre: ")

def menu():
    print(f"Hola {nombre}, Bienvenido al conversor de monedas")
    print("Seleccione una de las siguientes opciones de conversión")
    print("1. Dolares estadounidenses a pesos argentinos")
    print("2. Dolares estadounidenses a pesos colombianos")
    print("3. Dolares estadounidenses a pesos mexicanos")
    print("4. Salir del programa")
    
def validacion():
    opt=int(input("Seleccione la opción: "))
    if opt!=1 or opt !=2 or opt!= 3 or opt!=4:
        print("Opcion incorrecta")
    if opt==1:
        print(f"{PREGUNTA}")
        dolares= int(input(" "))
        pesos= dolares * ARS
        print(f"Tienes {pesos} pesos argentinos")
        
    elif opt==2:
        print(f"{PREGUNTA}")
        dolares= int(input(" "))
        pesos= dolares * COL
        print(f"Tienes {pesos} pesos colombianos")
        
    elif opt==3:
        print(f"{PREGUNTA}")
        dolares= int(input(" "))
        pesos= dolares * MEX
        print(f"Tienes {pesos} pesos colombianos")
        
    elif opt==4:
        print("¡Gracias por usar nuestro programa!")
    
     
menu()
validacion()

    

