# Este programa intenta sumar una lista de números pero tenia errores
def sumar_lista(numeros):
    total = 0
    for n in numeros:
        total = total + n
    return total


mi_lista = [10, 20, 30, 40]  # Error aquí: habia un string
resultado = sumar_lista(mi_lista)
print(
    "El total es: " + str(resultado)
)  # Error aquí: no puedes sumar texto con número, por lo que se convierte a string
