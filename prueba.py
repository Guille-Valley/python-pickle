import pickle
import os


class GestorBBDD:
    def __init__(self, titulo_buscar):
        self.titulo_buscar = titulo_buscar

    def buscar_peliculas(self):
        with open(f"ficheros/{self.titulo_buscar}.pckl", 'rb') as archivo:
            data = pickle.load(archivo)
        return data

    def listar_peliculas(self):
        archivos_pckl = [
            os.path.splitext(archivo)[0]
            for archivo in os.listdir("ficheros")
            if archivo.endswith('.pckl')
        ]

        return archivos_pckl


class Pelicula():
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion
        self.guardar_pelicula()

    def guardar_pelicula(self):
        with open(f"ficheros/{self.titulo}.pckl", 'wb') as archivo:
            pickle.dump(self, archivo)

    def __str__(self):
        return f"Pelicula: {self.titulo}, Duración: {self.duracion} minutos"


lista = {
    "f01": "f01",
    "f02": "f02",
    "f03": "f03"
}

d = 100
a = 1
if a == True:
    for l in lista:
        Pelicula(l, d)

        d += 100
