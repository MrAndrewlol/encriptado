

#INPUTS

#𝑀, 𝑝, 𝑞 & 𝑒


#Bloques de 4 digitos


#Funciones


def prime(numero):
    statement = True
    if (numero > 1):
        for i in range(2, numero):
            if(numero % i ) == 0:
                statement = False
        
    return statement


def MCD(e, phi):
    print("")

            

if(prime(11) == True):
    print("SIUUU")
else:
    print("no pasa nada")


        

#Funcion para poder saber si es primo o no


#Encriptacion RSA

#Diccionario de modulo 26
dicmod26 = { "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, 
             "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
             "K": 10, "L": 11, "M": 12, "N": 13, "O": 14,
             "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
             "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24,
             "Z": 25
}

menu = True
parte2 = True

#Inputs, Primero el mensaje pero no importa si
#lo pone en Mayusculas o Minusculas que siempre van a hacer Mayusculas

while(menu):
        
    print("Bienvenido al Encripación RSA")

    Mensaje = input("Porfavor Escribir el mensaje que desea Encriptar\n")
    Mensaje = Mensaje.upper()

    numerop = int(input("Escibir su primer numero primo\n"))

    numeroq = int(input("Escribir su segundo numero primo\n"))

    if(prime(numerop) == False):
        print("El primer numero no es primo")
        parte2 = False  
        
    if(prime(numeroq) == False):
        print("El Segundo numero no es primo")
        parte2 = False
    

    while(parte2 == True):
        print("Segunda parte...")
        e = round(int(input("Por favor ingresar un numero entero y que sea primo relativo a " + (numerop*numeroq))))
    
        if(prime(e) == True):
            parte2 == False
            print("Tercer parte....")
            ##Esta parte vamos a codificar los bloques
            if((numerop*numeroq) > 25252525 ):

                phi = (numerop-1)*(numeroq-1) #LLAVE QUE NO SE DEBE DE REVELAR
        else:
            print("Numero ingresado no es primo relativo")

        


