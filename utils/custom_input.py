def only_number(text: str) -> int:
    value = input(f"{text}\n")
    if not value.isnumeric():
        print("El dato no es numerico ingrese otro: ")
        only_number(text)
    return int(value)

# number = only_number("Ingrese un numero")
# print(f"El numero ingresado fue {number}")
# print(type(number))
# only_number("Ingrese su edad")

# value = only_number("ingrese un numero")
# value_other = only_number("ingrese otro numero")

# print(value > value_other) #  falso
# print(value >= value_other) # falso
# print(value < value_other) # verdadero
# print(value <= value_other) #verdadero 
# print(value == value_other) # falso 
# print(value != value_other) # falso

# a = "hola"
# b = "hola"

# print(a is b)
# print(a == b)
# print(id(a))
# print(id(b))
# c = a*100
# d = c
# print(a*100 is b*100)
# print(d is c)
# print(a*100 == b*100)

verdad = True
mentira = False

print(verdad and verdad)
print(verdad and mentira)
print(mentira and mentira)
print(mentira and verdad)

print(verdad or verdad) # verdad
print(verdad or mentira) # verdad 2, 3 falso
print(mentira or mentira) #verdad  y falso
print(mentira or verdad) # falso y verda
print("Not \n\n")
print(not (verdad or verdad)) # verdad
print(not (verdad or mentira)) # verdad 2, 3 falso
print(not (mentira or mentira)) #verdad  y falso
print(not (mentira or verdad)) # falso y verda