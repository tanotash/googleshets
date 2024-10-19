import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

import pandas as pd


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'

ID = '1p8l7NPbFjC9QV9WkPpR4LrRpem8v--DmimETEQbyS-M'

credenciales  = SAC.from_json_keyfile_name(KEY, SCOPES)

cliente = gspread.authorize(credenciales)
