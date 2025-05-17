dispositivos =[]

 
def agregar(nombre_dispositivo,marca,modelo,tipo,color,consumo_energia,voltaje):
    
    
    dispositivo = {"nombre_dispositivo":nombre_dispositivo,"marca":marca,"modelo":modelo,"tipo":tipo,"color":color, 
                   "consumo_energia": consumo_energia,"voltaje":voltaje}
    
    dispositivos.append(dispositivo)    
    

def mostrar(): # Funcion para mostar todos los dispositivos
    
    if len(dispositivos)== 0:
        return "Sin dispositivos"
    
    for dispositivo in dispositivos:
        
        print(dispositivo)

def buscar(busqueda):
    
    encontrado = False
    
    for dispositivo in dispositivos:
        
        if dispositivo['nombre_dispositivo'] == busqueda:
            encontrado = True
            return(dispositivo) 
        
    if encontrado== False:
        print("No se encontro el dispositivo")

def eliminar(busqueda):
    
    encontrado = False
    
    for dispositivo in dispositivos:
        
        if dispositivo['nombre_dispositivo'] == busqueda:
            encontrado = True
            dispositivos.remove(dispositivo)
         print(f"{dispositivo} Se elimino con exito")
    if encontrado== False:
        print("No se encontro el dispositivo")