def only_number(text: str) -> int:
    value = input(f"{text}\n")
    if not value.isnumeric():
        print("El dato no es numerico ingrese otro: ")
        only_number(text)
    return int(value)

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

if __name__ == "__main__":
    pass