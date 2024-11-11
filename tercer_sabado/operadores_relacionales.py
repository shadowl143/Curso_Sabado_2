
from util.custom_input import *

def operadores_relacionales() -> None:
    value = only_number("ingrese un numero")
    value_other = only_number("ingrese otro numero")
    print(f"{value} es mayor que {value_other}: {value > value_other}") #  falso
    print(f"{value} es mayor o igual que {value_other}: {value >= value_other}") # falso
    print(f"{value} es menor que {value_other}: {value < value_other}") # verdadero
    print(f"{value} es menor igual que {value_other}: {value <= value_other}") #verdadero 
    print(f"{value} es igual que {value_other}: {value > value_other}") # falso 
    print(f"{value} es diferente que {value_other}: {value != value_other}") # falso