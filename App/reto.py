"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
from time import process_time
from DataStructures import liststructure as lt
from DataStructures import listiterator as it
from ADT import list as lt
import helper as h
import req
import csv
import sys

movies_dir = "themoviesdb/"
details = movies_dir + "SmallMoviesDetailsCleaned.csv"
casting = movies_dir + "MoviesCastingRaw-small.csv"


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Conocer las buenas películas")
    print("3- Ranking de peliculas")
    print("4- Conocer un director")
    print("5- Conocer un actor")
    print("6- Entender un genero")
    print("7- Crear ranking")
    print("0- Salir")


def compareRecordIds(recordA, recordB):
    if int(recordA["id"]) == int(recordB["id"]):
        return 0
    elif int(recordA["id"]) > int(recordB["id"]):
        return 1
    return -1


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None
    """

    while True:
        printMenu()  # imprimir el menu de opciones en consola
        # leer opción ingresada
        inputs = input("Seleccione una opción para continuar\n")
        if len(inputs) > 0:

            if int(inputs[0]) == 1:  # opcion 1
                lista_details = h.loadCSVFile(
                    details, impl="ARRAY_LIST", cmpfunction=None
                )
                lista_casting = h.loadCSVFile(
                    casting, impl="ARRAY_LIST", cmpfunction=None
                )

            elif int(inputs[0]) == 2:  # opcion 2
                director = input("Ingrese el nombre del director\n")
                buenaspelis = req.buenasPeliculas(
                    director, lista_casting, lista_details
                )
                print(
                    f"Se encontraron {buenaspelis[0]} buenas películas con los parámetros dados."
                )
                print(
                    f"El promedio de la votación por dichas películas es de {buenaspelis[1]}."
                )

            elif int(inputs[0]) == 3:  # opcion 3
                num = int(input("Cuántas entradas quiere para el ranking? \n"))
                asc = bool(
                    int(
                        input(
                            "Digite:\n"
                            + "1 si desea se muestren las peliculas mejor calificadas\n"
                            + "0 si desea que se muestren las peor calificadas\n"
                        )
                    )
                )
                try:
                    ranking = req.crear_ranking_peli(lista_details, num, asc)
                    print("El ranking de películas es:\n")
                    cont = 0
                    pal = "ascendentemente" if asc else "descendentemente"
                    print(f"Ranking ordenado por votos {pal}:\n")
                    for i in ranking:
                        cont += 1
                        spc = 25 - len(i["title"])
                        print(
                            f"{cont}. {i['title']}{' '*spc} - vote count: {i['vote_count']} - vote average: {i['vote_average']}"
                        )
                    print()
                except UnboundLocalError:
                    print("\n" * 10 + "!!!\n\nPrimero carga los datos\n\n!!!")

            elif int(inputs[0]) == 5:  # opcion 5
                director = input("Ingrese el nombre del director\n")
                try:
                    information = req.conocer_director(
                        lista_details, lista_casting, director
                    )
                    for d in information:
                        print(
                            "id:",
                            d["id"],
                            " - " "title:",
                            d["title"],
                            " - ",
                            "vote average:",
                            d["vote_average"],
                        )
                except UnboundLocalError:
                    print("\n" * 10 + "!!!\n\nPrimero carga los datos\n\n!!!")

            elif int(inputs[0]) == 4:  # opcion 4
                name = input("Ingrese el nombre del actor\n")
                try:
                    inf = req.conocer_actor(lista_details, lista_casting, name)
                    for ac in inf:
                        print(
                            (ac["title"])
                            + ","
                            + (ac["numPeliculas"])
                            + ","
                            + (ac["vote_average"])
                            + ","
                            + (ac["director_name"])
                        )
                except UnboundLocalError:
                    print("\n" * 10 + "!!!\n\nPrimero carga los datos\n\n!!!")

            elif int(inputs[0]) == 6:  # opcion 6
                genero = input("Digite el género sobre el cuál desea trabajar:\n")
                try:
                    lista, longitud, promedio = req.entender_genero(
                        lista_details, genero
                    )
                    cont = 0
                    print("Las películas que tienen dicho género son\n")
                    for i in h.travel(lista, parameter="title"):
                        cont += 1
                        print(f"{cont}. {i}")
                    print(f"En total son {longitud} películas.")
                    print(
                        f"El voto promedio para las películas de género {genero} es {promedio}"
                    )
                    print()

                except UnboundLocalError:
                    print("\n" * 10 + "!!!\n\nPrimero carga los datos\n\n!!!")

            elif int(inputs[0]) == 6:  # opcion 7
                print("Que genero quiere para crear el ranking? ")
                g = input()
                print("cuantas entradas quiere? ")
                e = int(input())
                print("De peor a mejor (1) - De mejor a peor (2) ? ")
                s = int(input())

                if s == 1:
                    s = True
                else:
                    s = False

                try:
                    ranking, avg_v = req.crear_ranking_genero(lista_details, g, e, s)

                    if s == 1:
                        st = "mejores"
                    else:
                        st = "peores"

                    print(f"Las {e} {st} peliculas del genero {g} son:")
                    for c, i in enumerate(ranking):
                        print(f"N{c+1}. {i}")

                    print(f"Con promedio de votos {avg_v}")
                except UnboundLocalError:
                    print("\n" * 10 + "!!!\n\nPrimero carga los datos\n\n!!!")
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()
