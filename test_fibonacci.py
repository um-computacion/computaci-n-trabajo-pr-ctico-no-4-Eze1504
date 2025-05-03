def fibonacci_iterativo(n):

    if n < 0:
        raise ValueError("No se puede calcular Fibonacci para un número negativo")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def fibonacci_recursivo(n):
    
    if n < 0:
        raise ValueError("No se puede calcular Fibonacci para un número negativo")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)