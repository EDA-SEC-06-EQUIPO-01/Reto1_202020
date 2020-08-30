import config as cf
import helper as h
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import quicksort as sort
import itertools as itert


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


def crear_ranking_peli(details, x=10, ascendent=True) -> tuple:
    rank_co = list(h.travel(details))
    rank_co.sort(key=mov_count, reverse=ascendent)

    rank_av = list(h.travel(details))
    rank_av.sort(key=mov_avera, reverse=ascendent)

    return (rank_co[:x], rank_av[:x])


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


# "genres":'Music|Comedy|Action|Crime'
