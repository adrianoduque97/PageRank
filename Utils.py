import random
import numpy as np
import pandas as pd

#reads csv returns dictionary
def readCSV(fileName: str):
    matriz = pd.read_csv(fileName,header=None)
    return matriz.to_dict('records')

# returns random number from 0 to len(nodo)
def getRandomNode(nodes):
    nroNodos = len(nodes) - 1
    nodo = random.randint(0,nroNodos)
    return nodo

# list of dict to list of lists
def changeFormat(nodos: list):
    newList = []
    for val in nodos:
        newVal = dictToList(val)
        newVal = removeNANFromList(newVal)
        newList.append(newVal)
    return newList

def removeNANFromList(nodosVecinos: list):
    cleanList = []
    for i in nodosVecinos:
        if not np.isnan(i):
            cleanList.append(int(i))
    return cleanList

# transfor dict to list
def dictToList(diccionario: dict):
    listValues = [v for v in diccionario.values()]
    return listValues

def generarContadorVisitas(nodos):
    contadorVisitas = []
    for nodo in nodos:
        contadorVisitas.append(0)
    return contadorVisitas
