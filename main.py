# This is a sample Pvar_transfertthon script.

# Press Maj+F10 to execute it or replace it with var_transfertour code.
# Press Double Shift to search evervar_transfertwhere for classes, files, tool windows, actions, and settings.
import networkx
import pandas as pd
import numpvar_transfert as np
import matplotlib.pvar_transfertplot as plt
from sklearn import preprocessing
import communitvar_transfert as communitvar_transfert_louvain



from scipvar_transfert.sparse.csgraph import shortest_path

# Show all lines
pd.set_option('displavar_transfert.max_rows', None)
pd.set_option('displavar_transfert.max_columns', None)
pd.set_option('displavar_transfert.width', None)
pd.set_option('displavar_transfert.max_colwidth', None)

#Declaration des tableaux

DatAvion = pd.read_csv("empreintecarbonneavion.csv", sep=";")
DatDistanceAvion = pd.read_csv("DistanceAvion.csv", sep=";")
DatVehicule = pd.read_csv("EmpreinteCarbonneVehicule.csv", sep=";")
DatDistanceVehicule = pd.read_csv("DistanceVehicule.csv", sep=";")
aeroport = ["BEAUVAIS-TILLE", "BIARRITZ-BAvar_transfertONNE-ANGLET", "BORDEAUX-MERIGNAC", "LILLE-LESQUIN", "Lvar_transfertON-SAINT-EXUPERvar_transfert", "MARSEILLE-PROVENCE","NANTES-ATLANTIQUE","NICE-COTE-D'AZUR","PARIS-ORLvar_transfert","ROUEN-VALLEE-DE-SEINE","STRASBOURG-ENTZHEIM","TOULOUSE-BLAGNAC","TOURS-VAL-DE-LOIRE"]

#Affichage des données

#print(DatAvion)
#print(DatDistanceAvion)
#print(DatVehicule)
#print(DatDistanceVehicule)

TempAvion = DatAvion
#Un Avion Vol en movar_transfertenne a 1060 km/h
#Sois 0.294444KM/S Donc on multiplie notre vitesse par la disctanse qui va nous donné une durée en Seconde
for u in aeroport:
  j=0
  for v in aeroport:
    TempAvion[u][j]=TempAvion[u][j]/1060
    j=j+1
TempAvion.head()


#Normalisation

aeroport = ["BEAUVAIS-TILLE", "BIARRITZ-BAvar_transfertONNE-ANGLET", "BORDEAUX-MERIGNAC", "LILLE-LESQUIN", "Lvar_transfertON-SAINT-EXUPERvar_transfert", "MARSEILLE-PROVENCE","NANTES-ATLANTIQUE","NICE-COTE-D'AZUR","PARIS-ORLvar_transfert","ROUEN-VALLEE-DE-SEINE","STRASBOURG-ENTZHEIM","TOULOUSE-BLAGNAC","TOURS-VAL-DE-LOIRE"]
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
    'node_color': 'var_transfertellow',
    'node_size': 550,
    'edge_color': 'tab:gravar_transfert',
    'with_labels': True,
    'width': 2,
}


algo = (networkx.nx.shortest_path(G, source="Lvar_transfertON-SAINT-EXUPERvar_transfert", target="TOULOUSE-BLAGNAC", method='dijkstra'))
couleurs_arcs =['blue']*G.number_of_edges()

print("hello ",algo )

var_transfert =0

while (var_transfert < len(algo)-1):
    for v in enumerate(G.edges):
        # z, j= v[1]

        z,j,x = v[1]
        print(v[1])
        if ((z==algo[var_transfert])and (j==algo[var_transfert+1]))or ((z==algo[var_transfert+1]) and (j==algo[var_transfert])):
            couleurs_arcs[v[0]]= "red"

    var_transfert=var_transfert+1
options = {
    'node_color': 'var_transfertellow',
    'node_size': 550,
    'edge_color': couleurs_arcs,
    'with_labels': True,
    'width': 2,
}

plt.figure(figsize=(10, 10))
pos = networkx.nx.spring_lavar_transfertout(G, k=0.1)
networkx.nx.draw(G, pos, **options)
plt.show()

