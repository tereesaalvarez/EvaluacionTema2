import Ejercicio5

mi_coche = Ejercicio5.coche()
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

def inicio():
    print("ESte es el catalogo de vehiculos")
    print("1. Mostar todos los vehiculos")
    print("2. Mostrar vehiculos con 2 ruedas")
    print("3. Mostar vehiculos con 4 ruedas")
    print("4. Mostrar vehiculos con 6 ruedas")
    print("5. Salir")
    opcion= int(input("Elige una opcion: "))
    if opcion ==1:
        catalogar(mis_vehiculos)
    elif opcion ==2:
        print(catalogar_2(mis_vehiculos,2 ))
    elif opcion ==3:
        print(catalogar_2(mis_vehiculos,4 ))
    elif opcion ==4:
        print(catalogar_2(mis_vehiculos,6))
    elif opcion ==5:
        print("Saliendo")
