import gspread
from oauth2client.service_account import ServiceAccountCredentials

key_path = 'C:/Projects/Held Orders Project/held-orders-project-1f20881965f6.json'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

scope_str = ' '.join(scope)
credentials = ServiceAccountCredentials.from_json_keyfile_name(key_path, scope_str)

