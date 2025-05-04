from math import pi # para usar pi
import math # para usar las funciones de math
from datetime import date # para usar fechas 

# Ejercicios Pagina 35
def desafio_1():
    #1. Escribe un programa que pida al usuario el radio de un círculo y calcule el área.
    radio = int(input("Ingrese el radio: "))
    
    area = pi * radio**2
    
    print(f"El area es:{area}")

def desafio_2():
#2. Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

    celcius = int(input("Ingrese el valor a transformar de celsius a fahrenheith"))
    
    farenheith = (celcius* 9/5) + 32
    
    print(f"Se transformo con exito el valor en fahrenheith es: {farenheith}")

def desafio_3():
#3. Escribe un programa que pida al usuario los dos catetos de un triángulo rectángulo y calcule la hipotenusa.
    lado_uno= int(input("Ingrese el valor del cateto 1: "))
    lado_dos = int(input("Ingrese el valor del cateto 2: "))
    
    hipotenusa = lado_uno**2+lado_dos**2
    
    raiz= math.sqrt(hipotenusa)
    
    print(f"la hipotenusa es: {raiz}")
    
    print(hipotenusa)

def desafio_4():
    #4. Escribe un programa que pida al usuario su año de nacimiento, calcule su edad y genere un mensaje de saludo personalizado que incluya su nombre y la edad calculada.
    anio = int(input("Ingrese su año de nacimiento: "))
    
    anio_actual =date.today()
    edad = anio_actual.year - anio
    
    print(f"La edad de usted es: {edad}")

# Ejercicios de pagina 46

def desafio_5():
    #1. Escribe un programa que a partir de un número entero positivo, muestre por pantalla si es par o impar.
    verificar = True
    while verificar:
        numero = int(input("Ingrese un numero positivo"))
    
        if numero < 0:
         print("Error ingrese numero positivo")
         continue
        if numero % 2 ==0:
            print(f"El numero {numero} es par")
        else:
            print (f"El numero {numero} es impar")
            
        pregunta = input("¿Quiere ingresar otro numero? Si o No").lower()
        if pregunta == "no":
            print("Muchas gracias, hasta pronto.")
            verificar=False
            
def desafio_6():
    #2. Escribe un programa que a partir de un número entero positivo, muestre por pantalla si es primo o no.
    numero = int(input("Ingrese un numero:"))
   
    if numero <= 1:
        print(f"El número {numero} no es primo")
        return

    es_primo = True

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")
   
def desafio_7():
    #3. Escribe un programa que permita realizar la división de dos números siempre y cuando el denominador no sea 0.
    verificar = True
    while verificar:
        dividendo = int(input("Ingresa el dividendo: "))
        divisor = int(input("Ingresa el divisor: "))
    
        if divisor <=0:
         print("\nError no se puede dividir por 0")
         print("\n")
         continue
        
        division = dividendo / divisor
        
        print(f"El resultado es: {division}")
        
        pregunta = input("¿Quiere realizar otra division? Si o No: ").lower()
        
        if pregunta =="no":
            print("Muchas Gracias..")
            print("Hasta pronto")
            verificar =False
    
# Ejercicios pagina 49

def desafio_8():
    #1. Escribe un programa que solicite tres lados de un triángulo e indique si es equilátero, isósceles o escaleno.
    
    lado_1 = int(input("Ingrese el valor del lado 1: "))
    lado_2 = int(input("Ingrese el valor del lado 2: "))
    lado_3 = int(input("Ingrese el valor del lado 3: "))
    
    
    if lado_1 == lado_2 and lado_1 == lado_3 :
        print("El triangulo es equilatero") # tiene que tener 3 lados iguales 
    elif lado_1==lado_2 and lado_1 != lado_3 :
        print("El triangulo es Isosceles")  # tiene que tener 2 lados iguales
    else:
        print("el triangulo es escaleno")   # tiene que tener 3 lados desiguales
        
def desafio_9():
    #2. Escribe un programa que solicite al usuario que ingrese unacontraseña y confirme la contraseña. El programa debe verificar si
    #ambas contraseñas coinciden y no están vacías.
    verificacion = True
    while verificacion:
        contrasenia= "159753"
        usuario = input("Ingrese el usuario: ")
        password = input("Ingrese la contraseña: ")
    
        if usuario == "" or password == "":
         print("Error: usuario o contraseña estan vacio")
         continue
        
        if password == contrasenia  :
            print("Ingreso con exito")
            verificacion= False
        else :
            print("Contraseña equivocada")
            
def desafio_10():
    
#3. Escribe un programa que solicite al usuario el precio y la cantidadde un producto. Clasifique el producto como "caro" si el precio es
#mayor de $100 o si la cantidad es menor que 10 y el precio es mayor de $50. De lo contrario, clasifíquelo como "barato". Incluye
#condiciones para manejar valores falsos (0 o vacío).    
    
    producto = input("Ingrese Nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = int(input("Ingrese el precio: "))
    
    if precio > 100 and cantidad < 10 and precio > 50:
        print("el Precio es caro")
    else:
        print("el precio es barato")

def desafio_11():
    #Escribe un programa que solicite al usuario su nombre, edad y
    #número de teléfono. Verifica que ninguno de estos datos esté vacío
    #o sea un valor falso (por ejemplo, 0).
    while True:
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        telefono = input("Ingrese su numero de telefono: ")
        
    
        if nombre == "" or edad == 0 and telefono == "" or   len(telefono) !=10 :
            print("Ingrese valores validos")
            print (len(telefono))
            
            
            continue
        print(f"Su nombre es: {nombre}, su edad : {edad} y su telefonoe es: {telefono}")
        pregunta = input("Quiere ingresar otros datos ? SI O NO ").lower().strip()
        if pregunta == "no":
            print("Saliendo...")
            break
        
#Ejercicio pagina 52

def desafio_12():
   # 1. Escribe un programa que sume todos los números de una lista y luego responde ¿Qué tipo de variable utilizamos para resolver?

          numero_lista=[]

          suma = 0
          verificar = True
          while verificar:
            entrada = input("Ingresa un numero: ")
            if not entrada.isdigit(): # verificamos que sean numero los que ingresa 
                print("Error : Ingrese solo numeros mayor a 0")
                continue
           
            numero = int(entrada) #convertimos la entrada(String) a entero(int)
            suma +=numero          # Suma los numeros convertidos
            numero_lista.append(numero) #agregamos en la lista el numero ingresado
            
            pregunta = input("¿Quiere agregar otro numero? Si o No: " ).lower()
            if pregunta == "no":
                print("Saliendo del  programa")
                verificar = False
                
          print(f"la Sumatoria de la lista es: {suma}")
          print(f"Su lista es: {numero_lista}")
          
          # RESPUESTA: 
          # Se utilizan los siguientes tipos de variables:
          # - int: para almacenar los números ingresados y calcular la suma.
          # - list: para guardar todos los números ingresados.
          # - bool: para controlar el bucle while.
          # - str: para leer las entradas del usuario desde el teclado para evitar error de tipeo.

def desafio_13():
    #2. Escribe un programa que imprima el cuadrado de los números del 1 al 10.
    for i in range(1,11):
        
        cuadrado = i**2
        
        print(f"El Cuadrado de {i} es: {cuadrado}")
        
def desafio_14():
    #3. Escribe un programa que cuente los caracteres de una cadena de texto proporcionada por el usuario utilizando el for.
    cadena = input("Ingrese una frase: ")
    contador = 0
    
    for caracter in cadena:
        contador+=1
     
        
    print(f"el tamaño de la cadena es : {contador}")
    print(f"La cadena es: {cadena}")
    
def desafio_15():   
#4. Escribe un programa que cuente el número de vocales en una cadena de texto proporcionada por el usuario.    
    while True:
        cadena = input("Ingresa una frase: ")
    
        contador = 0
        for caracter in cadena:
            if caracter == "a" or caracter == "e" or caracter =="i" or caracter == "o" or caracter == "u":
             contador +=1
     
        print(f"La cadena tiene {contador} vocales") 
        pregunta = input("¿Quiere ingresar otra frase? Si o No: ").lower().strip
        if pregunta =="no":
            print("Saliendo del programa ")
            break
        
desafio_15()  
