# Battery Notification Service
Author: nskumar278@gmail.com
/nDate created: 15/12/2021
/nDate last modified: 15/12/2021
/nPython Version: 3.8.10

Description: 
Battery Notification for Linux Systems. 
When battery is full and still connected to power, it notifies with battery full speech.
When battery is less than 15% and still not connected to power, it notifies with battery low speech.
Every 5 minutes, it checks for battery status and notifies if battery is low or full.
If battery is full, then every 5 seconds notification will come until power is removed.
If battery is low, then every 5 seconds notification will come until power is attached. 
In case of battery low, it notifies 10 times in a row after every 5 minutes (Power Cut Case Handling).

Steps to Setup:
1. Copy battery-notification.py to /usr/bin
2. Copy battery-notification.service to /lib/systemd/system
3. Enter command in terminal: systemctl enable battery-notification
4. Enter command in terminal: reboot or systemctl start battery-notification
