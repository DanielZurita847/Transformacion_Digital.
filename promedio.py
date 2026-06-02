def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
        numeros (list): Lista de valores numéricos.

    Retorna:
        float: Promedio de los números de la lista.
    """
    if len(numeros) == 0:
        return 0

    return sum(numeros) / len(numeros)


# Solicitar datos al usuario
entrada = input("Ingrese varios números separados por comas: ")

# Convertir la entrada en una lista de números
numeros = [float(numero) for numero in entrada.split(",")]

# Calcular y mostrar el promedio
promedio = calcular_promedio(numeros)

print(f"Los números ingresados son: {numeros}")
print(f"El promedio es: {promedio:.2f}")