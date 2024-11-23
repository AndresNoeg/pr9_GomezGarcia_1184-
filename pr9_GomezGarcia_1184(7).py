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