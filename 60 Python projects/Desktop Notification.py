"""
Desktop Notification script.
Sends a periodic desktop reminder to stretch using the plyer library.
"""

import time
from plyer import notification


def send_stretch_reminder():
    """Send a desktop notification to remind the user to stretch."""
    notification.notify(
        title='ALERT!!! TIME TO STRETCH!!!',
        message='Get up and stretch your legs and back!',
        timeout=10
    )


def main():
    """Run the reminder loop every hour."""
    while True:
        send_stretch_reminder()
        time.sleep(3600)  # Remind every hour


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nStretch reminder stopped.")
