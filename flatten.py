def flatten(estructura):
    resultado = []   
    if isinstance(estructura, (list, tuple)):
        for item in estructura:
            resultado.extend(flatten(item))
    elif isinstance(estructura, dict):
        for key in estructura:
            resultado.extend(flatten(key))
            resultado.extend(flatten(estructura[key]))
    else:
        resultado.append(estructura)
    
    return resultado