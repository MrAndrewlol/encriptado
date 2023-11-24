

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

def relativeprime(b, a):
    while b:
        a, b = b, a % b
    return a




def Mconverter(lista):
    mensaje = ""
    for i in range(len(lista)):
        lista[i] = "{:02}".format(dicmod26[lista[i]])
        mensaje = mensaje+ str(lista[i])
    return mensaje

            

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
menecript = []
mensajencriptad = ""

#Inputs, Primero el mensaje pero no importa si
#lo pone en Mayusculas o Minusculas que siempre van a hacer Mayusculas

while(menu):
    menu = True
        
    print("Bienvenido al Encripación RSA")

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
            parte2 == False
            print("Tercer parte....")
            ##Esta parte vamos a codificar los bloques
            if((numerop*numeroq) > 25252525 ): #4 Digitos
                if((len(lista) % 4) == 0):
                    print("No se necesita Dummy variable")
                    b = 0
                    mensaje = 0
                    while(b <= (len(lista)/4)):
                        messegae = str(lista[mensaje]) + str(lista[mensaje+1]) + str(lista[mensaje+2]) + str(lista[mensaje+3])

                        menecript.append(int(messegae)^e) % (numerop*numeroq)
                        mensaje = mensaje + 4
                        b = b+1
                    
                    for i in menecript:
                        mensajencriptad = mensajencriptad + i + " "
                        
                else:
                    print("Se necesita un Dummy")
                    i = 0
                    while(i <= (len(lista) % 4)):
                        lista.append(0)
                        i =+ 1
                    b = 0
                    mensaje = 0
                    while(b <= (len(lista)/4)):
                        messegae = str(lista[mensaje]) + str(lista[mensaje+1]) + str(lista[mensaje+2]) + str(lista[mensaje+3])

                        menecript.append(int(messegae)^e) % (numerop*numeroq)
                        mensaje = mensaje + 4
                        b = b+1
                    
                    for i in menecript:
                        mensajencriptad = mensajencriptad + i + " "


                phi = (numerop-1)*(numeroq-1) #LLAVE QUE NO SE DEBE DE REVELAR

            if((numerop*numeroq) > 252525 and (numerop*numeroq) < 2525 ): #3 Digitos
                if((len(lista) % 3) == 0):
                    print("No se necesita Dummy variable")
                    b = 0
                    mensaje = 0
                    while(b <= ((len(lista)-1)/3)):
                        messegae1 = str(lista[mensaje]) + str(lista[mensaje+1]) + str(lista[mensaje+2]) 
                        messegae = (int(messegae1)^e) % (numerop*numeroq)
                        messegae = "{:06}".format(messegae)
                        menecript.append(messegae)
                        mensaje = mensaje + 3
                        b = b+1
                    
                    for i in menecript:
                        mensajencriptad = mensajencriptad + i
                    resultado = [mensajencriptad[i:i+4] for i in range(0, len(mensajencriptad), 4)]
                    mensajencriptad = ""
                    for i in resultado:
                        mensajencriptad = mensajencriptad + i + " "

                    print(mensajencriptad)
                        
                else:
                    print("Se necesita un Dummy")
                    i = 0
                    while(i <= (len(lista) % 3)):
                        lista.append("00")
                        i =+ 1
                    b = 0
                    mensaje = 0
                    while(b <= ((len(lista)-1)/3)):
                        messegae1 = ""
                        a = 0
                        while(a < 3):
                            messegae1 = messegae1 + str(lista[mensaje + a])
                            a = a+1

                        #messegae1 = str(lista[mensaje]) + str(lista[mensaje+1]) + str(lista[mensaje+2]) 
                        messegae = (int(messegae1)^e) % (numerop*numeroq)
                        messegae = "{:06}".format(messegae)
                        menecript.append(messegae)
                        mensaje = mensaje + 3
                        b = b+1
                    
                    for i in menecript:
                        mensajencriptad = mensajencriptad + i
                    resultado = [mensajencriptad[i:i+4] for i in range(0, len(mensajencriptad), 4)]
                    mensajencriptad = ""
                    for i in resultado:
                        mensajencriptad = mensajencriptad + i + " "

                    print(mensajencriptad)



                phi = (numerop-1)*(numeroq-1) #LLAVE QUE NO SE DEBE DE REVELAR
            
            if((numerop*numeroq) > 2525 and (numerop*numeroq) < 252525 ): #2 Digitos
                if((len(lista) % 2) == 0):
                    print("No se necesita Dummy variable")
                    b = 0
                    mensaje = 0
                    while(b <= (len(lista)/4)):
                        messegae = str(lista[mensaje]) + str(lista[mensaje+1]) 

                        menecript.append(int(messegae)^e) % (numerop*numeroq)
                        mensaje = mensaje + 2
                        b = b+1
                    
                    for i in menecript:
                        mensajencriptad = mensajencriptad + i + " "
                        
                else:
                    print("Se necesita un Dummy")
                    i = 0
                    while(i <= (len(lista) % 2)):
                        lista.append(0)
                        i =+ 1
                    b = 0
                    mensaje = 0
                    while(b <= (len(lista)/2)):
                        messegae = str(lista[mensaje]) + str(lista[mensaje+1])

                        menecript.append(int(messegae)^e) % (numerop*numeroq)
                        mensaje = mensaje + 2
                        b = b+1
                    
                    for i in menecript:
                        mensajencriptad = mensajencriptad + i + " "


                phi = (numerop-1)*(numeroq-1) #LLAVE QUE NO SE DEBE DE REVELAR

            if((numerop*numeroq) > 25 ): #1 digito
                if((len(lista) % 1) == 0):
                    print("No se necesita Dummy variable")
                    b = 0
                    mensaje = 0
                    while(b <= (len(lista)/1)):
                        messegae = str(lista[mensaje]) 

                        menecript.append(int(messegae)^e) % (numerop*numeroq)
                        mensaje = mensaje + 1
                        b = b+1
                    
                    for i in menecript:
                        mensajencriptad = mensajencriptad + i + " " #Arreglar porque si no aparece como 025 y son bloques de 4 
                        
                else:
                    print("Se necesita un Dummy")
                    i = 0
                    while(i <= (len(lista) % 1)):
                        lista.append(0)
                        i =+ 1
                    b = 0
                    mensaje = 0
                    while(b <= (len(lista)/4)):
                        messegae = str(lista[mensaje]) + str(lista[mensaje+1]) + str(lista[mensaje+2]) + str(lista[mensaje+3])

                        menecript.append(int(messegae)^e) % (numerop*numeroq)
                        mensaje = mensaje + 4
                        b = b+1
                    
                    for i in menecript:
                        mensajencriptad = mensajencriptad + i + " "


                phi = (numerop-1)*(numeroq-1) #LLAVE QUE NO SE DEBE DE REVELAR
        else:
            print("Numero ingresado no es primo relativo")

        


