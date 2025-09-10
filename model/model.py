import networkx as nx

from UI import controller
from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo=nx.Graph()

    def aggiungiNodi(self, x):
        voli = DAO.getAllFlights()
        aeroporti = DAO.getAllAirports()

        for a in aeroporti:
            idCompagnie = []
            s = 0
            for v in voli:
                if v.ORIGIN_AIRPORT_ID == a.ID or v.DESTINATION_AIRPORT_ID == a.ID:
                    if v.AIRLINE_ID not in idCompagnie:
                        idCompagnie.append(v.AIRLINE_ID)
                        s+=1

                if s >= int(x):
                    self.grafo.add_node(a)
        print(f"il numero di nodi è: {self.grafo.number_of_nodes()}")

    def aggiungiArchi(self):
        listaA1 = DAO.getAllAirports()
        listaA2 = DAO.getAllAirports()

        for a1 in listaA1:
            for a2 in listaA2:
                if a1 == a2:
                    pass
                else:
                    p=DAO.getPeso(a1.ID, a2.ID)
                    if p > 0:
                        self.grafo.add_edge(a1, a2, weight=p)
        print(f"numero di archi: {self.grafo.number_of_edges()}")

    def creaGrafo(self,x):
        self.aggiungiNodi(x)
        self.aggiungiArchi()
