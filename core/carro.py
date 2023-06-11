class Carro:
    def __init__(self,request):
        self.request = request 
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"]={}

        self.carro = carro

    def agregar(self,producto):
        id = str(producto.Barcode)
        if id not in self.carro.keys():
            self.carro[id]={
                "producto_id" :producto.Barcode,
                "nombre" : producto.nombre,
                "acumulado" : producto.precio,
                "cantidad": 1,

            }
        else:
            self.carro[id]['cantidad'] +=1
            self.carro[id] ["acumulado"] += producto.precio
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified= True



    def eliminar(self, producto):
        producto.Barcode = str(producto.Barcode)
        if producto.Barcode in self.carro:
            del self.carro[producto.Barcode]
            self.guardar_carro()


    def restar_producto(self,producto):
        id = str(producto.Barcode)
        if id in self.carro.keys():
            self.carro[id]["cantidad"] -= 1
            self.carro[id]["acumulado"] -= producto.precio
            if self.carro[id]["cantidad"] <= 0 :self.eliminar(producto)
            self.guardar_carro()

    # def eliminar_producto(self,producto):
    #     id = str(producto.Barcode)
    #     if id in self.carro.keys():
    #         self.eliminar(producto)
    #         self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified= True

        