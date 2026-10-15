from funciones import * 
from random import *

mensaje_menu: str = """
=========== MENU ===========
1. Generar contraseñas.
2. Buscar contraseña.
3. Informar estadísticas.
4. Ordenar y mostrar contraseñas.
5. Salir.
============================
-> """

mensaje_clave: str = """
================ GENERAR CLAVES ================
 Ingrese la cantidad de claves que desea generar
================================================
-> """

mensaje_error: str = """[X] VALOR INGRESADO INCORRECTO [X]"""
claves = None
menu = None



while menu != 5:
    menu: int = int(input(mensaje_menu))
    menu: int = validar_menu(menu, mensaje_menu, mensaje_error )

    match menu:
        case 1:
            claves = int(input(mensaje_clave))
            claves = validar_entero(menu, mensaje_menu, mensaje_error)
            claves= []
        case 2:
            print("Ingresaste a dos")

        case 3:
            print("Ingresaste a tres")

        case 4: 
            print("Ingresaste a cuatro")

