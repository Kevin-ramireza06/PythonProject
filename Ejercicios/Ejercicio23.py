for i in range(1,101) :
    contador = 0
    for j in range(1,(int(i/2))+1) :
        if i % j == 0 :
            contador += 1
    if contador == 1 :
        print(i)