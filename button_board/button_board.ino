// Button Switch Quantity dependent variables - As you add more switches, add more here!
int buttonPinMapping[] = {2,4,5,7,8,10,11,13}; // Button Pin input locations
int ARRAY_SIZE = sizeof(buttonPinMapping) / sizeof(int);

// Default initial/global states per switch
lastButtonState = new int [ARRAY_SIZE]
lastDebounceTime = new unsigned long [ARRAY_SIZE]
int lastButtonState[ARRAY_SIZE]; // lastButtonState tracking
unsigned long lastDebounceTime[ARRAY_SIZE]; // lastDebounceTime tracking

// ----------------------------------------------------------
unsigned long debounceDelay = 50; // Vibration+electrical noise delay offset (ms) 

int defaultButtSelect = ARRAY_SIZE;
int buttSelect = defaultButtSelect; // 3 - Default - Idle Case - Has to be +1 higher than whatever # of switches are configured
// i.e 2 switches means this should be 2+1
int buttonFlag = 0;

int buttonState = 1;


void setup() {
  for (int x = 0; x < ARRAY_SIZE; x++) {
    pinMode(buttonPinMapping[x], INPUT_PULLUP);
    lastButtonState[x] = 1
    lastDebounceTime[x] = 0
    //attachInterrupt(buttonPinMapping[x], buttPressed, LOW);
  }
   Serial.begin(115200);
}

void loop() {
  while (buttonFlag == 0) {
      delay(10);
      buttPressed();
  }

  if (buttSelect != defaultButtSelect){
      buttonIdStr = "Button" + buttSelect
      Serial.println(buttonIdStr);
  }

  bool pressed = pin_read(buttSelect);
  while (!pressed) {
      pressed = pin_read(buttSelect);
  }

  buttonFlag = 0;
  buttSelect = defaultButtSelect;
}

void buttPressed() {
  for (int idx = 0; idx < ARRAY_SIZE; idx++) {
      bool butt = pin_read(idx);
      if (!butt) {
          buttSelect = idx;
          buttonFlag = 1;
          break;
      }
  }
}

bool pin_read(int buttonIdx)
{
  // Debounce function
    int reading = digitalRead(buttonPinMapping[buttonIdx]);

  /*
  Serial.println("reading");
  Serial.println(reading);
  Serial.println(lastButtonState[buttonIdx]);
  */
  // check to see if you just pressed the button
  // (i.e. the input went from LOW to HIGH),  and you've waited
  // long enough since the last press to ignore any noise:  

  // If the switch changed, due to noise or pressing:
  if (reading != lastButtonState[buttonIdx]) {
    // reset the debouncing timer
    //Serial.println("YES THERES A DIFF");
    lastDebounceTime[buttonIdx] = millis();
  }
  //Serial.println(millis());
  //Serial.println(lastDebounceTime[buttonIdx]);
  if ((millis() - lastDebounceTime[buttonIdx]) >= debounceDelay) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
    //Serial.println("Reading saved");
    buttonState = reading;
  }
 
 lastButtonState[buttonIdx] = reading;
 /*
 Serial.println("buttonState");
 Serial.println(buttonState);
 */
 return buttonState;
}
