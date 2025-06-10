
import modulo # importamos todos los metodos del modulo.py

if __name__ == "__main__":
    
    contador = 0

    while True: # Creamos un funcion repetitiva para que se pueda usar nuevamente el menu 
    # Creamos el menu donde damos opciones para el usuario. 
       
        print("\n::::::::::::::::::::::::::::::")
        print("::      PANEL PRINCIPAL     ::")
        print("::::::::::::::::::::::::::::::")
        print("opcion 1 - Iniciar Sesion")
        print("opcion 2 - Registrar Usuario")
        opcion = input("Ingrese una opcion: ")


        if not opcion.isdigit():
          print("Error Ingrese digitos numericos ")
          continue
        else:
            convertir_a_entero = int(opcion)
            
        match convertir_a_entero:
            case 1 : 
                print("\n:::::::::::::::::::::")
                print("::  Iniciar Secion  ::")
                print(":::::::::::::::::::::")
                    
                usuario_validar = input("ingrese su usuario: ")
                contrasenia_validar = input("Ingrese su contraseña: ")
                modulo.verificar_contraseña(usuario_validar,contrasenia_validar)
                        
                if modulo.verificar_contraseña(usuario_validar,contrasenia_validar) == True and modulo.verificar_rol(usuario_validar) == True :
                    opcion = 2
                elif modulo.verificar_contraseña(usuario_validar,contrasenia_validar) == True and modulo.verificar_rol(usuario_validar) == False:
                    opcion = 1 
                else :
                    print("Usuario o Contraseña incorrecta")
                    continue
                        

                match opcion:
                        
                    case 1:  
                        while True:
                            
                            print("\n:::::::::::::::::::::")
                            print("::  Menu Usuario   ::")
                            print(":::::::::::::::::::::")
                            print("opcion 1 : Consultar Datos ")
                            print("opcion 2 : Prender o Apagar Luces")
                            print ("opcion 3 : Consultar Dispositivos")
                            print ("opcion 4 : Prender calefacion")
                            print ("opcion 5 : Volver al panel anterior")
                            opcion_menu = input("Ingrese una opcion: ")
                            if not opcion_menu.isdigit():
                                print("Error ingrese digitos numerico")
                                continue
                            else :
                                convertir = int(opcion_menu)
                                    
                            match convertir :
                                   
                                case 1 : 
                                    print("\n:::::::::::::::::::::::::::::")
                                    print("::  Panel Consultar Datos  ::")
                                    print(":::::::::::::::::::::::::::::")
                                    consulta = input("ingrese el usuario a consultar: ")
                                    modulo.consutar_usuario(consulta)
                                    
                                case 2:
                                    while True: 
                                        
                                        print("\n:::::::::::::::::::::::::")
                                        print("::  Panel Iluminacion  ::")
                                        print(":::::::::::::::::::::::::")
                                        print("\nOpcion 1 : Prender luceso o Apagar Luces ")
                                        print("Opcion 2 : Mostrar Todas las luces")
                                        print("Opcion 3 :  configurar Horario")
                                        print ("Opcion 4 :  Volver al menu anterior ")
                                        opcion_activar = input("ingrese una opcion")
                                        
                                        if not opcion_activar.isdigit():
                                           print("Error Ingrese digitos numericos")
                                           continue
                                        else:
                                            convertir_a_entero_3 = int(opcion_activar)
                                            
                                        match convertir_a_entero_3 :
                                            case 1: 
                                                print("\n:::::::::::::::::::::::::::::::::")
                                                print(":: PANEL DE PRENDIDO Y APAGADO ::")
                                                print(":::::::::::::::::::::::::::::::::")
                                                print("1.Prender luces")
                                                print("2.Apagar luces")
                                                opcion_lus = int(input("Ingrese una opcion: "))
                                
                                
                                                if opcion_lus ==1 :
                                                    busqueda = input(" Que habitacion quiere prender las luces?: ")
                                    
                                                    modulo.prender_luces(busqueda)
                                                elif opcion_lus ==2:
                                                    busqueda = input(" Que habitacion quiere pagar las luces?: ")
                                                    modulo.apagar_luces()
                                            case 2 : 
                                                print("\n::::::::::::::::::::::::::::::")
                                                print(":: Mostrar Todas las luces  ::")
                                                print("::::::::::::::::::::::::::::::")
                                                modulo.mostrar_luces()
                    
                                case 3:
                                    while True: 
                                        
                                        print("\n::::::::::::::::::::::::::::::")
                                        print("::    PANEL DISPOSITIVOS    ::")
                                        print("::::::::::::::::::::::::::::::")
                                        print("Opcion 1 : Buscar Dispositivos")
                                        print ("Opcion 2 : Mostrar todos los Dispositivos")
                                        print ("Opcion 3 : Volver al menu anterior")
                                        opcion_dispositivo = input("Ingrese una opcion: ")
                                    
                                        if not opcion_dispositivo.isdigit():
                                            print("Error : Ingrese Digitos numericos.")
                                            continue
                                        else :
                                            convetir_dispositivo = int(opcion_dispositivo)
                                        
                                        match convetir_dispositivo:
                                        
                                            case 1: 
                                                busqueda = input("Ingrese el Dispositivo a cosultar: ")
                                            
                                                modulo.buscar(busqueda)
                                                
                                            case 2 : 
                                                print("\n::::::::::::::::::::::::::::::")
                                                print("::    Dispositivos Encontrdos    ::")
                                                print("::::::::::::::::::::::::::::::")
                                                
                                                modulo.mostrar()
                                            case 3 : 
                                                break  
                                case 4 : 
                                    print("\n::::::::::::::::::::::::::")
                                    print("::  PANEL DE CALEFACCION  ::")
                                    print("::::::::::::::::::::::::::::")
                                     

                                    modulo.validar_calefacion()
                                    
                                    if modulo.validar_calefacion() == False:
                                        print("No hay dispositivos cargados")
                                    elif modulo.validar_calefacion() == True : 
                                    
                                        temperatura_hoy = int(input("Ingrese la temepratura de hoy : "))
                                        modulo.calefacion_ambiente(temperatura_hoy)
                                    
                                        
                                case 5: 
                                    break
                                    
                                case _: 
                                    print("Ingreso una opcion incorrecta")
                            
                            
                    case 2: 
                        while True:
                            print("\n:::::::::::::::::::::")
                            print("::  Menu Administrador  ::")
                            print(":::::::::::::::::::::")
                            print("Opcion 1 : Panel Dispositivos")
                            print("Opcion 2 : Panel de Iluminacion")
                            print("Opcion 3 : Calefacion")
                            print("Opcion 4 : Gestor de ubicacion")
                            print("Opcion 5 : Gestor de usuario")
                            print("Opcion 6 : Salir del programa")
        
                            opcion_admin  = input("Ingrese la opcion: ") # Guardamos la opcion del usuario 
                        
                            if not opcion_admin.isdigit():
                                print("Ingrese digitos numericos")
                            else :
                                convertir_numero = int(opcion_admin) # tranformamos la opcion en entero
                            
                            match convertir_numero: # ejecuta la opcion del usuario
    
                                case 1 : 
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

                                        if not opcion.isdigit():
                                            print("Ingrese digitos numericos")
                                            continue
                                        else : 
                                            convertir = int(opcion)
                                        
                                        match convertir:
                            
                                            case 1: 
        
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
                    
                                                    consumo_energia = int(input("Ingrese la potencia del dispositivo en vatios (W), por ejemplo 1500: "))
                    
                                                    voltaje = int(input("Ingrese el voltaje del electrodoméstico (V), por ejemplo 110 o 220: "))
                                                    
                                                    print("\n INGRESE LA UBICACIONES CARGADAS")
                                    
                                                    modulo.Mostrar_Habitaciones()
                                
                                                    ubicacion = input("Ingrese la ubicacion donde se colocara: ").lower()
                                                    estado = 0 
                    
                                                    modulo.agregar(nombre_dispositivo,marca,modelo,tipo,color,temperatura,tiempo,consumo_energia,voltaje,ubicacion,estado) # Aqui agregamos los datos a la funcion agregar.
                                                    pregunta = input("Quieres Ingresar otro dispositivo? SI o NO: ").lower().strip()
                                    
                                                    if pregunta == "no":
                                                        break
                                    

                                            case 2 : 
                                                
                                                print("\n::::::::::::::::::::::::::::::")
                                                print("::  Dispositivo Encontrado  ::")
                                                print("::::::::::::::::::::::::::::::")

                                                busqueda = input("\nIngrese el nombre del dispositivo que desea encontrar: ") # ingresamos el dispositivo a buscar
                                                
            
                                                modulo.buscar(busqueda)
                                                pass
        
                                            case 3 : 
                                                print("\n::::::::::::::::::::::::::::::")
                                                print("::  Todos los dispositivos  ::")
                                                print("::::::::::::::::::::::::::::::")
                                                modulo.mostrar()# aqui imprimimos la funcion donde se muestra la listas y sus datos
                 
    
                                            case 4 :
                                
                                                busqueda = input("\nIngrese el dispositivo que desea eliminar: ") # ingresamos el dispositivo a eliminar 
                                                print("\n::::::::::::::::::::::::::::::")
                                                print("::  Dispositivo Eliminado   ::")
                                                print("::::::::::::::::::::::::::::::")
             
                                                print(modulo.eliminar(busqueda)) # Aqui imprimimos y llamamos a la funcion para que elimine el dispositivo
                                                pass 
                                
                                            case 5: 
                                                break
                                            case _:
                                            # Este es un caso por default donde si no ingresan correctamente las opciones que indica el menu.
                                                print("Error : ingreso una opcion no valida ") # imprimimos el error 
                                                continue
        
                                case 2 :  
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
                                        
                                        if not opcion.isdigit():
                                            print("Error Ingrese Digitos numericos")
                                            continue
                                        else :
                                            convertir= int(opcion)
                                        
                                        match convertir :
                                            case 1: 
                                                print("\n:::::::::::::::::::::::::::::::::")
                                                print(":: PANEL DE PRENDIDO Y APAGADO ::")
                                                print(":::::::::::::::::::::::::::::::::")
                                                print("1.Prender luces")
                                                print("2.Apagar luces")
                                                opcion_prendido = input("Ingrese una opcion: ")
                                                
                                                if not opcion_prendido.isdigit():
                                                    print("Digite un valor numerico")
                                                    continue
                                                else : 
                                                    convertir_prendio_a_entero = int(opcion_prendido)
                                        

                                                match convertir_prendio_a_entero:
                                                    case 1 : 
                                                   
                                                        busqueda = input(" Que habitacion quiere prender las luces?: ")
                                    
                                                        modulo.prender_luces(busqueda)
                                                    case 2: 
                                                        busqueda = input(" Que habitacion quiere pagar las luces?: ")
                                                        modulo.apagar_luces()
                                            case 2:
                                
                                                print("\n:::::::::::::::::::::::::")
                                                print(":: PANEL MOSTRAR LUCES ::")
                                                print(":::::::::::::::::::::::::")
                                                print("1.Mostrar habitaciones apagadas")
                                                print("2.Mostrar habitaciones prendidas")
                                                print("3.Mostrar todas las habitaciones")
                                                print("4.Volver al menu anterior")
                                                opcion_mostrar_luces = input("Ingrese una opcion: ")
                                                
                                                if not opcion.isdigit():
                                                    print("Error Ingrese Digitos numericos")
                                                    continue
                                                else :
                                                    convertir_mostar_luces= int(opcion_mostrar_luces)
                                
                                                match convertir_mostar_luces:
                                                    case 1 : 
                                                        print("\n:::::::::::::::::::")
                                                        print(":: LUCES APAGADA ::")
                                                        print(":::::::::::::::::::")
                                                        modulo.mostrar_luces_apagado()
                                        
                                                        pass
                                    
                                                    case 2:
                                                        print("\n:::::::::::::::::::::")
                                                        print(":: LUCES PRENDIDAS ::")
                                                        print(":::::::::::::::::::::")
                                                        modulo.mostrar_luces_prendidos()
                                        
                                                        pass
                                    
                                                    case 3: 
                                                        print("\n::::::::::::::::::::::::")
                                                        print(":: TODAS UBICACIONES ::")
                                                        print("::::::::::::::::::::::::")
                                                        modulo.mostrar_luces()
                                        
                                                        pass
                                    
                                                    case 4: 
                                    
                                                        break
                                                    case _:
                                                        print("Error : Ingreso una opcion no valida")
                                    
                                            case 3: 
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
                                       
                                    
                                            case 4:
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
                                            
                                                  
                                            case 5: 
                                                break
                
                                case 3:
                                    print("\n::::::::::::::::::::::::::")
                                    print("::  PANEL DE CALEFACCION  ::")
                                    print("::::::::::::::::::::::::::::")
                                     

                                    modulo.validar_calefacion()
                                    
                                    if modulo.validar_calefacion() == False:
                                        print("No hay dispositivos cargados")
                                    elif modulo.validar_calefacion() == True : 
                                    
                                        temperatura_hoy = int(input("Ingrese la temepratura de hoy : "))
                                        modulo.calefacion_ambiente(temperatura_hoy)
                                    
                    
                                case 4:
                                    while True:
                                        print("\n::::::::::::::::::::::")
                                        print(":: Panel Ubicacion  ::")
                                        print("::::::::::::::::::::::")
                                        print("Opcion 1: Crear ubicacion")
                                        print("Opcion 2 : Mostrar Ubicacion")
                                        print("Opcion 3 : eliminar ubicacion")
                                        print("Opcion 4 : Volver al menu anterior")
                    
                                        opcion = input("Ingrese una Opcion: ")
                            
                                        if not opcion.isdigit():
                                            print("Error Ingrese Digitos Numericos")
                                            continue
                            
                                        else : 
                                            convertir = int(opcion)
                    
                                        match convertir:
                        
                                            case 1: 
                                                
                                                print("\n::::::::::::::::::::::::::")
                                                print("::  Crear Ubicaciones   ::")
                                                print(":::::::::::::::::::::::::")
                                                ubicacion = input("Ingrese una ubicacion: ")
                                                modulo.Crear_ubicacion(ubicacion)
                                                pass
                                            case 2: 
                                                print("\n::::::::::::::::::::::::::::::")
                                                print("::  Todas las Ubicaciones   ::")
                                                print("::::::::::::::::::::::::::::::")
                                                modulo.Mostrar_Habitaciones()
                                                pass
                    
                                            case 3:
                                                print("\n::::::::::::::::::::::::::::::")
                                                print("::   Ubicaciones a Eliminar  ::")
                                                print("::::::::::::::::::::::::::::::")
                            
                                                busqueda = input("Ingrese la ubicacion a eliminar: ")
                                                print("\n")
                                                modulo.eliminar_ubicacion(busqueda)
                                                
                                                if modulo.eliminar_ubicacion(busqueda) == True:
                                                    print("Se elimino con exito")
                                                
                                            case 4 : 
                                                break
                                
                                            case _: 
                                                print("Error ingreso una opcion invalida")
                                                continue
                                            
                                case 5:
                                    while True:
                                        print("\n::::::::::::::::::::::::::::")
                                        print("::  Configuracion Usuario  ::")
                                        print(":::::::::::::::::::::::::::::")
                                        print("Opcion 1 : Mostrar todos los usuarios")
                                        print("Opcion 2 : Cambiar rol de un usuario")
                                        print("Opcion 3 : Volver al menu anterior")
                                    
                                        opcion = input("Ingrese una opcion: ")
                                    
                                        if not opcion.isdigit():
                                            print("Error: Ingrese Digitos numericos")
                                            continue
                                        else: 
                                            convertir = int(opcion)
                                    
                                        match convertir :
                                        
                                            case 1: 
                                                print("\n::::::::::::::::::::::::::::::")
                                                print("::  TODOS LOS USUARIOS   ::")
                                                print("::::::::::::::::::::::::::::::")
                                                modulo.mostrar_usuarios()
                                            case 2: 
                                                print("\n:::::::::::::::::::::")
                                                print("::  Cambio de Rol   ::")
                                                print("::::::::::::::::::::::")
                                                print("Opcion 1 : Dar Rol De administrador ")
                                                print ("Opcion 2 : Dar Rol de Usuario Standar")
                                                print("Opcion 3 : Volver al menu anterior")
                                                opcion = input("Ingrese una opcion ")
                                                
                                                if not opcion.isdigit():
                                                    print("Error : Ingrese digitos numericos")
                                                    continue
                                                else : 
                                                    convertir = int(opcion)
                                                
                                                match convertir:
                                                    case 1 :
                
                                                        busqueda = input("Ingrese el usuario para cambiar Rol: ")
                                                
                                                        modulo.cambiar_rol_usuario_a_admin(busqueda)
                                                    case 2 : 
                                                        busqueda = input("Ingrese el usuario para cambiar Rol: ")
                                                        modulo.cambiar_rol_admin_a_usuario(busqueda)
                                                        
                                            case 3 : 
                                                break
                                            case _:
                                                print("Ingreso una opcion invalida")
                                case 6: 
                                    break
                    case _:
                        print("ERROR : Ingreso una opcion incorrecta")
                        
            #Panel  Registrar Usuario
            case 2 : 
                    verificar_bucle_dni = True
                    verificar_bucle_email = True
                    print("\n::::::::::::::::::::::::::::::")
                    print("::      Registro Usuario    ::")
                    print("::::::::::::::::::::::::::::::")
                    
                    usuario = input("Ingrese el usuario: ").strip()
                    contrasenia = input("Ingrese su contraseña: ").strip()
                    while verificar_bucle_email: # verificacmos que el email que contaga el caracater @ para que sea valido
                        
                        email_verificar  = input("Ingrese su Email: ").strip()
                        
                        for caracter in email_verificar:
                            if caracter == "@":
                                verificar_bucle_email = False
                                email = email_verificar
                        if verificar_bucle_email == True :
                            print("Error el Email no es valido Tiene que contiener el caracter @")     

                    while verificar_bucle_dni : # verificamos que tenga la cantidad de 8 digitos. 
                        dni_verificar = input("Ingrese su DNI: ").strip()
                    
                        if len(dni_verificar) == 8 :
                            dni = int(dni_verificar)
                            verificar_bucle_dni = False
                        else :
                            print ("El DNI no tiene los digitos correspondientes ")
                            continue 
    
                    numero_secreto = input("Ingrese un numero secreto para recuperar contraseña: ").strip()
                    
                    if contador==0 :
                        rol = 1
                    else:
                        rol =0
                    
                    modulo.registrar_usuario(usuario,contrasenia,email,dni,numero_secreto,rol)
                    contador+=1
                    
                
            case _:
                    print("Ingreso una opcion incorrecta")
 