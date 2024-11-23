print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 9")
print(" ")
#Define una funcion que elige el mayor de 3 numeros
def max_3(x1,x2,x3):
    if x1 > x2 and x3:
        print(x1)
    elif x2 > x3 and x1:
        print(x2)
    elif x3> x1 and x2:
        print(x3)
    else:
        print("Error")
#Invoca la funcion
print(max_3(22,34,45))
    