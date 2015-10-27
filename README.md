# BikeCommuter
An app that will automagically update my bike commuting spreadsheet.

### BikeCommute.py

This script modifies the current number of bike commutes in the Google Sheets spreadsheet [Bike Commuting](https://docs.google.com/spreadsheets/d/1DbbcRTwytdVD9khKGJmea5R1GdH41-4vfiq1I-UHxvs/edit?usp=sharing).

* Increment current completed commutes: 
	* `python BikeCommute.py`
* See current completed commutes: 
	* `python BikeCommute.py --see`
	* `python BikeCommute.py -s`
* Change current completed commutes to something explicitly: 
	* `python BikeCommute.py --write [number]`
	* `python BikeCommute.py -w [number]` 
* Reset current completed commutes: 
	* `python BikeCommute.py --reset`
	* `python BikeCommute.py -r`
