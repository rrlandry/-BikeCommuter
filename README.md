# BikeCommuter
An app that will automagically update my bike commuting spreadsheet.

## BikeCommute.py

This script modifies the current number of bike commutes in the Google Sheets spreadsheet [Bike Commuting](https://docs.google.com/spreadsheets/d/1DbbcRTwytdVD9khKGJmea5R1GdH41-4vfiq1I-UHxvs/edit?usp=sharing).

* Increment current completed commutes:
```bash
python BikeCommute.py
```

* Reset current completed commutes:
```bash
python BikeCommute.py -r
	or
python BikeCommute.py --reset
```
