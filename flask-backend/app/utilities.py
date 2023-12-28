from sqlalchemy.types import TypeDecorator
from sqlalchemy import Integer
import platform


class UnixTimestamp(TypeDecorator):
    impl = Integer

    def process_bind_param(self, value, dialect):
        if value is not None:
            return int(value.timestamp())
        else:
            return None


# GPIO handler
if platform.machine().lower() == 'armv71' and platform.system().lower() == 'linux':
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        print("GPIO library not found. Install it with 'pip install RPi.GPIO'")
        GPIO = None
else:
    class MockGPIO:
        BOARD = 1
        OUT = 1
        IN = 1
        HIGH = 1
        LOW = 1
        BCM = 1

        @staticmethod
        def setmode(mode):
            print("### GPIO mode set to {} ###".format(mode))

        @staticmethod
        def setup(pin, mode):
            print("### GPIO pin {} set to {} ###".format(pin, mode))

        @staticmethod
        def output(pin, value):
            print("### GPIO pin {} set to {} ###".format(pin, value))

        @staticmethod
        def input(pin):
            print("### GPIO pin {} read ###".format(pin))

        @staticmethod
        def cleanup():
            print("### GPIO cleanup ###")

        @staticmethod
        def setwarnings(value):
            print("### GPIO warnings set to {} ###".format(value))

    GPIO = MockGPIO
