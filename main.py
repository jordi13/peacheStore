__author__ = 'jordiblanchsalgado'

import App2

def menu():
    print("BIENVENIDO A LA PEACHSTORE")
    print("1-. Añadir nueva app")
    print("2-. Sumar una descarga")
    print("3-. Sumar un comentario")
    print("4-. Modificar los datos de identificacion de una APP")
    print("5-. Mostrar lista Apps ordenadas (Gratis/Pago)")
    print("6-. Calcular el num de estrellas de una APP")
    print("7-. Calcular el importe total ingresado hasta el momento (solo de pago)")
    print("8-. Listar Apps de un mismo proveedor ")
    print("9-. SALIR")

eleccion = 0
menu()
while eleccion != 9:
    eleccion = int(input())

    #AÑADIR NUEVA APP
    if eleccion == 1:
        print("")
        print("AÑADIR NUEVA APP: ")
        print("")
        print("Nombre :")
        nombreApp = str(input())
        print("Proveedor :")
        proveedor = str(input())
        print("Fecha de publicacion :")
        fecha = str(input())
        print("Precio :")
        precio = float(input())
        num_descargas = "0"
        num_puntuaciones = "0"
        puntuacion = "0"
        num_comentarios = "0"

        #Escribir apps.txt
        with open('apps.txt', mode='a', encoding='utf-8')as archivo:
                archivo.write(nombreApp+","+proveedor+","+fecha+","+str(precio)+","+num_descargas+","+num_puntuaciones+","+puntuacion+","+num_comentarios+"\n")
        print("")
        print("App añadida")
        print("")
        menu()

    #SUMAR UNA DESCARGA
    if eleccion == 2:
        print("Itroduce el nombre de la app ")
        nombre = str(input())
        apps = App2.App2(nombre)
        apps.crearApp(nombre)
        apps.sumarDescarga(nombre)
        menu()
    if eleccion == 3:
        print("Introduce el nombre de la app ")
        nombre = str(input())
        apps = App2.App2(nombre)
        apps.crearApp(nombre)
        apps.sumarComentari(nombre)
        menu()