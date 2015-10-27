# BikeCommuter
An app that will automagically update my bike commuting spreadsheet.

### BikeCommute.py

usage: BikeCommute.py [-h] [-s] [-r] [-w WRITE]

Increments the "Current Commutes Completed" for the spreadsheet located at
https://docs.google.com/spreadsheets/d/1DbbcRTwytdVD9khKGJmea5R1GdH41-4vfiq1I-
UHxvs/edit?usp=sharing

optional arguments:
  -h, --help            show this help message and exit
  -s, --show            show the current number of commutes completed.
  -r, --reset           reset number of commutes completed to zero.
  -w WRITE, --write WRITE
                        write a new value to the number of commutes completed.


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
