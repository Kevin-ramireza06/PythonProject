import re

ip = str(input("Pofavor dame una ip: "))

patron = r"^(([0-9]{1})|([0-9][0-9]{2})|([1][0-9][0-9]{3})|([2][0-4][0-9]{3})|([2][5][0-5]{3})).+([0-9]{1})|([0-9][0-9]{2})|([1][0-9][0-9]{3})|([2][0-4][0-9]{3})|([2][5][0-5]{3}).+([0-9]{1})|([0-9][0-9]{2})|([1][0-9][0-9]{3})|([2][0-4][0-9]{3})|([2][5][0-5]{3}).+([0-9]{1})|([0-9][0-9]{2})|([1][0-9][0-9]{3})|([2][0-4][0-9]{3})|([2][5][0-5]{3})$"

if re.fullmatch(patron, ip):
    bytes = ip.split(".")
    if int(bytes[0]) <= 127 : #if int(bytes[0]) in range (0,128):
        print(ip,"/8", sep="")
    if int(bytes[0]) <= 191 and int(bytes[0]) >= 128:
        print(ip, "/16", sep="")
    if int(bytes[0]) <= 223 and int(bytes[0]) >= 192:
        print(ip, "/24", sep="")
    if int(bytes[0]) <= 255 and int(bytes[0]) >= 224:
        print("Direccion reservada")
    if int(bytes[0]) > 255 and int(bytes[0]) < 0:
        print("La direcccion no es valida")
else:
    print("La direcccion no es valida")