
import modulo # importamos todos los metodos del modulo.py

if __name__ == "__main__":
    
 

    while True: # Creamos un funcion repetitiva para que se pueda usar nuevamente el menu 
    # Creamos el menu donde damos opciones para el usuario. 
        print("\n::::::::::::::::::::::::::::::")
        print("::      PANEL PRINCIPAL     ::")
        print("::::::::::::::::::::::::::::::")
        
        print("Opcion 1 : Panel Dispositivos")
        print("Opcion 2 : Panel de Iluminacion")
        print("Opcion 3 : Calefacion")
        print("Opcion 4 : Salir del programa")
        print("Opcion 5 : Gestor de ubicacion")
        
        opcion  = input("Ingrese la opcion: ") # Guardamos la opcion del usuario 
        match opcion:# ejecuta la opcion del usuario
    
                case "1" : 
                    while True : 
                        # Creamos un panel para dispositivos 
                        print("\n::::::::::::::::::::::::::::::")
                        print("::    PANEL DISPOSITIVOS    ::")
                        print("::::::::::::::::::::::::::::::")
                        print("\nOpcion 1 : Agregar nuevo dispositivo")
                        print("Opcion 2 : Buscar dispositivo")
                        print("Opcion 3 : Mostrar todo los dispositivos")
                        print("Opcion 4 : Eliminar Dispositivo")
                        print("Opcion 5 : Volver al menu anterior")
                        opcion = input("Ingrese la opcion: ")
                        match opcion:
                            
                            case "1": 
                                
                                
                                
                                # Ingresamos los datos para pasarlos como parametro a las funciones 
                                while modulo.Validar_habitaciones():
                
                                    nombre_dispositivo = input("\nIngrese el nombre del Dispositivo: ").lower()  
                    
                                    marca = input("Ingrese la marca del dispositivo: ").lower()
                    
                                    modelo = input("Ingrese el modelo: ").lower()
                                
                                    print("\n::::::::::::::::::::::::::::::")
                                    print("::  TIPOS DE DISPOSITIVOS   ::")
                                    print("::::::::::::::::::::::::::::::")
                                    print("1. Electrodomesticos")
                                    print("2. Iluminacion")
                                    print("3. Calefacion")
                                    print("4. Seguridad")
                               
                                    tipo = int(input("Ingrese el tipo: "))
                    
                                    color = input("Ingrese el color : ").lower()
                                
                                    temperatura = 0
                                
                                    tiempo = 0
                    
                                    consumo_energia = int(input("ingrese el consumo de energia del dispositivo: "))
                    
                                    voltaje = int(input("Ingrese el voltaje del Electrodomostico: "))
                                    
                                    modulo.Mostrar_Habitaciones()
                                
                                    ubicacion = input("Ingrese la ubicacion donde se colocara: ").lower()
                                    estado = 0 
                    
                                    modulo.agregar(nombre_dispositivo,marca,modelo,tipo,color,temperatura,tiempo,consumo_energia,voltaje,ubicacion,estado) # Aqui agregamos los datos a la funcion agregar.
                                    pregunta = input("Quieres Ingresar otro dispositivo? SI o NO").lower().strip()
                                    
                                    if pregunta == "no":
                                        break
                                    

                            case "2" : 

                                busqueda = input("\nIngrese el nombre del dispositivo que desea encontrar: ") # ingresamos el dispositivo a buscar
                                print("\n::::::::::::::::::::::::::::::")
                                print("::  Dispositivo Encontrado  ::")
                                print("::::::::::::::::::::::::::::::")
              
                                print(modulo.buscar(busqueda))
                                pass
        
                            case "3" : 
                                print("\n::::::::::::::::::::::::::::::")
                                print("::  Todos los dispositivos  ::")
                                print("::::::::::::::::::::::::::::::")
                                modulo.mostrar()# aqui imprimimos la funcion donde se muestra la listas y sus datos
                 
    
                            case "4" :
                                
                                
                                busqueda = input("\nIngrese el dispositivo que desea eliminar: ") # ingresamos el dispositivo a eliminar 
                                print("\n::::::::::::::::::::::::::::::")
                                print("::  Dispositivo Eliminado   ::")
                                print("::::::::::::::::::::::::::::::")
             
                                print(modulo.eliminar(busqueda)) # Aqui imprimimos y llamamos a la funcion para que elimine el dispositivo
                                pass 
                                
                            case "5": 
                                break
                            case _:
                                # Este es un caso por default donde si no ingresan correctamente las opciones que indica el menu.
                                print("Error : ingreso una opcion no valida ") # imprimimos el error 
                                continue
        
                case "2" :  
                    while True:
                        
                        print("\n::::::::::::::::::::::::::::::")
                        print("::   PANEL DE ILUMINACION   ::")
                        print("::::::::::::::::::::::::::::::")

                        print("Opcion 1 : Prender / Apagar luces")
                        print("Opcion 2 : Mostrar Prendio/ Apagado / todo")
                        print("Opcion 3 : Configurar Modo noche")
                        print("Opcion 4 : Configurar Modo Ahorro de Energia")
                        print("Opcion 5 : Volver al menu principal")
                        opcion = input("Ingrese una opcion: ")
                        match opcion :
                            case "1": 
                                print("\n:::::::::::::::::::::::::::::::::")
                                print(":: PANEL DE PRENDIDO Y APAGADO ::")
                                print(":::::::::::::::::::::::::::::::::")
                                print("1.Prender luces")
                                print("2.Apagar luces")
                                opcion = int(input("Ingrese una opcion: "))
                                
                                
                                if opcion ==1 :
                                    busqueda = input(" Que habitacion quiere prender las luces?: ")
                                    
                                    modulo.prender_luces(busqueda)
                                elif opcion ==2:
                                    busqueda = input(" Que habitacion quiere pagar las luces?: ")
                                    modulo.apagar_luces()
                            case "2":
                                
                                print("\n:::::::::::::::::::::::::")
                                print(":: PANEL MOSTRAR LUCES ::")
                                print(":::::::::::::::::::::::::")
                                print("1.Mostrar habitaciones apagadas")
                                print("2.Mostrar habitaciones prendidas")
                                print("3.Mostrar todas las habitaciones")
                                print("4.Volver al menu anterior")
                                opcion = input("Ingrese una opcion: ")
                                
                                match opcion:
                                    case "1" : 
                                        print("\n:::::::::::::::::::")
                                        print(":: LUCES APAGADA ::")
                                        print(":::::::::::::::::::")
                                        modulo.mostrar_luces_apagado()
                                        
                                        pass
                                    
                                    case "2":
                                        print("\n:::::::::::::::::::::")
                                        print(":: LUCES PRENDIDAS ::")
                                        print(":::::::::::::::::::::")
                                        modulo.mostrar_luces_prendidos()
                                        
                                        pass
                                    
                                    case "3": 
                                        print("\n::::::::::::::::::::::::")
                                        print(":: TODAS HABITACIONES ::")
                                        print("::::::::::::::::::::::::")
                                        modulo.mostrar_luces()
                                        
                                        pass
                                    
                                    case "4": 
                                    
                                        break
                                    case _:
                                        print("Error : Ingreso una opcion no valida")
                                    
                            case "3": 
                                print("\n:::::::::::::::::::::::::::::")
                                print(":: CONFIGURACION MODO NOCHE ::")
                                print("::::::::::::::::::::::::::::::")
                                        
                                hora_prendido= int(input("Ingrese la hora a que se prenderan las luces: "))
                                minuto_prendio = int(input("Ingrese los minutos: "))
                                while True:
                                            
                                        
                                    ubicacion_exterior = input("Ingrese la ubicacion de la casa: ")
    
                                    modulo.luces_modo_Noche(hora_prendido,minuto_prendio,ubicacion_exterior)
                                            
                                    pregunta = input("Quiere Ingresar otra ubicacion de la casa? SI O NO").lower().strip()
                                    if pregunta == "no":
                                        break
                                       
                                    
                            case "4":
                                print("\n::::::::::::::::::::::::::::::")
                                print(":: CONFIGURACION MODO AHORRO ::")
                                print(":::::::::::::::::::::::::::::::")
                                        
                                hora_apagado= int(input("Ingrese la hora a que se apagaran las luces: "))
                                minuto_apagado = int(input("Ingrese los minutos: "))
                                while True:
                                            
                                        
                                    ubicacion_exterior = input("Ingrese la ubicacion de la casa: ").lower()
    
                                    modulo.luces_modo_Noche(hora_apagado,minuto_apagado,ubicacion_exterior)
                                            
                                    pregunta = input("\nQuiere Ingresar otra ubicacion de la casa? SI O NO: ").lower().strip()
                                    if pregunta == "no":
                                        break
                            case "5": 
                                break
                
                case "3":
                    print("\n::::::::::::::::::::::::::")
                    print("::  PANEL DE CALEFACCION  ::")
                    print("::::::::::::::::::::::::::::")
                    
            
                    temperatura_hoy = int(input("Ingrese la temepratura de hoy : "))
                    modulo.calefacion_ambiente(temperatura_hoy)
                    
                case "4":
                    break
                
                
                case "5":
                    print("\n::::::::::::::::::::::")
                    print(":: Panel Ubicacion  ::")
                    print("::::::::::::::::::::::")
                    print("Opcion 1: Crear ubicacion")
                    print("Opcion 2 : Mostrar Ubicacion")
                    print("Opcion 3 : eliminar ubicacion")
                    
                    opcion = input("Ingrese una Opcion: ")
                    
                    match opcion:
                        
                        case "1": 
                            ubicacion = input("Ingrese una ubicacion: ")
                            modulo.Crear_ubicacion(ubicacion)
                            pass
                        case "2": 
                            modulo.Mostrar_Habitaciones()
                            pass
                    
                        case "3":
                            
                            busqueda = input("Ingrese la ubicacion a eliminar: ")
                            
                            modulo.eliminar_ubicacion(busqueda)
                            
                  
                    
                        
                    
                    
                    
                    
                    
                    
                case _:
                    print("ERROR : Ingreso una opcion incorrecta")
            
                    
        
        
     
    