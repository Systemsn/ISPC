
import modulo



while True:
    
    print(":::::Menu:::::")
    print("Opcion 1 : Agregar Dispositivo")
    print("Opcion 2 : Busar Dispositivo")
    print("Opcion 3 : Mostrar Dispositivo")
    print("Opcion 4 : Eliminar Dispostivos")
    opcion  = int(input("Ingrese la opcion: "))
    match opcion:
    
        case 1 : 
             # nombre,marca,modelo,tipo,color,consumo_energia,voltaje
             
             nombre_dispositivo = input("Ingrese el nombre del Dispositivo: ") # 
             marca = input("Ingrese la marca del dispositivo: ")
             modelo = input("Ingrese el modelo: ")
             tipo = input("Ingrese el tipo: ")
             color = input("Ingrese el color : ")
             consumo_energia = int(input("ingrese el consumo de energia del dispositivo: "))
             voltaje = int(input("Ingrese el voltaje del Electrodomostico: "))
             modulo.agregar(nombre_dispositivo,marca,modelo,tipo,color,consumo_energia,voltaje)
             
             pass
        case 2 : 
              busqueda = input("Ingrese el nombre del dispositivo que desea encontrar: ")

              
              print(modulo.buscar(busqueda))
              pass
        
        case 3 : 
            print(modulo.mostrar())
            pass
    
        case 4 :
            busqueda = input("Ingrese el dispositivo que desea eliminar: ")
             
            modulo.eliminar(busqueda)
            pass 
            
        case _:
            print("Error : ingreso una opcion no valida ")
            continue
        
    pregunta = input("Quiere ingresar otra opcion?: ").lower().strip()
    if pregunta == "no":
        break
        
    