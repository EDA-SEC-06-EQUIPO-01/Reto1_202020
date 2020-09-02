import config as cf
import helper as h
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import quicksort as sort
import itertools as itert

# Requerimiento 3


def conocer_director(details, casting, director_name) -> dict:

    lst = [
        node["id"]
        for node in h.travel(casting)
        if node["director_name"] == director_name
    ]

    info = []
    for node in h.travel(details):
        if node["id"] in lst:
            d = {
                "id": node["id"],
                "title": node["title"],
                "vote_average": node["vote_average"],
            }
            info.append(d)

    return info


def mov_count(e):
    return float(e["vote_count"])


def mov_avera(e):
    return float(e["vote_average"])

# Requerimiento 2


def crear_ranking_peli(details, x=10, ascendent=True):
    if ascendent:
        sort.quickSort(details, h.comp_count_avg_asc)
    else:
        sort.quickSort(details, h.comp_count_avg_desc)

    ranking = [item for item in itert.islice(h.travel(details), 0, x)]

    return ranking

# Requerimiento 5


def entender_genero(details, genero):
    lista_genero = h.filter(details, "genres", genero, impl="ARRAY_LIST")
    length = lt.size(lista_genero)

    avg_vote_lst = [int(i["vote_count"]) for i in h.travel(lista_genero)]
    avg_vote = sum(avg_vote_lst) / len(avg_vote_lst)

    return lista_genero, length, avg_vote


# Requerimiento 6
def crear_ranking_genero(details, genero, retrieve=10, ascendent=True):

    dgend = h.filter(details, "genres", genero, impl="ARRAY_LIST")

    if ascendent:
        sort.quickSort(dgend, h.comp_count_avg_asc)
    else:
        sort.quickSort(dgend, h.comp_count_avg_desc)

    raw = [item for item in itert.islice(h.travel(dgend), 0, retrieve)]

    ranking = [peli["title"] for peli in raw]

    avg_vote_lst = [int(i["vote_count"]) for i in raw]
    avg_vote = sum(avg_vote_lst) / len(avg_vote_lst)

    return ranking, avg_vote

# Requerimiento 4


def conocer_actor(details, casting, actorName) -> dict:
    # Este es el requerimiento opcional.
    lista = [
        node["id"]
        for node in h.travel(casting)
        if node["actor1_name"] == actorName or node["actor2_name"] == actorName or node["actor3_name"] == actorName or node["actor4_name"] == actorName or node["actor5_name"] == actorName
    ]
    actInf = []
    for node in h.travel(details):
        if node["id"] in lista:
            ac = {
                "num": {node["id"]},
                "avg": {node["vote_average"]},
                "title": node["title"],
                "director_name": node["director_name"],
            }
            ac["numPeliculas"] = len(ac["num"])
            ac["vote_average"] = (ac["avg"]/len(ac["avg"]))
            actInf.append(ac)

    return actInf
