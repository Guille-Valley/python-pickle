import pickle
import os

DIRECTORIO = "//192.168.4.6/Users/CTA/Desktop/Fila 02/peliculas_02/"


class GestorBBDD:
    # def __init__(self):

    def guardar_pelicula(self, obj):
        try:
            with open(f"{DIRECTORIO}{obj.titulo}.pckl", 'wb') as archivo:
                pickle.dump(obj, archivo)
        except Exception as e:
            print(e)

    def buscar_peliculas(self, titulo_buscar):
        try:
            with open(f"{DIRECTORIO}{titulo_buscar}.pckl", 'rb') as archivo:
                data = pickle.load(archivo)
            return data
        except Exception as e:
            print(e)

    def listar_peliculas(self):
        try:
            archivos_pckl = [
                os.path.splitext(archivo)[0]
                for archivo in os.listdir(DIRECTORIO)
                if archivo.endswith('.pckl')
            ]

            return archivos_pckl
        except Exception as e:
            print(e)


class Pelicula():
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    def __str__(self):
        return f"Pelicula: {self.titulo}, Duración: {self.duracion} minutos"


while (True):
    op = int(input("(1) para crear pelicula, (2) para Leer, (3) para salir: "))
    if (op == 1):
        nombre = input("Introduce nombre de la pelicula: ")
        duracion = int(input("Introduce duracion de la pelicula: "))
        GestorBBDD().guardar_pelicula(Pelicula(nombre, duracion))
    elif (op == 2):
        # Pelicula(nombre, duracion)
        print(GestorBBDD().listar_peliculas())
        print("Dime la pelicula de la que quieras saber su duracion")
        buscar_pelicula = input("Introduce la pelicula a buscar: ")
        print(GestorBBDD().buscar_peliculas(buscar_pelicula))
    elif (op == 3):
        break
