def contar_primos(numero):

    cont = 0
    primos = []

    for n in range(1, numero + 1):
        
        for d in range(1, n + 1):
            if n % d == 0:
                cont += 1
        
        if cont == 2:
            #print("{}".format(n), end=" ")
            primos.append(n)

        cont = 0

    return primos

print(contar_primos(13))
