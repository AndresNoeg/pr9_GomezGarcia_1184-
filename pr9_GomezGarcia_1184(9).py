print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 9")
print(" ")
#Define una funcion que escribe x la veces que se escriba
def n_caracteres(x):
    c = 0
    while c<x:
        c += 1
        print("x", end="")


x = int(input("Ingrese un numero entero: "))
#Invoca la funcion
n_caracteres(x)
