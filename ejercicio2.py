class descuento:
    def __init__(self):
        self.porcentaje = 15
        self.limite = 300000



    def aplicar_descuento(self, precio):
        if precio > self.limite:
            descuento = precio * (self.porcentaje / 100)
            return precio - descuento
        return precio

    def envio_gratis (self,popayan):
        if popayan:
            return True
        else:
            return False

        if envio_gratis( True):
            print("El envío es gratis")
        else:
            print("El envío tiene un costo adicional")

    def valor_total(self, precio, popayan):
        precio_con_descuento = self.aplicar_descuento(precio)
        if self.envio_gratis(popayan):
            return precio_con_descuento
        else:
            costo_envio = 10000
            return precio_con_descuento + costo_envio

print(descuento().aplicar_descuento(350000))
print(descuento().valor_total(3000, True))