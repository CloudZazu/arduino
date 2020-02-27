"""
Prerequisities:
pip install pyserial - Serial driver package
pip install pytz - Time zone package
"""
import datetime
import io
import pytz
import serial
 
#device   = '/dev/tty.usbserial-AE01AX15' # serial port (Linux/Mac)
device = 'COM3' # serial port (Windows)
baud     = 115200                        # baud rate
filename = 'button_switch_logging'                # log file to save data in
filename_ext = '.txt'


def get_log_output_file_ptr(timestamp):
    log_suffix = timestamp.strftime(LOG_SUFFIX_TIMESTAMP_FMT)

    outFile = None
    try:
        full_filename = f'{filename}_{log_suffix}{filename_ext}'
        outFile = open(full_filename, 'w')
    except Exception as e:
        print(f'issue with opening file\nError:{e}')

    return outFile
    
def convert_line_to_str(line):
    
    encodings = ['utf-8', 'utf-16', 'ascii']
    
    tmp_line = None
    for encoding in encodings:
        try:
            tmp_line = line.decode(encoding, 'ignore')
            break
        except Exception:
            pass
        
    return tmp_line if tmp_line else str(line)


BUTTON_LINEVAL_MAPPING = {'Button0' : 'A1', 
                          'Button1' : 'A2',
                          'Button2' : 'A3',
                          'Button3' : 'A4',
                          'Button4' : 'B1',
                          'Button5' : 'B2',
                          'Button6' : 'B3',
                          'Button7' : 'B4'}

if __name__ == '__main__':

    # Changeable constants
    TIMESTAMP_FMT = "%Y-%m-%d %H:%M:%S"
    LOG_SUFFIX_TIMESTAMP_FMT = "%Y-%m-%d_%H_%M_%S"
    LOG_SPLIT_INTERVAL = datetime.timedelta(days=1)

    EASTERN_TIMEZONE = pytz.timezone('US/Eastern')

    current_time = datetime.datetime.now()
    prior_time = current_time

    output_file = get_log_output_file_ptr(current_time)

    with serial.Serial(device, baud) as serialPort:
        print('Connected')

        while True:
            current_time = datetime.datetime.now()
            if prior_time + LOG_SPLIT_INTERVAL <= current_time:
                if output_file:
                    try:
                        output_file.close()
                    except Exception:
                        print('ptr doesnt exist')

                tmp_file = get_log_output_file_ptr(current_time)
                if tmp_file:
                    output_file = tmp_file
                
                # Reset prior_time to current time since its past LOG_SPLIT_INTERVAL
                prior_time = current_time

            line = serialPort.readline() # must send \n! get a line of log
            line = convert_line_to_str(line)
            
            # Attempt to strip un-necessary characters
            try:
                line = line.strip() # Removes carriage\tab\newline chars (\r\c\n)
            except Exception:
                pass

            # Attempt to add current system timestamp
            try:
                # Get current timestamp (GMT) and cast it to eastern time zone
                current_time = datetime.datetime.now(EASTERN_TIMEZONE)
                
                # converts current time to appropriate defined string format
                current_time = current_time.strftime(TIMESTAMP_FMT)
                try:
                    line = BUTTON_LINEVAL_MAPPING[line]
                except Exception:
                    pass
                    
                line = f'{current_time} - {line}'
            except Exception:
                pass

            print(line)                      # show line on screen
            output_file.write(line)          # write line of text to file
            output_file.write('\n')                # Add new line 
            output_file.flush()              # make sure it actually gets written out

    if output_file:
        output_file.close()

    print("We're done?!")
