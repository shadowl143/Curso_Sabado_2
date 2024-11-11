from tercer_sabado.main_tercer_sabado import opciones
from segundo_sabado.tipos_de_datos import *
from util.custom_input import only_number
from os import system

ver = only_number("Desea ver los ejemplos\n 1.- Si\n 2.- No")
system("cls")
while ver == 1:
    dia = only_number("Seleccione un día \n 1.- Segundo Sabado \n 2.- Tercer sabado")
    if dia == 1:
        system("cls")
        todos_ejemplos()
    elif dia == 2:
        system("cls")
        opciones()
    ver = only_number("Desea ver los ejempos \n 1.- Si\n 2.- No")
    system("cls")
    
    
   