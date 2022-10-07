import Ejercicio5

mi_coche = Ejercicio5.coche
mi_bicicleta = Ejercicio5.bicicleta
mi_camioneta = Ejercicio5.camioneta
mi_moto = Ejercicio5.moto
mis_vehiculos = [mi_bicicleta, mi_camioneta, mi_moto, mi_coche]

def catalogar(ListaVehiculos):
    for vehiculo in ListaVehiculos:
        print(vehiculo.__str__())

def catalogar_2(ListaVehiculos, ruedas):
    ListaVehiculos2 = []
    for vehiculo in ListaVehiculos:
        if vehiculo.get_ruedas() == ruedas:
            ListaVehiculos2.append(vehiculo)
    return f"Se encuentran {len(ListaVehiculos)}vehiculos con {ruedas} ruedas"