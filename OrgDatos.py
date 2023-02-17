with open("Nombres_variables.txt", "r") as archivo:
     with open("Salida_datos_ordenados.txt", "w") as salida:
        def busquedaForm():
                coincidencias=0
                busqueda =input("Texto que quieres buscar")
                for i, linea in enumerate(archivo):
                    if busqueda.lower() in linea.lower():
                        print(f"Linea {i + 1}: {linea}", end= "")
                        coincidencias+=1
                if coincidencias ==3:
                    salida.write(linea)
                else:
                    print(f"Coincidencias encontradas: {coincidencias}.")
       

       
            
                                                                               

"""
salida = open ('Salida_datos_ordenados','w')
salida.write(str_varord)
salida.close()c 


for lines in range(500):# 500= numero de lineas que queremos que lea del document
        linea = archivo.readline()
        print(linea)

       

"""