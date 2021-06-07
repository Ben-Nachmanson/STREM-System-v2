# STREM-System-v2

## !!!Rasberry Pi needs to be integrated and Stepper needs to be implemented.

Python script for a lab experiment.

Necessary Packages:
Python 3
https://www.python.org/downloads/

PyQt5

## Linux
> sudo apt-get install python3-pyqt5

## Windows
> pip install PyQt5

## Mac
> python3 -m pip install PyQt5

Please Refer to https://pythonbasics.org/install-pyqt/ if you are having further issues installing PyQt5.

To run the application compile this file. 
> STREMv2GUI.py



When using the application check that all inputs (Sheet & StartStage) do not have error messages then click reset everytime before the Start button is clicked.

When changing the Start Stage value just write the number and click reset. You will get errors otherwise.

The cycle will loop endlessly unless the "Reset" button is clicked, and it will halt at the current state when "Pause" is clicked.

The Ph and ORP values are being written to a .txt file every 5 minutes.

The Save feature will save the current sheet to a .txt file, then to load it use the Load feature click the .txt File you would like to load then click reset.


