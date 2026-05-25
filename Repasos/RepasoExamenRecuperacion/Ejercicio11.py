accesos = [
    ("192.168.1.1", "/home", 200),
    ("10.0.0.5", "/admin", 401),
    ("192.168.1.1", "/login", 200),
    ("172.16.0.2", "/imagenes/logo.png", 404),
    ("10.0.0.5", "/admin", 404),
    ("192.168.1.1", "/imagenes/logo.png", 404)
]

ipsUnicas = set()

for i in accesos:
    ipsUnicas.add(i[0])

print("Ips Unicas:" , ipsUnicas)

rutasFallidas = set()
for i in accesos:
    if i[2] == 404:
        rutasFallidas.add(i[1])

print("Runtas fallidas: " , rutasFallidas)
