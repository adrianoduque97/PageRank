import pandas as pd
import numpy as np
import networkx as nx
import pylab
import RandomWalker


randomWalker = RandomWalker.RandomWalker('nodos.csv')
rank=[]

def powerIteration(m,r):

    r = np.transpose(r)
    rAnterior= r
    for i in range(0, len(m)):
        r = m * rAnterior
        with np.printoptions(precision=3): print("Vector r\n"+str(r)+"\n")
        print ("sum: "+str(np.sum(r)))
        randomWalker.walk()
        if (rAnterior==r).all():
            break
        rAnterior = r
    a = open("vectorfinal.csv", 'w')
    a.write(str(r))
    print("\nPageRank END\n")


def teleport(M, b):

    M=teleportDead(M)
    mUnos = np.zeros((len(M), len(M)))
    mUnos[:] = float(1 / len(M))
    T = b * M + (1 - b) * mUnos
    with np.printoptions(precision=3):print("\nMATRIZ TELEPORTED\n"+str(T))
    return T

def teleportDead(M):

    for col in range(0,len(M)):
        if (M[:,col]==0).all():
            M[:,col] = float(1/len(M))

    return M


def plotGraph(M):
    MatT = np.transpose(M)
    G = nx.DiGraph(MatT)
    G.selfloop_edges(data=True)
    pos = nx.spring_layout(G)
    pylab.figure("Mi grafo")
    nx.draw(G, pos, with_labels=True)

    nx.draw_networkx_edges(G, pos, width=1.2, font_color="b")
    pylab.show()

if __name__ == "__main__":

    beta = 0.7
    df = pd.read_csv("test1.csv", header=None)
    Mat = np.matrix(df)
    with np.printoptions(precision=3): print("MATRIZ INICIAL \n"+ str(Mat))
    rankZero = []
    y = teleport(Mat,beta)
    for i in range(0, len(Mat)):
        rankZero.append(float(1 / len(Mat)))

    print("\nVector r inicial\n"+str(rankZero)+"\n")
    rankZero = np.matrix(rankZero)
    powerIteration(y,rankZero)

    plotGraph(np.matrix(df))







