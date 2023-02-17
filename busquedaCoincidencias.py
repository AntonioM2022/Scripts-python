#Ejemplo de como encontrar coincidencias en un archivo de texto.
def busquedaTexto():
    print("Busqueda en un archivo de texto. ")
    nombreArchivo=input ("Escriba el nombre del archivo: ")
    coincidencias=0
    try:
        with open(nombreArchivo, "r") as archivo:
            busqueda= input("Texto a buscar: ")
            print("\n Resultados :")
            for i, linea in enumerate(archivo):
                if busqueda.lower() in linea.lower():
                    print(f"Linea {i + 1}: {linea}", end= "")
                    coincidencias+=1
            if coincidencias ==0:
                print("No hubo coincidencias. ")
            else:
                print(f"Coincidencias encontradas: {coincidencias}.")        

        
    except OSError as e:
        print(f"Error al acceder el archivo: {e}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")    
