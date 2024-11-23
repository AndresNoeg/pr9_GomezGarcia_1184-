# pr9_GomezGarcia_1184-

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 9")
print(" ")
#Define funcion que elige el mayor de 2 numeros
def max(a, b):
    if a > b:
        return a
    else:
        return b
#Invoca la funcion
print(max(21,22))

![image](https://github.com/user-attachments/assets/40b969b8-0016-4080-a0bd-458e4ab27e13)

![image](https://github.com/user-attachments/assets/3502e932-d868-4d26-b3a8-bc96674b3bcb)

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

![image](https://github.com/user-attachments/assets/119f98fc-a57f-4a43-ac72-ba2b2b9ce107)

![image](https://github.com/user-attachments/assets/f6ff856c-be40-44ff-82f6-b18a40c6056e)

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

![image](https://github.com/user-attachments/assets/2bfbb0e8-c8c0-4bf4-9ebb-40d9366ac901)

![image](https://github.com/user-attachments/assets/c71b82a9-9a05-48c7-b0d6-e90fae71eb84)

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 9")
print(" ")
#Define una funcion que dice si una letra es vocal
def tf():
    if x=="a" or "A":
        print("True")
    elif x=="e" or "E":
        print("True")
    elif x=="i" or "I":
        print("True")
    elif x=="o" or "O":
        print("True")
    elif x=="u" or "U":
        print("True")
    else:
        print("False")
#Pide una letra al usuario
x=str(input("Ingrese una letra: "))
#Invoca la funcion
print(tf()) 

![image](https://github.com/user-attachments/assets/7eaec44e-bd5e-4ea8-933e-fc8c4fd1eb56)

![image](https://github.com/user-attachments/assets/6d8c8d70-3c4f-4cb1-b0b8-473824fae83c)

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 9")
print(" ")
#Define lista
lista=[1,2,3,4]
#Define una funcion que suma los elementos de la lista
def sum():
    r=lista[0]+lista[1]+lista[2]+lista[3]
    print(r)
#Define una funcion que multiplica los elementos de la lista
def multip():
    r1=lista[0]*lista[1]*lista[2]*lista[3]
    print(r1)

#Invoca la primera funcion
print(sum())
print(" ")
#Invoca la segunda funcion
print(multip())

![image](https://github.com/user-attachments/assets/2b0ff7ba-0b1f-475b-95f1-c59e3e39f180)

![image](https://github.com/user-attachments/assets/44c4de94-c280-4083-bc23-fb1025bc2ae2)

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 9")
print(" ")
#Define una variable string
x="estoy probando"
#Define una funcion que escribe el mensaje en inversa
def inversa():
    return x[::-1]
    print()

#Invoca la funcion
print(inversa())

![image](https://github.com/user-attachments/assets/0ad4dab9-2f8d-431d-bfd6-890715173a31)

![image](https://github.com/user-attachments/assets/6d535f91-5158-4a45-919a-353b0155a606)


print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 9")
print(" ")
#Define una variable string
x="radar"
#Define una funcion que identifica los palindromos
def palindromo():
    if x[::-1]== x:
        print("Es un palindromo")
    else:
        print("Esto no es un palindromo")
#Invoca la funcion
print(palindromo())

![image](https://github.com/user-attachments/assets/21d24290-59ea-4f69-b151-09c79d8b0cbe)

![image](https://github.com/user-attachments/assets/ec99ea8d-0fa9-4199-aedb-3bb2519b6f24)

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

![image](https://github.com/user-attachments/assets/dc0f371a-11d3-4746-92bf-32eb21f4cbcf)

![image](https://github.com/user-attachments/assets/80ee0143-85c1-423d-a6c2-b288d3fffc7d)


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

print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 9")
print(" ")
#Define una funcion en la cual se escribe * las veces que quiera el usuario
def histograma(lista):
    for numero in lista:
        print('*' * numero)

#Invoca la funcion
histograma([5,4,3,2,1])

![image](https://github.com/user-attachments/assets/c54af49b-723d-40c4-8bfa-78a2611e9ff6)

![image](https://github.com/user-attachments/assets/2097d87c-9f5c-42ca-b472-826f774d0ff7)





