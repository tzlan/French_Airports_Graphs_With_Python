# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import networkx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import community as community_louvain



from scipy.sparse.csgraph import shortest_path

# Show all lines
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#Declaration des tableaux

DatAvion = pd.read_csv("empreintecarbonneavion.csv", sep=";")
DatDistanceAvion = pd.read_csv("DistanceAvion.csv", sep=";")
DatVehicule = pd.read_csv("EmpreinteCarbonneVehicule.csv", sep=";")
DatDistanceVehicule = pd.read_csv("DistanceVehicule.csv", sep=";")
aeroport = ["BEAUVAIS-TILLE", "BIARRITZ-BAYONNE-ANGLET", "BORDEAUX-MERIGNAC", "LILLE-LESQUIN", "LYON-SAINT-EXUPERY", "MARSEILLE-PROVENCE","NANTES-ATLANTIQUE","NICE-COTE-D'AZUR","PARIS-ORLY","ROUEN-VALLEE-DE-SEINE","STRASBOURG-ENTZHEIM","TOULOUSE-BLAGNAC","TOURS-VAL-DE-LOIRE"]

#Affichage des données

#print(DatAvion)
#print(DatDistanceAvion)
#print(DatVehicule)
#print(DatDistanceVehicule)

TempAvion = DatAvion
#Un Avion Vol en moyenne a 1060 km/h
#Sois 0.294444KM/S Donc on multiplie notre vitesse par la disctanse qui va nous donné une durée en Seconde
for u in aeroport:
  j=0
  for v in aeroport:
    TempAvion[u][j]=TempAvion[u][j]/1060
    j=j+1
TempAvion.head()


#Normalisation

aeroport = ["BEAUVAIS-TILLE", "BIARRITZ-BAYONNE-ANGLET", "BORDEAUX-MERIGNAC", "LILLE-LESQUIN", "LYON-SAINT-EXUPERY", "MARSEILLE-PROVENCE","NANTES-ATLANTIQUE","NICE-COTE-D'AZUR","PARIS-ORLY","ROUEN-VALLEE-DE-SEINE","STRASBOURG-ENTZHEIM","TOULOUSE-BLAGNAC","TOURS-VAL-DE-LOIRE"]
for v in aeroport :
  DatDistanceAvion[v] = DatDistanceAvion[v]/100
for v in aeroport :
  DatDistanceVehicule[v] = DatDistanceVehicule[v]/100
for v in aeroport :
  DatAvion[v] = DatAvion[v]/100
for v in aeroport :
  DatVehicule[v] = DatVehicule[v]/100
print(DatAvion["BEAUVAIS-TILLE"][0])


def generation_graphe(data, data1, aeroport):
    G = networkx.nx.MultiGraph()
    for v in aeroport:
        G.add_node(v)
        j = 0
    for v in aeroport:
        j = 0
        for u in aeroport:
            VarAvion = data[v][j]
            VarVoiture = data1[v][j]
            G.add_weighted_edges_from([(v, u, VarAvion), (v, u, VarVoiture)])
            j = j + 1
    return G


G = generation_graphe(DatAvion, DatVehicule, aeroport)
for e in enumerate(G.edges):
    print(e)
options = {
    'node_color': 'yellow',
    'node_size': 550,
    'edge_color': 'tab:gray',
    'with_labels': True,
    'width': 2,
}


algo = (networkx.nx.shortest_path(G, source="LYON-SAINT-EXUPERY", target="TOULOUSE-BLAGNAC", method='dijkstra'))
couleurs_edge =['blue']*G.number_of_edges()

print("hello ",algo )

y =0

while (y < len(algo)-1):
    for v in enumerate(G.edges):
        # z, j= v[1]

        z,j,x = v[1]
        print(v[1])
        if ((z==algo[y])and (j==algo[y+1]))or ((z==algo[y+1]) and (j==algo[y])):
            couleurs_edge[v[0]]= "red"

    y=y+1
options = {
    'node_color': 'yellow',
    'node_size': 550,
    'edge_color': couleurs_edge,
    'with_labels': True,
    'width': 2,
}

plt.figure(figsize=(10, 10))
pos = networkx.nx.spring_layout(G, k=0.1)
networkx.nx.draw(G, pos, **options)
plt.show()

