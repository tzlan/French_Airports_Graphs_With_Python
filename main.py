# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import networkx as nx
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

print(DatAvion)
print(DatDistanceAvion)
print(DatVehicule)
print(DatDistanceVehicule)



#Normalisation

