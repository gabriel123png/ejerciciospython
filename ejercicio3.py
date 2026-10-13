class carrito_compra:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio": precio})
    def total(self):
        return sum(p["precio"] for p in self.productos)
    
carrito = carrito_compra()
carrito.agregar_producto("camisa", 522000)
carrito.agregar_producto("pantalon", 225000)
print(carrito.total())