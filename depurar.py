# This program tries to sum a list of numbers but had errors.
def sumar_lista(numeros):
    total = 0
    for n in numeros:
        total = total + n
    return total


mi_lista = [10, 20, 30, 40]  # Error here: there was a string
resultado = sumar_lista(mi_lista)
print(
    "El total es: " + str(resultado)
)  # Error here: you cannot add text with a number, so it is converted to a string
