class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
            self.cart = self.session["cart"]
        self.cart = cart

    def add(self, producto):
        identificador = str(producto.identificador)
        if identificador not in self.cart.keys():
            self.cart[identificador] = {
                "identificador": identificador,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1
            }
        else:
            self.cart[identificador]['cantidad'] += 1
        self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self, producto):
        producto_id = str(producto.identificador)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def decrement(self, producto): 
        for key, value in self.cart.items():
                if key == str(producto.identificador):
                    value["cantidad"] = value["cantidad"] - 1
                    if value["cantidad"] < 1:
                        self.remove(producto)
                    else:
                        self.save()
                    break
                else:
                    print("El producto no existe en el carrito")
    
    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True