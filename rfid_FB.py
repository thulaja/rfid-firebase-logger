fid firebase
import RPi.GPIO as GPIO
import time
import firebase_admin
from firebase_admin import credentials, db
from mfrc522 import SimpleMFRC522

# Firebase Setup
cred = credentials.Certificate(" path.json")  # <-- update path if needed
firebase_admin.initialize_app(cred, {
    'databaseURL': ''  # <-- change to your DB URL
})

ref = db.reference('rfid_logs')

# GPIO and RFID setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
reader = SimpleMFRC522()

try:
    while True:
        print("Place your card...")
        id, text = reader.read()
        cleaned_text = text.strip().upper()
        print("ID:", id)
        print("Text:", cleaned_text)

        if id == 718218134462:
            print("Authorized card")
            team_name = 'priyanka'
            access_status = 'Access Granted'
            GPIO.output(40, 1)
        elif id == 456761152055:
            print("Authorized card")
            team_name = 'jayasree'
            access_status = 'Access Granted'
            GPIO.output(40, 1)
        else:
            team_name = cleaned_text
            print("Unauthorized card")
            access_status = 'Access Denied'
            GPIO.output(40, 0)

        log_data = {
            'rfid_id': str(id),
            'team_name': team_name,
            'access_status': access_status,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }

        ref.push(log_data)
        print("Data sent to Firebase!")

        time.sleep(5)
        GPIO.output(40, 0)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
