print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 9")
print(" ")
#Define una funcion que dice la longitud de una lista
def longitud(s):
    c=0
    for elemento in s:
        c+=1
    return c

#Define una lista
liston=[20,30,40,50]
#Invoca la funcion
print(longitud(liston))