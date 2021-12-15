'''
    File name: battery-notification.py
    Author: nskumar278@gmail.com
    Date created: 14/12/2021
    Date last modified: 14/12/2021
    Python Version: 3.8.10
    
    Description: 
    Battery Notification for Linux Systems. 
    When battery is full and still connected to power, it notifies with battery full speech.
    When battery is less than 15% and still not connected to power, it notifies with battery low speech.
    Every 5 minutes, it checks for battery status and notifies if battery is low or full.
    If battery is full, then every 5 seconds notification will come until power is removed.
    If battery is low, then every 5 seconds notification will come until power is attached. 
    In case of battery low, it notifies 10 times in a row after every 5 minutes (Power Cut Case Handling).
'''

import os, time
from gtts import gTTS  
from playsound import playsound  
  
batteryFull = "Battery Full! Please remove the charger"
batteryLow = "Battery Low! Please connect the charger"  

batteryFullMP3File = '/home/rently/batteryFull.mp3'
batteryLowMP3File = '/home/rently/batteryLow.mp3'

language = 'en'  

if not os.path.isfile(os.path.join(batteryFullMP3File)):
    obj = gTTS(text=batteryFull, lang=language, slow=False)  
    obj.save(batteryFullMP3File)

if not os.path.isfile(os.path.join(batteryLowMP3File)):
    obj = gTTS(text=batteryLow, lang=language, slow=False)
    obj.save(batteryLowMP3File)  

# 5 minutes
mainInterval = 5 * 60

# 5 seconds
interval = 5 

  
while True:
    count = 0
    while True:
        status = open ("/sys/class/power_supply/BAT0/status").read().strip()
        capacity = int (open ("/sys/class/power_supply/BAT0/capacity").read().strip())
        if status == 'Full':
            playsound(os.path.join(batteryFullMP3File)) 
        elif status == 'Discharging' and capacity <= 15:
            if count > 10:
                break;
            playsound(os.path.join(batteryLowMP3File))
            count = count + 1
        else:
            break
        
        time.sleep (interval)

    time.sleep(mainInterval)
