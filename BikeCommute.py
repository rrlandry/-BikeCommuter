import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('cert.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

# Open a worksheet from spreadsheet with one shot
wks = gc.open("TestSheet").sheet1

cell = wks.acell('B2')
wks.update_acell('B2', int(cell.value)+1)
