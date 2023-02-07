import datetime
import winsound

# Set the alarm time
alarm_time = "10:30:00"

# Get the current time
current_time = datetime.datetime.now().time().isoformat()

while True:
    if current_time == alarm_time:
        winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
        break
    else:
        current_time = datetime.datetime.now().time().isoformat()