List_usuario=[]
def Registrar_Usuario():
    
     verificar=True
     
     while verificar:  
    
        nombre = input("Ingrese el usuario: ")
        
        contrasenia = input("Ingrese la contraseña: ")
        
        email = input("Ingrese su Email: ")
        
        if nombre =="" or contrasenia =="" or email=="":
            print("Error Complete todos los campos")
            continue
    
        usuario={"nombre":nombre,"contrasenia":contrasenia,"email":email}
        
        if nombre != "" and contrasenia !="" and email!="":
            List_usuario.append(usuario)
            print("Se Agrego con exito")
    
        pregunta = input("¿Desea ingresar otro usuario? Si o No: ").lower().strip()

        if pregunta =="no":
            verificar = False
    
def Eliminar_Usuario():
    busqueda= input("Ingrese el usuario a eliminar: ")
    Encontrado = False
    
    for usuario in List_usuario: # Se Crea una copia de la lista 
        
        if usuario["nombre"]== busqueda:
            List_usuario.remove(usuario)
            Encontrado=True
            print("Se Elimino con exito")
    
    if Encontrado==False:
        print("No se encontro el usuario")
    
    
def buscar_usuario():
    busqueda = input("Ingrese el usuario a buscar: ")
    encontrado = False
    for usuario in List_usuario:
        
        if usuario["nombre"]== busqueda:
            encontrado=True
            print("Se encontro con exito")
            print(usuario)
            
    if encontrado== False:
        print("No se encontro el usuario")
       
def mostrar_usuario():
    print(List_usuario)
    
    

