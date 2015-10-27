# BikeCommuter
An app that will automagically update my bike commuting spreadsheet.

### BikeCommute.py

This script modifies the current number of bike commutes in the Google Sheets spreadsheet [Bike Commuting](https://docs.google.com/spreadsheets/d/1DbbcRTwytdVD9khKGJmea5R1GdH41-4vfiq1I-UHxvs/edit?usp=sharing).

* Increment current completed commutes: `python BikeCommute.py`
** Yep
* See current completed commutes: `python BikeCommute.py -s` or `python BikeCommute.py --see`
* Reset current completed commutes: `python BikeCommute.py -r` or `python BikeCommute.py --reset`
* Change current completed commutes to something explicitly: `python BikeCommute.py -w [number]` or `python BikeCommute.py --write [number]`
