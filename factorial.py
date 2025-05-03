def factorial_iterativo(n):
    
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

def factorial_recursivo(n):
    
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursivo(n - 1)