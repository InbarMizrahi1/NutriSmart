# OTP.py

import random
import sys
import json
from flask import Flask, request, jsonify
import pywhatkit
import pyautogui
import time

app = Flask(__name__)

# Store OTPs for verification
otp_storage = {}

@app.route('/send_otp', methods=['POST']

)
def send_otp():
    try:
        data = request.get_json()
        phone_number = data.get('phoneNumber')
        otp = random.randint(10000, 99999)
        msg = f"Your OTP is {otp}"
        

        # Store OTP against phone number
        otp_storage[phone_number] = otp

        # Assuming sendwhatmsg_instantly sends OTP via WhatsApp
        pywhatkit.sendwhatmsg_instantly(phone_number, msg)
        time.sleep(10)
        pyautogui.press('enter')

        return jsonify({'otp': otp}), 200
    except Exception as e:


        print("Error sending OTP:", e)
        return jsonify({'error': 'Failed to send OTP'}), 500

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    try:
        data = request.get_json()
        phone_number = data.get('phoneNumber')
        user_otp = data.get('otp')

        # Retrieve the stored OTP for the given phone number
        stored_otp = otp_storage.get(phone_number)

        if stored_otp and str(stored_otp) == str(user_otp):
            return jsonify({'success': True}), 200
        else:
            return jsonify({'success': False, 'message': 'Invalid OTP'}), 400
    except Exception as e:
        print("Error verifying OTP:", e)
        return jsonify({'error': 'Failed to verify OTP'}), 500

if __name__ == "__main__":
    app.run(port=5173)
