#Son funciones sin nombre y que solo tienen una linea de codigo/funcionalidad

def cuadrado(x):
    return x**2

print(cuadrado(5))

cuadradoLambda = lambda x: x**2 #Asi se hace una funcion lambda
#Ponemos la lambda en una variable, y para acceder al resultado, usamos la variable
print(cuadradoLambda(5))
#Para llamar las lambdas y pasasrle los parametros, usamos la sintaxis de una funcion normal( funcion(parametro) )

#Asi se haria una lambda con parametros variables
promedio = lambda *lista : sum(lista)/len(lista)

print(promedio(9,8,5,4))
print(promedio(7,2))

cuadradoMayorQue10 = lambda  x: True if x**2 >= 10 else False #Aqui usamos y asi se usa el operador ternario


print(cuadradoMayorQue10(4))