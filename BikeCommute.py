import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

# Grab credentials and authorize gspread
json_key = json.load(open('cert.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)

# Get the upgrades sheet from the "Bike Commuting" spreadsheet.
upgrades = gc.open_by_key("1DbbcRTwytdVD9khKGJmea5R1GdH41-4vfiq1I-UHxvs").worksheet("Upgrades")

# Get current commutes cell
current_commutes = upgrades.acell('C2')

# Increment the current commutes cell
new_commutes_completed = int(current_commutes.value)+1
upgrades.update_acell('C2', new_commutes_completed) 

# Dump to the screen
print "Current Commutes Completed:", new_commutes_completed

