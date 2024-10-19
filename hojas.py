import gspread
from google.oauth2 import service_account as sa
import pandas as pd
from datetime import datetime


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

#Establezco los alcances de la API de Google Sheets y Google Drive para poder obtener acceso
# a la hoja de cálculo de Google Sheets.
KEY = 'key.json'
#Llave de autenticación de Google Cloud Platform que sera proporcionada mediante zip
#ya que me revoca los permisos si google nota se hace publico el archivo

ID = '1p8l7NPbFjC9QV9WkPpR4LrRpem8v--DmimETEQbyS-M'
#ID de la hoja de cálculo de Google Sheets con link 
#https://docs.google.com/spreadsheets/d/1p8l7NPbFjC9QV9WkPpR4LrRpem8v--DmimETEQbyS-M/edit?gid=0#gid=0 


credenciales  = sa.Credentials.from_service_account_file(KEY, scopes=scopes)

cliente = gspread.authorize(credenciales)

hoja = cliente.open_by_key(ID).sheet1
#Abro la hoja de cálculo de Google Sheets con el ID proporcionado y selecciono la primera hoja
#previamente creada con datos fictisios de empleados



df = pd.DataFrame(hoja.get_all_records())
print(df)
#visualizo la hoja de cálculo en un DataFrame de Pandas


df['Fecha de Contratación'] = pd.to_datetime(df['Fecha de Contratación'])
today = datetime.now().date()
#Convierto la columna de Fecha de Contratación a un objeto de fecha y obtengo la fecha actual
#para poder realizar operaciones con fechas

df['Años en la Empresa'] = df['Fecha de Contratación'].apply(lambda x: today.year - x.year)

df['Salario Anual'] = df['Salario Mensual'] * 12
reporte = df[['Nombre', 'Salario Mensual', 'Salario Anual', 'Años en la Empresa']]
print(reporte)
#defino las columnas a filtrar y visualizo el reporte de salarios anuales de los empleados


reporte_salarios = cliente.open_by_key(ID).add_worksheet('Reporte Salarios', rows=len(reporte), cols=len(reporte.columns))
reporte_salarios.update([reporte.columns.values.tolist()] + reporte.values.tolist())
#actualizo la hoja de cálculo con el reporte de salarios anuales de los empleados