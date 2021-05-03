# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import networkx
import matplotlib.pyplot as plt
from sklearn import preprocessing
import community as community_louvain

# Show all lines
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

data = pd.read_csv("d9c5dbbe269cee68a13ccbe7e7eda7f3728b39d5f62cd6e9a7ad5272fd5678.csv", sep=";")
print(data)