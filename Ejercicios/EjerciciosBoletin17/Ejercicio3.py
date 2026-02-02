# Un código bancario en formato IBAN en nuestro país está formado por 24 caracteres de los
# cuales los dos primeros son letras y los restantes 22 son dígitos númericos comprendidos entre el 0
# y el 9. Por ejemplo, el siguiente sería un IBAN válido
# ES1234567890123456789012
# Es corriente verlos escritos tanto de esta forma, sin espacios, como con diferentes separaciones
# para que sea más cómodo. Por ejemplo, los siguientes también serían IBAN válidos:
# ES12 3456 7890 1234 5678 9012
# ES12 3456 7890 12 3456789012
# ES 12 3456 7890 123456789012
# Escribe una función que reciba como argumento un nombre de fichero que tendrá un listado de
# códigos de este tipo. Algunos serán válidos y otros no. Tu programa debería de mostrar por consola
# sólo los válidos. Por ejemplo, si el contenido del fichero codigos.txt recibido fuese este:
# ES1234567890123456789012
# UK12345678901234567
# 3312 3456 7890 1234 5678 9012
# ES12 3456 7890 12 345678901299999
# FR32 5456 7898 22 0456789012
# ES 12 3456 7XX0 123456789012
# Tu programa debería de dar la siguiente salida en consola:
# Códigos correctos en el fichero codigos.txt:
# País: ES
# DC: 12
# Entidad: 3456
# Sucursal: 7890
# DC cuenta: 12
# Número de cuenta: 3456789012
# País: FR
# DC: 32
# Entidad: 5456
# Sucursal: 7898
# DC cuenta: 22
# Número de cuenta: 0456789012
# Hay 2 códigos correctos y 4 incorrectos
# Como puedes ver, los distintos elementos del código son los dígitos del mismo tal y como aparecen
# ordenados en él. Y, como siempre, cuida de que la salida sea igual a la que se muestra aquí
import re

def validarIBAN(nombreFichero):
    with open(nombreFichero, "r") as fichero:
        regex = r"^[A-Z]{2}( *[0-9] *){22}$"
        contadorCorrectos = 0
        contadorInorrectos = 0

        print("Códigos correctos en el fichero codigos.txt:")
        for linea in fichero:
            linea = linea.replace(" ", "").strip()
            if re.fullmatch(regex, linea):
                contadorCorrectos += 1
                print("Pais:", linea[0:2])
                print("DC:", linea[2:4])
                print("Entidad:", linea[4:8])
                print("Sucursal:", linea[8:12])
                print("DC Cuenta:", linea[14:16])
                print("Numero de cuentna:", linea[16:])
            else:
                contadorInorrectos += 1
        # if re.fullmatch(regex, linea):
        #     linea = linea.replace(" ", "")
        #     contadorCorrectos += 1
        #     print("Pais:", linea[0:2])
        #     print("DC:", linea[2:4])
        #     print("Entidad:", linea[4:8])
        #     print("Sucursal:", linea[8:12])
        #     print("DC Cuenta:", linea[13:15])
        #     print("Numero de cuentna:", linea[15:])
        # else:
        #     contadorInorrectos += 1
        #
        # while linea != "":
        #     linea = fichero.readline().strip()
        #     if re.fullmatch(regex, linea):
        #         linea = linea.replace(" ", "")
        #         contadorCorrectos += 1
        #         print("Pais:",linea[0:2])
        #         print("DC:",linea[2:4])
        #         print("Entidad:",linea[4:8])
        #         print("Sucursal:",linea[8:12])
        #         print("DC Cuenta:",linea[13:15])
        #         print("Numero de cuentna:",linea[15:])
        #     else:
        #         contadorInorrectos += 1

        print("Hay", contadorCorrectos,"codigos correctos y", contadorInorrectos,"codigos incorrectos")

validarIBAN("Ejercicio3Prueba")


