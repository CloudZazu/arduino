# Button Board
- [How it Works](#How-it-Works)
- [Required Packages](#Required-Packages)

## How it Works
We leverage the Arduino sketch code as the firmware to collect the button sensory data.\
Then, use a Python script to data collect off the serial port and store it on a csv file 
based on some interval that you specify per the script.\
The current script stores the log at a daily basis starting at when it started.\
i.e If the Python script started at 5PM EST, it would reset at 5PM EST on the following day.

## Python Execution Command
The following command should be ran in the directory that contains the button_board_logging.py
```
python button_board_logging.py
```
or you can do something like the following with an absolute filepath to run it:
```
python /Documents/arduino/button_board_logger.py
```
## Requirements

### Arduino 
Arduino needs to be installed on some system in order to upload the .ino sketch file.\
The Arduino version should be at least 1.8.10.

### Python Packages
At least Python 3.8 needs to be installed on the client PC and ensure pip is installed with it as an option.\
To install required Python packages, run the following in command prompt/Terminal
```
pip install pyserial
pip install pytz 
```
pyserial - Serial driver package\
pytz - Time zone package