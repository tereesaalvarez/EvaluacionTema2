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
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

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