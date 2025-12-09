#Son funciones sin nombre y que solo tienen una linea de codigo/funcionalidad

def cuadrado(x):
    return x**2

print(cuadrado(5))

cuadradoLambda = lambda x: x**2 #Asi se hace una funcion lambda
#Ponemos la lambda en una variable, y para acceder al resultado, usamos la variable
print(cuadradoLambda(5))
#Para llamar las lambdas y pasasrle los parametros, usamos la sintaxis de una funcion normal( funcion(parametro) )

promedio = lambda *lista : sum(lista)/len(lista)
#Asi se haria una lambda con parametros variables

print(promedio(9,8,5,4))
print(promedio(7,2))
