var=0
with open('Nombres_variables.txt', 'r') as archivo:
    with open('salida.txt', 'w') as archivo_destino:
                    for linea in archivo:
                        palabras = linea.split()
                        for palabra in palabras:
                            i = 0
                            while i < len(palabra) and palabra[i] not in ['.', '_']:
                                i += 1
                                
                        var = var+ 1       
                        archivo_destino.write('%s   %s  %s' %(var,palabra[:i],linea))
       

       
            
                                                                               

"""
'I am %s %s. I teach %s' %(first_name, last_name, language)
var = 0
with open('Nombres_variables.txt', 'r') as archivo:
    for linea in archivo:
        palabras = linea.split()
        for palabra in palabras:
            i = 0
            while i < len(palabra) and palabra[i] not in ['.', '_']:
                i += 1
            var += 1
            print('{}  {}  '.format(var, palabra[:i]))



with open("Nombres_variables.txt", "r") as f:
    contenido = f.read(2097)

# Separar el contenido en palabras y ordenarlas alfabéticamente
palabras = contenido.split()
palabras.sort()

# Imprimir las variables hasta encontrar un punto o un guión bajo
i = 1
for palabra in palabras:
    variable = ""
    for c in palabra:
        if c in [".", "_"]:
            break
        variable += c
    print(f"{i}. {variable}")
    i += 1
       

"""