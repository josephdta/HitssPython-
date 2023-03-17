#/*
# * Escribe un programa que muestre por consola (con un print) los
# * números de 1 a 100 (ambos incluidos y con un salto de línea entre
# * cada impresión), sustituyendo los siguientes:
# * - Múltiplos de 3 por la palabra "fizz".
# * - Múltiplos de 5 por la palabra "buzz".
# * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
# */

fz= list(range(1,101,1))
j="fizz"
k="buzz"
m="fizzbuzz"
#print (fz)

for i in fz:
    if i%3 == 0 and i%5==0:
        print(m)
        print(" ")
    elif i%5==0:
        print(k)
        print(" ")
    elif i%3 == 0: 
        print(j)
        print(" ")
    else:
        print(i)
        print(" ")