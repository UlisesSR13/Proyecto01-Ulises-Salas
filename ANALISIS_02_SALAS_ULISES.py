# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:11:45 2022

@author: Ulises Salas
"""
import pandas as pd

""" PUNTO 1:  Las 10 rutas comerciales mas usadas


"""

#Generar un data frame 

df= pd.read_csv("C:/Users/1046581/Documents/PHYTON CURSOS SANTANDER/data-science-proyecto2-master/synergy_logistics_database.csv")

df["Rutas"]= + df["origin"]+ "-" + df["destination"]

#Agrupar los datos por las categorias que necesitamos
grouped= df.groupby("Rutas").agg({
    
   
    "register_id": 'count',
     "total_value": 'sum',
    })

#Ordenar los datos por el id, dado que este nos indica el numero de veces de la ruta
rutas= grouped.sort_values(by= ["register_id"], ascending=[False]) 

#Obtenemos las rutas mas usadas
print(f" Las 10 RUTAS MAS USADAS SON : " , rutas[:10])


#Para las ruta mas redituables usamos la categoria de total value
rutas_mas_redituables = grouped.sort_values(by= ["total_value"], ascending= [False])
#Obtenemos las rutas mas redituables 
print(f" LAS 10 RUTAS MAS REDITUABLES SON :", rutas_mas_redituables [:10])



""" PUNTO 2:  Medio de transporte mas utlizado: 3 medios mas importantes, considerando el valor
de importaciones y exportaciones, medio de transporte a reducir

"""
#Agrupamos ahora por la categoria de transport mode.
grouped= df.groupby("transport_mode").agg({
    
   
    "register_id": 'count',
     "total_value": 'sum',
    })

#Ordenamos en una nueva variable por total value de cada medio de transporte
modo=  grouped.sort_values(by= ["total_value"], ascending=[False]) 

#Los tres medios de transporte mas usados y por valor total

print(f" Los 3 medios de transporte mas usados por valor total son : " , modo[:4])




""" PUNTO 3 : Valor total de importaciones y exportaciones. Paises que generan el 80% del
valor de las exportaciones e importaciones 
"""
#Ordenamos por categoria de Origen para obtener los paises exportadores
grouped= df.groupby("origin").agg({
    
   
    
     "total_value": 'sum',
    })

#Generamos el valor total de todas las operaciones 
valor_total= grouped["total_value"].sum()

#Ordenamos a los paises mas exportadores 
mas_exportan=  grouped.sort_values(by= ["total_value"], ascending=[False])
#Creamos una nueva columna para obtener el procentajes de cada uno
mas_exportan["porcentaje"]= (mas_exportan["total_value"]/valor_total)*100
#Genermaos una variable con la suma acumulada de los procentajes
colcumsum= mas_exportan.cumsum()["porcentaje"]
#Agregamos esos valores a la nueva columna, Porcentaje acum
mas_exportan["Porcentaje acum"]=colcumsum
#Generamos un listado de los paises con los procentajes acumulados dentro del 80% 
top_80= mas_exportan[mas_exportan["Porcentaje acum"] <80]

#Obtenemos la lista de los paises con una participacion aproximada del 80%
print("Paises exportadores que representan aproximadamente el 80% del valor total de ganancias:", top_80)


""" PAISES IMPORTADORES 

"""
#Agrupamos ahora por detino, para paises importadores 
grouped2= df.groupby("destination").agg({
    
   

     "total_value": 'sum',
    })

valor_total= grouped2["total_value"].sum()

#Ordenamos nuevamente de mayor a menor
mas_importan=  grouped2.sort_values(by= ["total_value"], ascending=[False])
#Generamos una nueva columna y variable para sus respectivos porcentajes

mas_importan["porcentaje"]= (mas_importan["total_value"]/valor_total)*100
colacumsum= mas_importan.cumsum()["porcentaje"]
mas_importan["porcentaje acumulado"]= colacumsum
#Obtenemos los paises cuya participacion es aproximada al 80%
top_80_import= mas_importan[mas_importan["porcentaje acumulado"] <80]
#Obtenemos a los paises importadores con una participación aproximada del 80%
print("Paises importadores que representan aproximadamente el  80% del valor total de valor", top_80_import)













