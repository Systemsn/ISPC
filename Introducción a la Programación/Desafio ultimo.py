#1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número conlos dígitos en orden inverso:

def Desafio_1():
    numero = int(input("Ingrese un numero de tres digitos: "))
    verificar= True
    while verificar:
        if numero <100 :
            print("Error ingrese un numero de 3 digitos")
            continue
    
        numero_invertido=int(str(numero)[::-1])
        
        print(numero_invertido)
        
        pregunta = input("¿Quiere ingresar otro numero? Si o No ").lower()
        
        
Desafio_1()
            
            
    
    