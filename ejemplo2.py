def calcular_pago (horas  , tarifa_hora=200000):
    if horas > 40:
        return 100000
    return horas * tarifa_hora
print(calcular_pago(50, 300000))
print(calcular_pago(30, 300000))