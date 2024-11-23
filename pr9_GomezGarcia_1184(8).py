print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 9")
print(" ")
#Define 2 listas
lista1=["Hola", "Soy", "Noe"]
lista2=["Alo", "Me llamo", "Noe"]
#Define una funcion que nos dice si un elemtno de una lista se repite en otra
def listas():
    if lista1[0]==lista2[0]:
        print("True")
    elif lista1[1]==lista2[0]:
        print("True")
    elif lista1[2]==lista2[0]:
        print("True")
    elif lista1[2]==lista2[1]:
        print("True")
    elif lista1[2]==lista2[2]:
        print("True")
    else:
        print("Error")
#Invoca la funcion
print(listas())