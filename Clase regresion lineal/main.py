#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:57:32 2025

@author: Estudiante
"""
#%%


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import seaborn as sns
from sklearn.model_selection import train_test_split

#%% DATOS PARA ALTURAS


# Especifica los nuevos nombres de las columnas
columns = ['LU', 'altura', 'sexo', 'altura_madre']
datos = pd.read_csv("alturas.csv", usecols= [0,1,2,3], index_col=0, names=columns, skiprows=1)

datos = datos[datos['altura'].notna()]
datos_varones = datos[datos['sexo'] == 'M']

#%%

X = datos_varones[['altura_madre']]

alturas = datos[['altura_madre']]
Y = alturas[datos['sexo'] == 'M']
#%%

def calcularError(dato_nuevo, X, Y):
    errores = []
    k = []
    for i in range(1,21):
        neigh = KNeighborsRegressor(n_neighbors = i)
        neigh.fit(X, Y)
        neigh.predict(dato_nuevo)

        Y_pred = neigh.predict(X)
        error = mean_squared_error(Y, Y_pred)
        errores.append(error)
        k.append(i)
    return errores, k
#%%

dato_nuevo = pd.DataFrame([{'altura_madre': 156}])

errores, k = calcularError(dato_nuevo, X, Y)
plt.plot(k, errores)

#%% PRUEBA PARA KNN

mpg = pd.read_csv("auto-mpg.xls")

plt.scatter(mpg["mpg"], mpg['acceleration'])

X = mpg[['acceleration']]
Y = mpg[['mpg']]

neigh = KNeighborsRegressor(n_neighbors = 4)
neigh.fit(X, Y)

Y_pred = neigh.predict(X)

error = mean_squared_error(Y, Y_pred)

#%%
fig, ax = plt.subplots(nrows=1, ncols=2, figsize = (14,6))
errores = []
k = []
for i in range(1,21):
    neigh = KNeighborsRegressor(n_neighbors = i)
    neigh.fit(X, Y)

    Y_pred = neigh.predict(X)
    error = mean_squared_error(Y, Y_pred)
    errores.append(error)
    k.append(i)

ax[0].scatter(k,errores)
ax[0].set_xlabel("k vecinos")
ax[0].set_ylabel("MSE")
ax[0].grid()


neigh = KNeighborsRegressor(n_neighbors = 4)
neigh.fit(X, Y)

Y_pred = neigh.predict(X)

ax[1].set_title("Grafico cuando k = 4")
ax[1].scatter(X,Y)
ax[1].scatter(X,Y_pred)
ax[1].set_xlabel("acceleration")
ax[1].set_ylabel("mpg")
ax[1].grid()
#%%
fig, ax = plt.subplots(nrows=1, ncols=20, figsize = (70,6))
for i in range(1,21):
    neigh = KNeighborsRegressor(n_neighbors = i)
    neigh.fit(X, Y)

    Y_pred = neigh.predict(X)
    error = mean_squared_error(Y, Y_pred)
    errores.append(error)
    k.append(i)
    j = i - 1
    ax[j].set_title(f"Prediccion si k = {i}")
    ax[j].scatter(X,Y, label = "originales")
    ax[j].scatter(X,Y_pred, label = "predicho")
    ax[j].set_xlabel("acceleration")
    ax[j].set_ylabel("mpg")
    ax[j].grid()
    
#%%
columnas = ['mpg', 'displacement', 'acceleration','weight', 'horsepower']
sns.pairplot(mpg[columnas])
#%%

X = mpg[['acceleration', 'displacement', 'weight', 'horsepower']]
Y = mpg[['mpg']]


errores = []
k = []
for i in range(1,21):
    neigh = KNeighborsRegressor(n_neighbors = i)
    neigh.fit(X, Y)

    Y_pred = neigh.predict(X)
    error = mean_squared_error(Y, Y_pred)
    errores.append(error)
    k.append(i)
mpg = pd.read_csv("auto-mpg.xls")
plt.scatter(k,errores)
plt.xlabel("k vecinos")
plt.ylabel("MSE")
plt.grid()

# espacio

neigh = KNeighborsRegressor(n_neighbors = 4)
neigh.fit(X, Y)

Y_pred = neigh.predict(X)
error = mean_squared_error(Y, Y_pred)
    
fig, ax = plt.subplots(nrows=2, ncols=2, figsize = (14,8))
ax[0][0].set_title("Grafico cuando k = 4")
ax[0][0].scatter(X['acceleration'], Y)
ax[0][0].scatter(X['acceleration'],Y_pred)
ax[0][0].set_xlabel("acceleration")
ax[0][0].set_ylabel("mpg")
ax[0][0].grid()

ax[0][1].set_title("Grafico cuando k = 4")
ax[0][1].scatter(X['displacement'], Y)
ax[0][1].scatter(X['displacement'],Y_pred)
ax[0][1].set_xlabel("displacement")
ax[0][1].set_ylabel("mpg")
ax[0][1].grid()

ax[1][0].set_title("Grafico cuando k = 4")
ax[1][0].scatter(X['horsepower'], Y)
ax[1][0].scatter(X['horsepower'],Y_pred)
ax[1][0].set_xlabel("horsepower")
ax[1][0].set_ylabel("mpg")
ax[1][0].grid()

ax[1][1].set_title("Grafico cuando k = 4")
ax[1][1].scatter(X['weight'], Y)
ax[1][1].scatter(X['weight'],Y_pred)
ax[1][1].set_xlabel("weight")
ax[1][1].set_ylabel("mpg")
ax[1][1].grid()
#%% REESCALANDO LOS DATOS

mpg = pd.read_csv("auto-mpg.xls")

def reescalar(columna):
    maximo = columna.max()
    minimo = columna.min()
    col_n = (columna - minimo)/(maximo - minimo)
    return col_n
    
mpg_n = mpg[['mpg','acceleration', 'displacement', 'weight', 'horsepower']]
mpg_n['acceleration'] = reescalar(mpg['acceleration'])
mpg_n['weight'] = reescalar(mpg['weight'])
mpg_n['horsepower'] = reescalar(mpg['horsepower'])
mpg_n['displacement'] = reescalar(mpg['displacement'])


#X = mpg_n[['acceleration', 'displacement', 'weight', 'horsepower']]
X = mpg_n[['acceleration','weight']]
Y = mpg_n[['mpg']]
#%%
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)
errores_train = []
errores_test = []
kas = []
for k in range(1,300):
    modelo = KNeighborsRegressor(n_neighbors=k)
    modelo.fit(X_train, Y_train)
    Y_pred_train = modelo.predict(X_train)
    Y_pred_test = modelo.predict(X_test)
    error_train = mean_squared_error(Y_train, Y_pred_train)
    error_test = mean_squared_error(Y_test, Y_pred_test)
    errores_train.append(error_train)
    errores_test.append(error_test)
    kas.append(k)
    
plt.plot(kas, errores_train, label = 'train')
plt.plot(kas, errores_test, label = 'test')
plt.xlabel('Numero de vecinos k')
plt.ylabel('MSE')
plt.grid()
plt.legend()


#%%