__author__ = 'jordiblanchsalgado'

class App2():
    def __init__(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre


    def sumarDescarga(self,nombre):
        varNombre = nombre

        with open('apps.txt',mode='r',encoding='utf-8')as archivo:
            contenido = ""
            contModificad = ""

            for linia in archivo:
                nombre,proveedor,fecha_publi,precio,num_descargas,num_puntuaciones,puntuacion,num_comentarios = linia.split(',',7)
                num_comentarios = num_comentarios.strip("\n")

                if varNombre != nombre:
                    contenido = contenido + (nombre+","+proveedor+","+fecha_publi+","+str(precio)+","+str(num_descargas)+","+str(num_puntuaciones)+","+str(puntuacion)+","+str(num_comentarios)+"\n")

                else:
                    nuevo_num_descargas = int(num_descargas) + 1
                    contModificad = (nombre+","+proveedor+","+fecha_publi+","+str(precio)+","+str(nuevo_num_descargas)+","+str(num_puntuaciones)+","+str(puntuacion)+","+str(num_comentarios)+"\n")

            contTotal = contenido+contModificad

        with open('apps.txt',mode='w',encoding='utf-8')as archivo:
            archivo.write(contTotal)
            print("")
            print("---DESCARGA SUMADA---")
            print("")

    def crearApp(self,nombre):
        varNombre = nombre
        with open('apps.txt',mode='r',encoding='utf-8')as archivo:
            encontrado = False
            for linia in archivo:
                nombre,proveedor,fecha_publi,precio,num_descargas,num_puntuaciones,puntuacion,num_comentarios = linia.split(',',7)
                num_comentarios = num_comentarios.strip("\n")
                if varNombre == nombre:
                    encontrado = True
                    app = App2(nombre)

            if(encontrado == False):
                print("No encontrada esta APP")
        return app

    def sumarComentari(self,nombre):
        varNombre = nombre

        with open('apps.txt',mode='r',encoding='utf-8')as archivo:
            contenido = ""
            contModificad = ""

            for linia in archivo:
                nombre,proveedor,fecha_publi,precio,num_descargas,num_puntuaciones,puntuacion,num_comentarios = linia.split(',',7)
                num_comentarios = num_comentarios.strip("\n")

                if varNombre != nombre:
                    contenido = contenido + (nombre+","+proveedor+","+fecha_publi+","+str(precio)+","+str(num_descargas)+","+str(num_puntuaciones)+","+str(puntuacion)+","+str(num_comentarios)+"\n")

                else:
                    nuevo_num_comentarios = int(num_comentarios) + 1
                    contModificad = (nombre+","+proveedor+","+fecha_publi+","+str(precio)+","+str(num_descargas)+","+str(num_puntuaciones)+","+str(puntuacion)+","+str(nuevo_num_comentarios)+"\n")

            contTotal = contenido+contModificad

        with open('apps.txt',mode='w',encoding='utf-8')as archivo:
            archivo.write(contTotal)
            print("")
            print("---COMENTARIO SUMADA---")
            print("")

