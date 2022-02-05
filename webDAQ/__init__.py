import time

from webDAQ.sensor.RandomDataSensor import RandomDataSensor
import socketio

socketio = socketio.Client()


@socketio.event
def connect():
    print('connection established')
    socketio.emit("connected", data={"type": 1})


@socketio.on("start")
def on_message():
    print("Arrived!")
    interval = 0.1

    sensor = RandomDataSensor()
    last_time = time.time()

    while True:
        current_time = time.time()
        if current_time - last_time > interval:
            data = sensor.get_data()
            socketio.emit("new-data", data={"data": data, "time": current_time})

            # Update time
            last_time = current_time


@socketio.event
def disconnect():
    print('disconnected from server')
