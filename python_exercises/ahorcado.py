from random import *

def elegir_palabra():
    lista_palabras=['hola','cocodrilo','rinoceronte','elefante','hipopotamo','leopardo']
    palabra_secreta=choice(lista_palabras)
    return palabra_secreta.upper()


def iniciar_juego(palabra_elegida):

    letra='0'
    longitud=len(palabra_elegida)
    intentos=longitud
    palabra_oculta=list('_'*longitud)

    print('\n')
    print(palabra_oculta)

    while intentos > 0:

        if palabra_oculta == list(palabra_elegida):
            print("\n¡Felicidades!, has ganado\n")
            break
        
        letra=ingresar_letra()

        if letra not in palabra_elegida:
            intentos-=1
            print('\nTe quedan ' + str(intentos) + ' vidas\n')
            if intentos == 0:
                print("\nSe acabaron los intentos, ¡Has perdido!\n")
                break
            
        for i, l in enumerate(palabra_elegida):
            if l == letra:
                palabra_oculta[i]=letra
        
        print(palabra_oculta)


def ingresar_letra():

    letra='000'
       
    while len(letra) > 1 or letra.isalpha() == False:
        
        letra=input('\nInserte una letra: ')

    return letra.upper()

        
iniciar_juego(elegir_palabra())

#print(ingresar_letra())