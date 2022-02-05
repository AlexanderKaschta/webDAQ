from webDAQ import socketio
import sys

socketio.connect('http://localhost:5000')
try:
    socketio.wait()
except KeyboardInterrupt:
    print('Interrupted')
    sys.exit(0)