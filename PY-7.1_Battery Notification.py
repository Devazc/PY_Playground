import psutil
import time
import pyttsx3
from win10toast import ToastNotifier
import threading

toaster = ToastNotifier()
x = pyttsx3.init()
x.setProperty('rate', 110)
x.setProperty('volume', 3)
count = 0

def show_notification(show_text):
    global count
    if count < 2:
        toaster.show_toast(show_text,
                           icon_path='battery_indicator.ico',
                           duration=10)
        count += 1

def monitor():
    while True:
        time.sleep(1)
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = int(battery.percent)

        if percent < 29:
            if not plugged:
                show_notification("Your battery is at " + str(percent) + "%. Please plug in the charger.")
                x.say("Your battery is getting low so charge it right now")
                x.runAndWait()

        elif percent >= 80:
            if plugged:
                show_notification("Charging is getting complete.")
                x.say("Charging is getting complete.")
                x.runAndWait()

if __name__ == "__main__":
    monitor()
