class vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {}ruedas ".format(self.color, self.ruedas)

    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color

    def set_ruedas(self, ruedas):
        self.ruedas = ruedas
    def get_ruedas(self):
        return self.ruedas

class coche(vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        #uso el super para traer lo anterior
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad
    def get_velocidad(self):
        return self.velocidad

    def set_cilindrada(self, cilindrada):
        self.cilindrada = cilindrada
    def get_cilindrada(self):
        return self.cilindrada

class bicicleta(vehiculo):
    def __init__(self,color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ", {}urbana/deportiva".format(self.tipo)
    
    def set_tipo(self, tipo):
        self.tipo = tipo
    def get_tipo(self):
        return self.tipo

class camioneta(vehiculo):
    def __init__(self,color,ruedas,carga):
        super().__init__(color,ruedas)
        self.carga = carga
    def __str__(self):
        return super().__str__() + ", {} kg".format(self.carga)

    def set_carga(self, carga):
        self.carga=carga
    def get_carga(self):
        return self.carga

class moto(vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        #uso el super para traer lo anterior
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad
    def get_velocidad(self):
        return self.velocidad

    def set_cilindrada(self, cilindrada):
        self.cilindrada = cilindrada
    def get_cilindrada(self):
        return self.cilindrada
