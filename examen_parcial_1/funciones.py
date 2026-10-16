from random import *

def validar_menu(numero:int, mensaje_numero:str, mensaje_error:str) -> int:
    while numero < 0 or numero > 5:
        numero = int(input(f"""{mensaje_error}
{mensaje_numero}"""))

    return(numero)

def validar_entero(numero:int, mensaje_numero:str, mensaje_error:str) -> int:
    while numero < 0:
        numero = int(input(f"""{mensaje_error}
{mensaje_numero}"""))

    return(numero)

def obtener_minuscula():
    letras_minusculas = randint(97,122)
    letras_minusculas = chr(letras_minusculas)
    return letras_minusculas

def obtener_mayuscula():
    letras_mayusculas = randint(65,90)
    letras_mayusculas = chr(letras_mayusculas)
    return letras_mayusculas

def obtener_numeros_naturales():
    numero = randint(1,9)
    numero = f"{numero}"
    return numero

def obtener_lista_de_caracteres(longitud):
    clave = ""
    for i in range(longitud):
        opcion_caracter = randint(1,3)
        if opcion_caracter == 1:
            mayuscula = obtener_mayuscula()
            caracter = mayuscula
        elif opcion_caracter == 2:
            minuscula = obtener_minuscula()
            caracter = minuscula
        else:
            numero_natural = obtener_numeros_naturales()
            caracter = numero_natural
        clave += (f"{caracter}")
    return clave


def obtener_lista_de_claves(cantidad_claves):
    listas = []
    for _ in range(cantidad_claves):
        longitud = randint(8, 15)
        listas += [obtener_lista_de_caracteres(longitud)]
    return listas


def obtener_claves_en_string(lista_de_claves):
    claves_string = ""

    for i in range(len(lista_de_claves)):
        claves_string += lista_de_claves[i] + "\n"

    return claves_string

lista_claves = obtener_lista_de_claves(8)
claves = obtener_claves_en_string(lista_claves)
print(claves)