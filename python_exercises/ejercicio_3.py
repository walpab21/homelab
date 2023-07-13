def valida_ceros(*args):
    anterior=999
    for n in args:
        if (n == 0) and (anterior == 0):
            return True
        else:
            anterior = n
            continue
    return False


print(valida_ceros(5,0,0,2,8))