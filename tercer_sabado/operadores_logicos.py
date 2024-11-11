from util.custom_input import only_number
from os import system

mentira = False
verdad = True

def tabla_verdad_and() -> None:
    print("Tabla de la verdad de and")
    print(f"verdad y verdad es: {verdad and verdad}")
    print(f"verdad y mentira es:{verdad and mentira}")
    print(f"mentira y mentira es: {mentira and mentira}")
    print(f"mentira y verdad es: {mentira and verdad}")

def tabla_verdad_or() -> None:
    print("Tabla de la verdad de or")
    print(f"verdad o verdad es: {verdad or verdad}")
    print(f"verdad o mentira es:{verdad or mentira}")
    print(f"mentira o mentira es: {mentira or mentira}")
    print(f"mentira o verdad es: {mentira or verdad}")

def tabla_verdad_not_and() -> None:
    print("Tabla de la verdad de not and")
    print(f"la negacion de verdad y verdad es: {not(verdad and verdad)}")
    print(f"la negacion de verdad y mentira es:{not(verdad and mentira)}")
    print(f"la negacion de mentira y mentira es: {not(mentira and mentira)}")
    print(f"la negacion de mentira y verdad es: {not(mentira and verdad)}")

def tabla_verdad_not_or() -> None:
    print("Tabla de la verdad de not or")
    print(f"la negacion de verdad o verdad es: {not(verdad or verdad)}")
    print(f"la negacion de verdad o mentira es:{not(verdad or mentira)}")
    print(f"la negacion de mentira o mentira es: {not(mentira or mentira)}")
    print(f"la negacion de mentira o verdad es: {not(mentira or verdad)}")

def opcion() -> int:
    opcion_seleccionada = only_number('''
    Seleccione el ejemplo que quiere visualizar
    1.- Tabla de verdad and
    2.- tabla de verdad or
    3.- Tabla de verdad negacion and
    4.- Tabla de verdad negacion or
    5.- Salir.
    ''')
    return opcion_seleccionada

def seleccion_opcion() -> None:
    opciones = opcion()
    system("cls")
    if opciones == 1:
        tabla_verdad_and()
        seleccion_opcion()
    elif opciones == 2:
        tabla_verdad_or()
        seleccion_opcion()
    elif opciones  == 3:
        tabla_verdad_not_and()
        seleccion_opcion()
    elif opciones == 4:
        tabla_verdad_not_or()
        seleccion_opcion()
    elif opciones == 5:
        print("Saliendo de ejemplos....")
    else:
        print("Selecciono una opcion no valida")
        seleccion_opcion()
        