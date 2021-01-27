import time
from plyer import notification

if __name__ == '__main__':
    while true:
        notification.notify(
            title = "ALEART!!! TIME TO STRETCH!!!",
            message= "TIME TO GET UP AND STRETCH",
            timeout= 10

        )
        time.sleep(3600)
