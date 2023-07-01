def devolver_distintos(num1,num2,num3):
    
    lista=[num1,num2,num3]
    mayor=max(lista)
    menor=min(lista)
    suma=sum(lista)
    lista.remove(mayor)
    lista.remove(menor)
    medio=lista[0]

    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    elif suma in range(10,16):
        return medio


print(devolver_distintos(4,3,4))
