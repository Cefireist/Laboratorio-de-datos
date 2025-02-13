#!/usr/bin/env python3   []
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:02:34 2025

@author: Estudiante
"""
# %% IMPORTO LIBRERIAS
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ruta_carpeta= "/home/Estudiante/Descargas/clase exploracion datos/"
#%% · LEO LOS DATOS  Y GRAFICO

data_vinos = pd.read_csv(ruta_carpeta + "wine.csv", sep =";")

fig, ax = plt.subplots()
plt.rcParams['font.family'] = 'sans-serif'
ax.scatter(data = data_vinos, x = 'fixed acidity', y = 'citric acid', s = 8, color = "darkblue")

#%% GRAFICO DE SCATTER
data_arboles = pd.read_csv(ruta_carpeta + "arbolado-en-espacios-verdes.csv", index_col = 2)
frecuencias_aparicion = data_arboles['id_especie'].value_counts()
top_30 = frecuencias_aparicion.head(30).index.tolist()
arboles_mas_frecuentes = data_arboles[data_arboles['id_especie'].isin(top_30)]


fig, ax = plt.subplots()
ax.scatter(data = arboles_mas_frecuentes, x = 'altura_tot', y = 'diametro', s = 8, color = "red")
ax.set_title("longitud vs latitud")
ax.set_xlabel("longitud")
ax.set_ylabel("latitud")

#%% GRAFICO DE BURBUJAS

data_vinos = pd.read_csv(ruta_carpeta + "wine.csv", sep =";")

fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'

tamano_burbuja = 8
ax.scatter(data = data_vinos, x = 'fixed acidity', y = 'citric acid',
           s = data_vinos["residual sugar"]*tamano_burbuja, color = "green")

ax.set_title("Cantidad de azucar segun acidez y acido citrico")
ax.set_xlabel("Fixed acidity [ud]")
ax.set_ylabel("Citric acid [ud]")
ax.grid(alpha = 0.7)


#%% GRAFICO DE TORTAS
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'

data_vinos = pd.read_csv(ruta_carpeta + "wine.csv", sep =";")

data_vinos['type'].value_counts().plot(kind='pie',ax = ax,
                                       autopct = '%1.1f%%',
                                       colors = ["red", "blue"],
                                       startangle=90,
                                       shadow = True,
                                       explode = (0.1,0),
                                       legend = False
                                       )

ax.set_title("Distribucion de tipos de vino")
ax.set_ylabel("")
# ['#66b3ff', '#ff9999']

#%%

data_vinos = pd.read_csv(ruta_carpeta + "wine.csv", sep =";")

fig, ax = plt.subplots()
ax.scatter(data = data_vinos, x = 'sulphates', y = 'pH', s = 8, color = "red")
ax.set_xlabel("Sulphates")
ax.set_ylabel("pH")



#%%

cheetahRegion = pd.read_csv(ruta_carpeta + "cheetahRegion.csv")
fig, ax = plt.subplots()
ax.bar(data= cheetahRegion, x = 'Anio', height = 'Ventas')

ax.set_title("Venta de la compañia cheetah sports")
ax.set_xlabel("año")
ax.set_ylabel("ventas (millones de $)")
ax.set_xlim(0,11)
ax.set_ylim(0,250)

ax.set_xticks(range(1,11,1))
ax.set_yticks([])
ax.bar_label(ax.containers[0], fontsize = 8)

#%%

cheetahRegion = pd.read_csv(ruta_carpeta + "cheetahRegion.csv")
fig, ax = plt.subplots()
cheetagRegion.plot(data= cheetahRegion, x = 'Anio', y = ['regionEste', 'regionOeste'], kind = 'bar',
        label = ["region Este", "region Oeste"], ax = ax )



#%%

gaseosas = pd.read_csv(ruta_carpeta + "gaseosas.csv")

fig, ax = plt.subplots()
gaseosas['Compras_gaseosas'].value_counts(normalize=True).plot.bar(ax=ax)

ax.set_title("Frecuencia Venta de Gaseosas")
ax.set_xlabel("Marcas de gaseosas")
ax.set_yticks([])
ax.bar_label(ax.containers[0], fontsize=8)
ax.tick_params(axis = "x", labelrotation=0)


#%%
ageAtDeath = pd.read_csv(ruta_carpeta + "ageAtDeath.csv" )

fig, ax = plt.subplots()
sns.histplot(data = ageAtDeath['AgeAtDeath'], bins = 26)

#%%
import duckdb as dd
tips = pd.read_csv(ruta_carpeta + "tips.csv" )

propina_hombres = dd.sql(
    """
    SELECT COUNT(tip) AS suma_hombre, day, sex
    FROM tips
    WHERE sex = 'Male'
    GROUP BY day, sex
    """
    ).df()
propina_mujeres = dd.sql(
    """
    SELECT COUNT(tip) AS suma_mujer, day, sex
    FROM tips
    WHERE sex = 'Female'
    GROUP BY day, sex
    """
    ).df()
propinas = dd.sql(
    """
    SELECT pj.suma_mujer, pj.day, ph.suma_hombre
    FROM propina_hombres AS ph
    INNER JOIN propina_mujeres AS pj
    ON pj.day = ph.day
    """
    ).df()

fig, ax = plt.subplots()
propinas.plot(x = "day", y = ['suma_hombre','suma_mujer'], kind = 'bar',
              label=['Male', 'female'],order = ['Thur','Fri','Sat','Sun'], ax = ax)
ax.set_ylabel("Sum of tips", fontsize = 14)
ax.set_xlabel("Day",fontsize = 14)
ax.set_title("Sum of tips by day and sex")

#sns.histplot(data = tips, x = 'tip', hue = tips['sex'], alpha = 0.5)

#sns.histplot(data = propina_mujeres['tip'], color = "red", bins = 7, label = "Mujeres", alpha = 0.5)
#sns.histplot(data = propina_hombres['tip'], color = "blue", bins = 7, label = "hombres", alpha = 0.5)
ax.legend()
#%%

import seaborn as sns
import matplotlib.pyplot as plt

# Crear el boxplot
ax = sns.boxplot(x="day", y="tip", hue="sex", data=tips, order=['Thur', 'Fri', 'Sat', 'Sun'], palette={"Female": "pink", "Male": "lightblue"})

# Configurar el título y las etiquetas de los ejes
ax.set_title('Propinas')
ax.set_xlabel('Día de la Semana')
ax.set_ylabel('Valor de Propina ($)')
ax.set_ylim(0, 12)

# Configurar la leyenda
ax.legend(title="Sexo")

# Configurar las etiquetas del eje X
ax.set_xticklabels(['Jueves', 'Viernes', 'Sábado', 'Domingo'])

# Mostrar el gráfico
plt.show()


#%%

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Crear el violinplot
ax = sns.violinplot(x="sex", y="tip", data=tips, palette={"Female": "pink", "Male": "lightblue"})

# Configurar el título y las etiquetas de los ejes
ax.set_title('Propinas')
ax.set_xlabel('Sexo')
ax.set_ylabel('Valor de Propina ($)')

# Formatear el eje Y para mostrar valores en dólares
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("${x:,.2f}"))

# Establecer los límites del eje Y
ax.set_ylim(0, 12)

# Configurar las etiquetas del eje X
ax.set_xticklabels(['Femenino', 'Masculino'])

# Mostrar el gráfico
plt.show()

#%%










#%%



