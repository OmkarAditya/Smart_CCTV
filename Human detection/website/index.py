from flask import Flask, render_template, request
import serial
import time

app = Flask(__name__)

ser = serial.Serial('COM20', 9600)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:servo_number>/<int:joystick_value>', methods=['POST'])
def move_servo(servo_number, joystick_value):
    command = f'{servo_number}:{joystick_value}'
    ser.write(command.encode())
    time.sleep(0.1)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
