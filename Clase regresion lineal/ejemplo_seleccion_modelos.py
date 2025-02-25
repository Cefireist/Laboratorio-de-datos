#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:31:28 2025

@author: mcerdeiro
"""


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold

from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error

from sklearn.neighbors import KNeighborsRegressor
from sklearn import tree

#%% cargamos los datos
df = pd.read_csv('seleccion_modelos.csv')

X = df.drop("Y", axis=1)
y = df.Y
#%% separamos entre dev y eval
X_dev, X_eval, y_dev, y_eval = train_test_split(X,y,test_size=0.1, random_state = 20)

# eval es el held out
# eval es el resto, luego hacemos el k folding sobre dev
#%% experimento

alturas = [1,2,3,4,5,6,7,8,13,21]
nsplits = 10
kf = KFold(n_splits = nsplits)

resultados = np.zeros((nsplits, len(alturas)))
# una fila por cada fold, una columna por cada modelo
for i, (train_index, test_index) in enumerate(kf.split(X_dev)):

    kf_X_train, kf_X_test = X_dev.iloc[train_index], X_dev.iloc[test_index]
    kf_y_train, kf_y_test = y_dev.iloc[train_index], y_dev.iloc[test_index]
    
    for j, hmax in enumerate(alturas):
        
        arbol = tree.DecisionTreeClassifier(max_depth = hmax)
        arbol.fit(kf_X_train, kf_y_train)
        pred = arbol.predict(kf_X_test)
        score = accuracy_score(kf_y_test,pred)
        
        resultados[i, j] = score
#%% promedio scores sobre los folds
scores_promedio = resultados.mean(axis = 0)


#%% 
for i,e in enumerate(alturas):
    print(f'Score promedio del modelo con hmax = {e}: {scores_promedio[i]:.4f}')

#%% entreno el modelo elegido en el conjunto dev entero
for i in alturas:
    depth = i
    arbol_elegido = tree.DecisionTreeClassifier(max_depth = depth)
    arbol_elegido.fit(X_dev, y_dev)
    y_pred = arbol_elegido.predict(X_dev)
    
    score_arbol_elegido_dev = accuracy_score(y_dev, y_pred)

    # pruebo el modelo elegido y entrenado en el conjunto eval
    y_pred_eval = arbol_elegido.predict(X_eval)       
    score_arbol_elegido_eval = accuracy_score(y_eval, y_pred_eval)
    
    print(f"score del arbol con depth {depth} en dev: {score_arbol_elegido_dev}")
    print(f"score del arbol con depth {depth} en held out: {score_arbol_elegido_eval}")
    print("")

#%%








#%% cargamos los datos
mpg = pd.read_csv("auto-mpg.xls")

X = mpg[['acceleration']]
y = mpg[['mpg']]

#%% separamos entre dev y eval
X_dev, X_eval, y_dev, y_eval = train_test_split(X,y,test_size=0.1, random_state = 20)

# eval es el held out
# eval es el resto, luego hacemos el k folding sobre dev
#%% experimento

k_neighbours = np.arange(1,51,1)
nsplits = 10
kf = KFold(n_splits = nsplits)

resultados = np.zeros((nsplits, len(k_neighbours)))
# una fila por cada fold, una columna por cada modelo
for i, (train_index, test_index) in enumerate(kf.split(X_dev)):

    kf_X_train, kf_X_test = X_dev.iloc[train_index], X_dev.iloc[test_index]
    kf_y_train, kf_y_test = y_dev.iloc[train_index], y_dev.iloc[test_index]
    
    for j, neighbour in enumerate(k_neighbours):
        neigh = KNeighborsRegressor(n_neighbors = neighbour)
        neigh.fit(kf_X_train, kf_y_train)

        pred = neigh.predict(kf_X_test)

        score = mean_squared_error(kf_y_test, pred)
        resultados[i, j] = score
#%% promedio scores sobre los folds
scores_promedio = resultados.mean(axis = 0)


#%% 
for i,e in enumerate(k_neighbours):
    print(f'Score promedio del modelo con k = {e}: {scores_promedio[i]:.4f}')


neigh_elegido = KNeighborsRegressor(n_neighbors = 2)
neigh_elegido.fit(X_dev, y_dev)

y_pred = neigh.predict(X_dev)

score_k_elegido_dev = mean_squared_error(y_dev, y_pred)
    
# pruebo el modelo elegido y entrenado en el conjunto eval
y_pred_eval = neigh_elegido.predict(X_eval) 
score_n_elegido_eval = mean_squared_error(y_eval, y_pred_eval) 
    
print(score_k_elegido_dev)
print("")
print(score_n_elegido_eval)
#%% entreno el modelo elegido en el conjunto dev entero

score_k_eval = []
score_k_dev = []
for i in k_neighbours:
    k = i
    neigh_elegido = KNeighborsRegressor(n_neighbors = k)
    neigh_elegido.fit(X_dev, y_dev)

    y_pred = neigh.predict(X_dev)

    score_dev = mean_squared_error(y_dev, y_pred)
        
    # pruebo el modelo elegido y entrenado en el conjunto eval (held out)
    y_pred_eval = neigh_elegido.predict(X_eval) 
    score_eval = mean_squared_error(y_eval, y_pred_eval)      
    
    score_k_eval.append(score_eval)
    score_k_dev.append(score_dev)
    print(f"score del KNn con k = {k} en dev: {score_dev}")
    print(f"score del KNn con k = {k} en held out: {score_eval}")
    print("")
plt.scatter(k_neighbours, score_k_eval, label = "en held out")
plt.scatter(k_neighbours, score_k_dev, label = "en dev")
plt.xlabel("k vecinos")
plt.ylabel("MSE")
plt.grid()
plt.legend()
#%%