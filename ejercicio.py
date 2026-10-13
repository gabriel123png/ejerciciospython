def calcular_medalla(puntos):
    if puntos >= 4.5:
        return "Oro"
    elif puntos >= 4.0:
        return "Plata"
    elif puntos >= 3.8:
        return "Bronce"
    else:
        return "Sin medalla"

print(calcular_medalla(3.4))