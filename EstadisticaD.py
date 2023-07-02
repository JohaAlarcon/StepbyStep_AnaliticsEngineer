import pandas as pd

#Crear un dataframe de ejemplo con edades
edades = pd.DataFrame({'edad': [25,30, 35, 40, 45, 50, 55, 60, 65, 70]})

#   Calcular la media
media = edades['edad'].mean()
print('Media: ',media)

#   Calcular la mediana
mediana = edades['edad'].median()
print('Mediana: ',mediana)

#   Calcular la desviacion standar
std = edades['edad'].std()
print('Desviacion estandar: ',std)

#   Calcular rango de edades
rango = edades['edad'].max() - edades['edad'].min()
print('Rango ',rango)           


#Crear un dataframe de ejemplo con salarios

salarios = pd.DataFrame ({'salario': [2000,2500,3000,3500,4000,4500]})

#   Calcular la media
media1 = salarios['salario'].mean()
print('Media: ',media1)

#   Calcular la mediana
mediana1 = salarios['salario'].median()
print('Mediana: ',mediana1)

#   Calcular la desviacion standar
std1 = salarios['salario'].std()
print('Desviacion estandar: ',std1)

#   Calcular rango de edades
rango1 = salarios['salario'].max() - salarios['salario'].min()
print('Rango ',rango1)   