# solicita input
texto=input("Ingrese texto a analizar: \n\n")

# ingresa 3 letras
print("\n")
l1=input("Ingrese letra 1:")
l2=input("Ingrese letra 2:")
l3=input("Ingrese letra 3:")

# analizando...
print("\nAnalizando texto...\n")

# convertir a minuscula
texto = texto.lower()

# guardar palabras en lista
lista_palabras = texto.split()

# remover espacios del texto
texto_letras = texto.replace(" ","")

# remover comas del texto
texto_letras = texto_letras.replace(",","")

# guardar letras en lista
lista_letras = list(texto_letras)

# ITEM 1: cuantas veces aparece cada letra elegida
c1=lista_letras.count(l1)
c2=lista_letras.count(l2)
c3=lista_letras.count(l3)
print(f"La letra '{l1}' aparece {c1}")
print(f"La letra '{l2}' aparece {c2}")
print(f"La letra '{l3}' aparece {c3}")

# ITEM 2: cuantas palabras hay en total
cantidad_palabras=len(lista_palabras)
print(f"Hay en total {cantidad_palabras} palabras")

# ITEM 3: mostrar primera y ultima letra
primera_letra = lista_letras[0]
ultima_letra = lista_letras[-1]
print(f"La primera letra es '{primera_letra}' y la ultima es '{ultima_letra}'")

# ITEM 4: palabras en orden inverso
lista_palabras_inverso=lista_palabras[::-1]
print(" ".join(lista_palabras_inverso))

# ITEM 5: validar si la palabra python se encuentra en el texto
print("python" in lista_palabras)
