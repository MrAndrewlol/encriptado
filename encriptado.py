
##PROGRAMA REALIZADO POR

#GUSTAVO CRUZ 22779
#ANDRE JO 22199



#INPUTS

#𝑀, 𝑝, 𝑞 & 𝑒


#Bloques de 4 digitos
#Funciones

# Ansi para impresión de pantalla con colores en terminal
CLEAR = "\033[2J"
BLUE = "\033[94m"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

import time
# Funcion que imprime lento
def slowprint(text):
    for char in text:
        print(char, end ='', flush=True)
        time.sleep(0.1)
# Funcion para verificar si un numero es primo
def is_prime(n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Funcion para encontrar numeros primos de 2 a raiz cuadradada de n
def get_primes(n0):
    primes = []
    for num in range(2, n0 +1):
        if is_prime(num):
            primes.append(num)
    return primes

# Funcion que encuentra los numeros primos p y q
def findpq(n):
    primes = get_primes(n)
    
    for p in primes:
        if n % p == 0:
            q = n // p
            return p,q
    return None, None

# Funcion que implementa el algoritmo extendido de euclides, retorna mcd, y coeficientes x, y
def euclides(a,b):
    if a == 0:
        return(b, 0, 1)
    else:
        mcd, x, y = euclides(b%a, a)
    return (mcd, y -(b//a) *x, x)

# Funcion para calcular el modulo inverso multiplicativo
def modinverse(a,m):
    mcd, x, y = euclides(a,m)
    if mcd != 1:
        slowprint(f"{RED} ERROR... NO HAY INVERSO MULTIPLICATIVO ...")
    else:
        return x%m

# Funcion para calcular la llave privada    
def privKey(e, p, q):
    phi = (p-1)*(q-1)
    return modinverse(e, phi) 

def decrypt(C, d, n):
    M = ""
    for i in range(0, len(C), 4):
        bloque = C[i:i + 4]
        num = int(bloque)
        dec_num = pow(num, d, n)
        letra1 = chr((dec_num // 100) + ord('A'))
        letra2 = chr((dec_num % 100) + ord('A'))
        M += letra1 + letra2
    return M


def main():
    #slowprint(f"{CLEAR}\t\t{BLUE} Bienvenido al programa de codificación y decodificación RSA{RESET}\n\n")
    C = input(f"{GREEN}Ingrese el mensaje cifrado, en bloques de dos letras: ").replace(" ", "")
    e = int(input("Ingrese el valor de e: "))
    n = int(input("Ingrese el valor de n: "))
    print(CLEAR)
    #slowprint(f"{BLUE}...Calculando p y q...")
    p,q = findpq(n)    
    #slowprint(f"\n{GREEN}Encontrado p:{p} q: {q}")
    #slowprint(f"\n{BLUE}Calculando llave privada... {RESET}")
    d = privKey(e,p,q)
    #slowprint(f"\n{CLEAR}{GREEN}Llave privada d: {d}{RESET}")
    M = decrypt(C,d,n)
    print(f"\n\t{RED} El mensaje descifrado es: {M}")







def prime(numero):
    statement = True
    if (numero > 1):
        for i in range(2, numero):
            if(numero % i ) == 0:
                statement = False
        
    return statement

def relativeprime(b, a):
    while b:
        a, b = b, a % b
    return a


def obtenernum(pyq):
    statement = False
    maxnum = ""
    while(statement == False):
        maxnum = maxnum + "25"
        if(pyq > int(maxnum) and pyq < int(maxnum + "25") ): #31 >= 25 31<=2525
            statement = True
    return maxnum

def contador(pyq):
    statement = False
    maxnum = ""
    numeroglobal = 0
    while(statement == False):
        maxnum = maxnum + "25"
        numeroglobal = numeroglobal + 2
        if(pyq > int(maxnum) and pyq < int(maxnum + "25") ): #31 >= 25 31<=2525
            statement = True
    return numeroglobal


def Mconverter(lista):
    mensaje = ""
    for i in range(len(lista)):
        lista[i] = "{:02}".format(dicmod26[lista[i]])
        mensaje = mensaje+ str(lista[i])
    return mensaje

            

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
menecript = []
mensajencriptad = ""
numeroglobal = 0


#Inputs, Primero el mensaje pero no importa si
#lo pone en Mayusculas o Minusculas que siempre van a hacer Mayusculas

while(menu):
    menu = True
    parte2 = True
        
    print("Bienvenido al Encripación RSA")

    print("\n Por favor elegir las siguientes opciones")
    print("\n1.Encriptación\n2.Desencriptación")

    decision = input( "1 para encriptar y 2 para desencriptar\n")

    if(decision == "1"):
            
        Mensaje = input("Porfavor Escribir el mensaje que desea Encriptar\n")
        Mensaje = Mensaje.upper()
        Mensaje = Mensaje.replace(" ", "")

        lista = list(Mensaje)
        mensajemod = Mconverter(lista)


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
            e = round(int(input("Por favor ingresar un numero entero y que sea primo relativo a " + str(numerop*numeroq) + "\n")))
            ##Basicamente si p y q son menores a 2525 entonces da eso por ejemplo 3551 por lo tanto son de dos caracteres y ahi lo separas en 4 bloques
            print()
            if(relativeprime(e,(numerop*numeroq)) == 1): 
                parte2 = False
                print("Tercer parte....")
                ##Esta parte vamos a codificar los bloques
                

                if((numerop*numeroq) > int(obtenernum(numerop*numeroq)) ): #3 Digitos
                    mensajencriptad = ""
                    numeroglobal = contador((numerop*numeroq))
                    if((len(lista) % int(numeroglobal)) == 0):
                        print("No se necesita Dummy variable")
                        b = 0
                        mensaje = 0
                        while(b <= ((len(lista)-1)/(int(numeroglobal)/2))):
                            messegae1 = ""
                            a = 0
                            while(a < (int(numeroglobal)/2)):
                                messegae1 = messegae1 + str(lista[mensaje + a])
                                a = a+1

                            #messegae1 = str(lista[mensaje]) + str(lista[mensaje+1]) + str(lista[mensaje+2]) 
                            if(int(numeroglobal) <= 10):
                                numeroglobal = "{:02}".format(numeroglobal)

                            numberformat = "{:" + str(numeroglobal) +"}"
                            messegae = int(int(messegae1)**e) 
                            messegae = messegae % (numerop*numeroq)
                            messegae = numberformat.format(messegae)
                            menecript.append(messegae)
                            mensaje = round(mensaje + (int(numeroglobal)/2))
                            b = b+1
                        
                        for i in menecript:
                            mensajencriptad = mensajencriptad + i
                        resultado = [mensajencriptad[i:i+4] for i in range(0, len(mensajencriptad), 4)]
                        mensajencriptad = ""
                        for i in resultado:
                            mensajencriptad = mensajencriptad + i + " "

                        print("El mensaje encriptado es: " +mensajencriptad)
                        print("LLave publica es (" + str(e) + "," +  str(numerop*numeroq) + ")" )
                        menu = False


                        phi = (numerop-1)*(numeroq-1) #LLAVE QUE NO SE DEBE DE REVELAR
                            
                    else:
                        print("Se necesita un Dummy")
                        i = 0
                        while(i <= (len(lista) % int(numeroglobal))):
                            lista.append("00")
                            i =+ 1
                        b = 0
                        mensaje = 0
                        while(b <= ((len(lista)-1)/(int(numeroglobal)/2))):
                            messegae1 = ""
                            a = 0
                            while(a < (int(numeroglobal)/2)):
                                messegae1 = messegae1 + str(lista[mensaje + a])
                                a = a+1

                            #messegae1 = str(lista[mensaje]) + str(lista[mensaje+1]) + str(lista[mensaje+2]) 
                            if(int(numeroglobal) <= 10):
                                numeroglobal = "{:02}".format(numeroglobal)

                            numberformat = "{:" + str(numeroglobal) +"}"
                            messegae = int(int(messegae1)**e) 
                            messegae = messegae % (numerop*numeroq)
                            messegae = numberformat.format(messegae)
                            menecript.append(messegae)
                            mensaje = round(mensaje + (int(numeroglobal)/2))
                            b = b+1
                        
                        for i in menecript:
                            mensajencriptad = mensajencriptad + i
                        resultado = [mensajencriptad[i:i+4] for i in range(0, len(mensajencriptad), 4)]
                        mensajencriptad = ""
                        for i in resultado:
                            mensajencriptad = mensajencriptad + i + " "

                        print("El mensaje encriptado es: " +mensajencriptad)
                        print("LLave publica es (" + str(e) + "," +  str(numerop*numeroq) + ")" )
                        menu = False


                    phi = (numerop-1)*(numeroq-1) #LLAVE QUE NO SE DEBE DE REVELAR
            else:
                print("Numero ingresado no es primo relativo")

    if(decision == "2"):
        main()
        menu = False


            


