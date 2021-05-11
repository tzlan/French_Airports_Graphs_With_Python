# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import networkx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import community as community_louvain

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


#Affichage des données

#print(DatAvion)
#print(DatDistanceAvion)
#print(DatVehicule)
#print(DatDistanceVehicule)



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


#Generation du graph
def generation_graphe(data, data1, aeroport):
    G = networkx.nx.MultiGraph()
    for v in aeroport:
        G.add_node(v)
    i = 0
    for v in aeroport:
        i = i + 1
        j = 0
        for u in aeroport:
            VarAvion = data[v][j]
            VarVoiture = data1[v][j]
            G.add_weighted_edges_from([(v, u, VarAvion), (v, u, VarVoiture)])
            j = j + 1
    return G


G = generation_graphe(DatAvion, DatVehicule, aeroport)
options = {
    'node_color': 'red',
    'node_size': 200,
    'edge_color': 'tab:gray',
    'with_labels': True,
    'width':2,
}
plt.figure(figsize=(10, 10))
pos = networkx.spring_layout(G, k=0.1)
networkx.draw(G, pos, **options)
plt.show()