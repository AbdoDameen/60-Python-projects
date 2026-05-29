"""
Alarm Clock script.
Takes user input for alarm time and plays a sound when the time matches.
"""

from datetime import datetime
from playsound import playsound


def validate_time_format(alarm_time: str) -> bool:
    """
    Validate that the alarm time is in HH:MM:SS AM/PM format.
    Returns True if valid, False otherwise.
    """
    try:
        # Parse to verify format
        datetime.strptime(alarm_time, "%I:%M:%S %p")
        return True
    except ValueError:
        return False


def main():
    """Get user input, validate, and run the alarm loop."""
    while True:
        alarm_time = input("Enter the time to set the alarm (HH:MM:SS AM/PM): ").strip()
        if validate_time_format(alarm_time):
            break
        print("Invalid time format. Please use HH:MM:SS AM/PM (e.g., 11:30:00 AM).")

    alarm_hour = alarm_time[0:2]
    alarm_minute = alarm_time[3:5]
    alarm_seconds = alarm_time[6:8]
    alarm_period = alarm_time[9:11].upper()

    print("Setting up alarm...")

    while True:
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_seconds = now.strftime("%S")
        current_period = now.strftime("%p")

        if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_minute == current_minute:
                    if alarm_seconds == current_seconds:
                        print("Wakie Wakie!")
                        playsound("Alarm Clock.mp3")
                        break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nAlarm cancelled.")
