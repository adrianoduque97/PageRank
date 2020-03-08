import sys
import statistics
import Utils

class RandomWalker:
    nodos = None
    contadorVisitas = None
    nodoActual = None
    contadorIteracion = None
    historico = None

    def __init__(self, csvFile:str) -> None:
        super().__init__()
        self.contadorIteracion = 0
        self.nodos = Utils.readCSV(csvFile)
        self.nodos = Utils.changeFormat(self.nodos)
        self.contadorVisitas = Utils.generarContadorVisitas(self.nodos)
        self.nodoActual = Utils.getRandomNode(self.nodos)
        self.historico = [0,0]

    def walk(self):
        self.historico[self.contadorIteracion%2] = self.nodoActual
        print("Random Walker is in node: " + str(self.nodoActual+1))
        print("---- Random Walker Iteration " + str(self.contadorIteracion)+"----")
        nodoDestino = self.getDestino(self.nodos[self.nodoActual])-1

        if nodoDestino == -2:
            nodoDestino = self.teleport("Current node is dead end. ")

        if nodoDestino == self.nodoActual:
            nodoDestino = self.teleport("Current node points itself (Spidertrap). ")

        if self.checkSpiderTrap():
            nodoDestino = self.teleport("Random walker is in a spider trap. ")

        print("Random Walker is moving towards node: " + str(nodoDestino+1))
        self.nodoActual = nodoDestino
        self.contadorVisitas[nodoDestino] = self.contadorVisitas[nodoDestino] + 1
        self.contadorIteracion +=1
        print(self.contadorVisitas)

    def teleport(self, reason: str):
        print(reason)
        response = input("Press 1 for teleporting or 0 for end of program\n")
        if response == str(1):
            print("Teleporting...")
            # do teleport
            return Utils.getRandomNode(self.nodos)
        else:
            print("End of program")
            sys.exit()

    def getDestino(self,posibleDestino):
        destino = posibleDestino[0]
        if destino == -1:
            return destino
        minVisitas = self.contadorVisitas[posibleDestino[0]-1]
        for opcion in posibleDestino:
            if minVisitas > self.contadorVisitas[opcion-1]:
                minVisitas = self.contadorVisitas[opcion-1]
                destino = opcion
        return destino

    def checkSpiderTrap(self):
        if self.contadorIteracion%10 == 0 & self.contadorIteracion!=5:
            sortedVisitas = self.contadorVisitas.copy()
            sortedVisitas.sort()
            cuartil1 = sortedVisitas[4] + (.25 * (sortedVisitas[5] - sortedVisitas[4]))
            cuartil3 = sortedVisitas[14] + (.25 * (sortedVisitas[15] - sortedVisitas[14]))
            interCuartil = cuartil3 - cuartil1
            maxValue = cuartil3 + (interCuartil*3)
            nroVisitas1 = float(self.contadorVisitas[self.historico[0]])
            nroVisitas2 = float(self.contadorVisitas[self.historico[1]])
            if nroVisitas1 > maxValue and nroVisitas2 > maxValue:
                return True
        return False

    def setNodos(self, nodes):
        self.nodos = nodes

    def setContadorVisitas(self, contador):
        self.contadorVisitas = contador

    def getNodos(self, nodes):
        return self.nodos

    def getContadorVisitas(self, nodes):
        return self.contadorVisitas

    def setNodoActual(self, origen):
        self.nodoActual = origen