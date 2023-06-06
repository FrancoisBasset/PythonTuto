"""File testing functions"""

import json
import pickle
from classes.distro import Distro

def test():
    """First test"""
    with open("workfile", "a", encoding="utf-8") as f:
        while True:
            i = input("Distribution : ")
            if i == "":
                break
            f.write(i + "\n")

        value = ("the answer", 42)
        f.write(str(value) + "\n")

    with open("workfile", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            print(i + 1, line, end="")

def test2():
    """Second test"""
    with open("distros", "a", encoding="utf-8") as distro:
        while True:
            i = input("Distro : ")
            if i == "":
                break

            with open("index", "a", encoding="utf-8") as index:
                index.write(str(len(i)) + ",")

            distro.write(i)

    with open("distros", "r", encoding="utf-8") as distro:
        distros = distro.read()

        with open("index", "r", encoding="utf-8") as index:
            indexes = index.read().split(",")
            del indexes[-1]
            start = 0

            for length in indexes:
                end = start + int(length)
                #print(distros[start:end])
                start = end

            distro.seek(0)
            for i in indexes:
                print(distro.read(int(i)))

def test3():
    """Third test"""
    try:
        with open("distros", "r", encoding="utf-8") as distros_file:
            distros = json.load(distros_file)
    except FileNotFoundError:
        distros = []

    with open("distros", "a+", encoding="utf-8") as distros_file:
        while True:
            print("\n\n1 Lister les distros")
            print("2 Ajouter une distro")
            print("3 Quitter")
            choice = input("Choix : ")

            match choice:
                case "1":
                    print("Liste des distros :")
                    for distro in distros:
                        print(f"[{distro}]")
                case "2":
                    distro = input("Nom de la distro : ")
                    distros.append(distro)
                    distros.sort()
                    distros_file.truncate(0)
                    json.dump(distros, distros_file)
                case "3":
                    break

def test_pickle_dump():
    distros = [
        Distro("debian", "debian", "12"),
        Distro("ubuntu", "debian", "23.04"),
        Distro("fedora", "red hat", 38),
        Distro("mint", "ubuntu", "21.1"),
        Distro("arch", "arch", "rolling"),
        Distro("slackware", "slackware", 15)
    ]
    
    for distro in distros:
        with open(distro.name, "wb") as f:
            pickle.dump(distro, f)

def test_pickle_load():
    distros = ["debian", "ubuntu", "fedora", "mint", "arch", "slackware"]

    for distro in distros:
        with open(distro, "rb") as f:
            print(pickle.load(f))
