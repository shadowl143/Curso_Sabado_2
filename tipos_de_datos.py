# Este es un comentario de una sola linea
'''
Author: Julián Lara
Fecha: 26/10/24
Descripcion: Tipos de datos y comentarios
'''

str_text: str = "saludo" # este es un tipo de dato para textos
i_number: int = 1 # tipo de dato numerico que se utiliza cuando la variables es utilizada para operaciones aritmeticas.
numero_decimal: float = 2.0 # es un tipo d dato numerico con decimales a diferencia de los int un decimal siempre tendra .
estado: bool = True # utilizados para mostrar un dato como true or false.

# print es utilizado para mostrar en pantalla un texto y el type muestra el tipo de dato que este contiene.
print(type(str_text))
print(type(i_number))
print(type(numero_decimal))
print(type(estado))

## Concatenar string
# 1:
name = "julian"
surname = "lara"
primer_forma = ("hola", str_text) # funciona algo distinto de lol esperado
segunda_forma = ("el nombre %s su apellido es  %s" %(name, surname)) 
tercer_forma = f"e nombre {name} su apellido es  {surname}"

print(name, surname) # forma de concatenar por medio de comas.
print("{} {}".format(name, surname)) # esta forma de concatenar es por medio una funcion de la clase str
print(name + ' ' + surname) # forma de concatenar mas comun en lenguajes de programación en general
print(f"{name} {surname}") # ingresar variables dentro de una cadena de texo de forma literal es las mas utilizado por su visibilidad y facilidad de uso.

print("hola {} {}".format(str_text, estado))
print(segunda_forma)
print(tercer_forma)


### numerico ###
resultado_suma = i_number + 20 # suma
resultado_resta = i_number - 20 #resta
resultado_multiplicar = i_number * 20 #multiplicacion
resultado_dividir = i_number / 20 #division
resultado_suma = i_number + 20

print(resultado_suma)
print(resultado_resta)
print(resultado_multiplicar)
print(resultado_dividir)

print(10/3)
resultado_exponente = 2 ** 3
resultado_division_enteros = 10 // 3
resultado_residuo = i_number % 2 # pares impares<
variables_complejas = 2j #complex

print(variables_complejas * 2j)


print(i_number * numero_decimal)
# print(10/3)
# print(resultado_division_enteros)
# print(resultado_exponente)
# print(resultado_residuo)
mostrar_repetido = str_text * 5
print(str_text * 5)
print(mostrar_repetido +' '+ str_text)