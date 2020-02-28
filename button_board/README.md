# Button Board
- [How it Works](#How-it-Works)
- [Required Packages](#Required-Packages)

## How it Works
We leverage the Arduino sketch code as the firmware to collect the button sensory data.\
Then, use a Python script to data collect off the serial port and store it on a csv file 
based on some interval that you specify per the script.\
The current script stores the log at a daily basis starting at when it started.
i.e If the Python script started at 5PM EST, it would reset at 5PM EST on the following day.
```
python button_board_logging.py
```

### Requirements
####Ardunio 
Arduino needs to be installed on some system in order to upload the .ino sketch file.
####Python Packages
To install required Python packages, run the following
```
pip install pyserial - Serial driver package
pip install pytz - Time zone package
```