try:
    fichero = open("quijote.txt", "rt") #Con esta variable ya tenemos acceso y podemos usar el fichero

#Tiene un segundo parametro que es opcional en el cual definimos de que modo lo queremos abrir('rt')
    #Quiere decir que se abre en modo lectura, y es de texto
    #Las dormas mas comunes de usarlas son para abrirlo son
    #   r = lectura
    #   w = escritura
    #   a = agreagar al final
    #Y los tipos de fichero mas comunes son:
    #   t = texto
    #   n = binario
    #Podemos agreagar un + y este indica que se puede realizar la otra operacion, pero depende de cual pongamos primero

    #texto = fichero.read() #Este lee el fichero completo
    #print(texto)
    #Siempre que se ejecuta algo con el fichero el cursosr va a aavanzar, y lo siguiente se va a ejecutar desde donde
    #esta el cursor

    # lineas = fichero.readlines() #Este guarda tambien el fichero completo, pero como lista, y cada elemento es una linea
    # #Y guarda tambien el caracter de la linea que seria el "\n"
    # for l in lineas:
    #     print(l[:-1])
    # print("----------------")
    #
    # for i in range(len(lineas)):
    #     if lineas[i][-1] == "\n": #i == len(lineas):
    #         lineas[i] = lineas[i][:-1]
    # print(lineas)
    # #fichero = fichero.readlines() #ESte guarda tambien el fichero completo, pero como lista, y cada elemento es una linea

    linea = fichero.readline(5)
    while linea != "":
        print(linea)
        linea = fichero.readline(5) #el read line lee una linea entera desde donde esta el cursor, hasta que necuentra un "\n"
        #Si se le pone un parametro, leera la cantidad de caracteres que se le indique y pasara a la siguiente linea
    fichero.close() #DE esta forma abrimos y cerramos un fichero

#Salta excepciones si el fichero no existe
except:
    print("Error al abrir el fichero")
    #Como en java, lo mejor es trabajar los ficheros con try catch