import argparse
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--show", help="Show the current number of commutes", action="store_true")
parser.add_argument("-r", "--reset", help="Reset number of commutes to zero", action="store_true")
parser.add_argument("-w", "--write", help="Write a new value to the number of commutes", type=int)
args = parser.parse_args()

# Grab credentials and authorize gspread
json_key = json.load(open('cert.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)

# Get the upgrades sheet from the "Bike Commuting" spreadsheet.
upgrades = gc.open_by_key("1DbbcRTwytdVD9khKGJmea5R1GdH41-4vfiq1I-UHxvs").worksheet("Upgrades")

# Get current commutes cell
current_commutes = upgrades.acell('C2')

if args.show:
	# Simply dump the current commute value, don't change it.
	print "Current Commutes Completed Is:", current_commutes.value
elif args.reset:
	# Reset to zero
	upgrades.update_acell('C2', 0) 
	print "Current Commutes Reset To: 0"
elif args.write:
	# Set the commutes to inputted parameter
	upgrades.update_acell('C2', args.write) 
	print "Current Commutes Set To:", args.write
else:
	# Increment the current commutes cell
	new_commutes_completed = int(current_commutes.value)+1
	upgrades.update_acell('C2', new_commutes_completed) 
	print "Current Commutes Incremented To:", new_commutes_completed
