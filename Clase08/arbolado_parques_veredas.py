import pandas as pd 
import seaborn as sns

# leo los CSV a DataFrames
df_parques = pd.read_csv('../Data/arbolado-en-espacios-verdes.csv')
df_veredas = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')

# creo una copia filtrando "tipas" y solo las columnas diam y alt
df_tipas_parques = df_parques[df_parques['nombre_cie']=="Tipuana Tipu"][['diametro','altura_tot']].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico']=="Tipuana tipu"][['diametro_altura_pecho','altura_arbol']].copy()

# agrego una nueva columna previo al concat
amb_parq = ['parque' for i in range(df_tipas_parques.shape[0])]
amb_ver = ['vereda' for i in range(df_tipas_veredas.shape[0])]

df_tipas_parques['ambiente'] = amb_parq
df_tipas_veredas['ambiente'] = amb_ver

# cambio los encabezados para que los compartan
headers = ['diam', 'alt', 'ambiente']
df_tipas_parques.columns = headers
df_tipas_veredas.columns = headers

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques], ignore_index=True)

# ploteo
df_tipas.boxplot('diam', by = 'ambiente')
df_tipas.boxplot('alt', by = 'ambiente')