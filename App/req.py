import config as cf
import helper
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import quicksort as sort


def conocer_director(details, casting, director_name) -> dict:

    lst = [
        node["id"]
        for node in helper.forward_travel(casting)
        if node["director_name"] == director_name
    ]

    info = []
    for node in helper.forward_travel(details):
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


def crear_ranking_peli(details, x=10, ascendent=True) -> tuple:
    rank_co = list(helper.forward_travel(details))
    rank_co.sort(key=mov_count, reverse=ascendent)

    rank_av = list(helper.forward_travel(details))
    rank_av.sort(key=mov_avera, reverse=ascendent)

    return (rank_co[:x], rank_av[:x])


def crear_ranking_genero(details, genero, retrieve=10, ascendent=True):
    sort.quickSort(details, helper.comp_count_avg_asc)

    print("D")