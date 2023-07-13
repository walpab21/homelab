def modifica_palabra(palabra):
    palabra_set=set(palabra)
    palabra_set_ordenada=sorted(palabra_set)
    return palabra_set_ordenada

print(modifica_palabra("supertux"))
