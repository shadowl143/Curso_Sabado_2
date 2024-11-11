from .operadores_logicos import seleccion_opcion
from .operadores_relacionales import operadores_relacionales
from util.custom_input import only_number
from os import system

def opciones():
    option = only_number("Desea ver ejemplos del tercer sabado ejemplo \n 1.-Si \n2.-No.")
    system("cls")
    if option == 1:
        ejemplo = only_number("seleccione una de las siguientes opciones para continuar\n 1.- operadores logicos\n 2.-operadores_relacionales")
        if ejemplo == 1:
            seleccion_opcion()
            opciones()
        elif ejemplo == 2:
            operadores_relacionales()
            opciones()
    else:
        system("cls")
        print("Gracias por revisar los ejemplos")