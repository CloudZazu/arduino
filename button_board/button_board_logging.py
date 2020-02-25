"""
Prerequisities:
pip install pyserial - Serial driver package

"""
import io
import serial
 
#device   = '/dev/tty.usbserial-AE01AX15' # serial port (Linux/Mac)
device = 'COM3' # serial port (Windows)
baud     = 115200                        # baud rate
filename = 'button_switch_logging.txt'                # log file to save data in
 
with serial.Serial(device, baud) as serialPort, open(filename,'wb') as outFile:
    print('Connected')
    
    while True:
        line = serialPort.readline() # must send \n! get a line of log
        print(line)                 # show line on screen
        outFile.write(line)          # write line of text to file
        outFile.flush()              # make sure it actually gets written out

print("We're done?!")
