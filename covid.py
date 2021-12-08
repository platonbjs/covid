from numpy.lib.function_base import cov
import pandas as pd
import matplotlib.pyplot as plt
#csv_url ='https://cnecovid.isciii.es/covid19/resources/casos_hosp_uci_def_sexo_edad_provres.csv'
csv_url = './casos.csv'
covid_df = pd.read_csv(csv_url)
# covid_df_groupby_fecha = covid_df.groupby('fecha')
tabla_fecha = covid_df.groupby('fecha').sum()
tabla_fecha.plot(y=['num_casos','num_def','num_uci','num_hosp'])
plt.show()
# Calculos por rangos de edad
covid_df_groupby_grupo_edad = covid_df.groupby('grupo_edad')
# Hago recuento
tabla_grupos_edad = covid_df_groupby_grupo_edad.sum()
# Calculo porcentajes
tabla_grupos_edad['%hosp'] = (tabla_grupos_edad['num_hosp']/tabla_grupos_edad['num_casos'])*100
tabla_grupos_edad['%uci'] = (tabla_grupos_edad['num_uci']/tabla_grupos_edad['num_casos'])*100
tabla_grupos_edad['%def'] = (tabla_grupos_edad['num_def']/tabla_grupos_edad['num_casos'])*100
# Y pintamos
print(tabla_grupos_edad)
print ('--------------------------------------------------------------------------------------------')
# Asigno categorias por debajo de 50
category_dict = {'0-9': '<50',
                '10-19': '<50',
                '20-29': '<50',
                '30-39': '<50',
                '40-49': '<50',
                '50-59': '>=50',
                '60-69': '>=50',
                '70-79': '>=50',
                '80+': '>=50',
                'NC': 'NC'}
covid_df['edad'] = covid_df['grupo_edad'].map(category_dict)
# Agrupo por esta nueva categoria
covid_df_groupby_edad = covid_df.groupby('edad')
# Hago recuento
tabla_final = covid_df_groupby_edad.sum()
# Calculo porcentajes
tabla_final['%hosp'] = (tabla_final['num_hosp']/tabla_final['num_casos'])*100
tabla_final['%uci'] = (tabla_final['num_uci']/tabla_final['num_casos'])*100
tabla_final['%def'] = (tabla_final['num_def']/tabla_final['num_casos'])*100
# Y pintamos
print(tabla_final)
