print("Bienvenido al programa. ")

#Bucle para solicitar al usuario un numero entero positivo
while True:
    try:
        n = int(input("Ingrese un numero entero positivo: "))
        #Se verfica si el numero ingresado es positivo
        if n <= 0:
            print("El numero debe ser positivo. ")
            continue
        break
    except ValueError:
        #Si se ingresa un valor no entero, se maneja la excepcion y se pide al usuario que ingrese un valor valido
        print("Entrada incorrecta, intente de nuevo. ")

#Inicio de la variable suma en cero
suma = 0

#Bucle para calcular la suma de la serie}


for i in range (1, + n+1):
#Se agrega el valor 1/i a la variable suma

    suma += 1/i
#Se imprime el resultado
print("El resultado de la serie es: ", suma)