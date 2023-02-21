with open('Nombres_variables.txt', 'r') as f:
    t= f.readlines()

for linea in t:
    variables_nombre=t 

    var=0
    while(var<2097):
        var= var+1
    
        with open('Nombres_variables.txt', 'r') as archivo:
                    for linea in archivo:
                        palabras = linea.split()
                        for palabra in palabras:
                            i = 0
                            while i < len(palabra) and palabra[i] not in ['.', '_']:
                                i += 1
                            
                        print('{}  {} {}'.format (var,variables_nombre, palabra[:i]))    
       
       
       
       

       
            
                                                                               

"""
salida = open ('Salida_datos_ordenados','w')
salida.write(str_varord)
salida.close()c 


for lines in range(500):# 500= numero de lineas que queremos que lea del document
        linea = archivo.readline()
        print(linea)

       
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