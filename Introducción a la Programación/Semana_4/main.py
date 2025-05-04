import usuario

if __name__ == "__main__":
    
 while True:

    print("Opcion 1. Registrar Usuario")
    print("Opcion 2. Buscar Usuario")
    print("Opcion 3. Eliminar Usuario")
    print("Opcion 4. Mostrar Usuarios")
    opcion = int(input("Ingrese Una Opcion: "))
    #if opcion <3 :
    #    print("Error Ingrese una opcion valida")
    #    continue

    match(opcion):
     case 1: 
         usuario.Registrar_Usuario()
         pass
     case 2: 
         usuario.buscar_usuario()
         pass
     case 3: 
         usuario.Eliminar_Usuario()
         pass
     case 4:
         usuario.mostrar_usuario()
         pass
     case _:
         print("Error Ingrese una opcion valida")
         continue
         
    pregunta = input("Desea usar otra funcion ? Si o No: ").lower().strip()
    if pregunta == "no":
        print("Saliendo...")
        break
    
    