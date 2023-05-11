from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QMainWindow, QApplication
from ui_mainwindow import Ui_MainWindow
import serial
# import system libraries
import time, random


# import Adafruit IO REST client
from Adafruit_IO import Client, Feed, RequestError

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_Wlkq70a8bxarcX2mW0sryKYpF0nv'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'pgmaldonado'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'analog' feed
    feed_01 = aio.feeds('slider')
except RequestError: # create an `analog` feed
    feed = Feed(name='slider')
    feed_01 = aio.create_feed(feed)


try: # if we have a 'analog' feed
    feed_00 = aio.feeds('gauge')
except RequestError: # create an `analog` feed
    feed = Feed(name='gauge')
    feed_00 = aio.create_feed(feed)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.serial_port = None

        self.pushButton.clicked.connect(self.connect_port)
        self.pushButton_2.clicked.connect(self.send_data)
        self.pushButton_3.clicked.connect(self.close_port)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.receive_data)
        self.timer.start(100)

    def connect_port(self):
        port_name = self.comboBox.currentText()
        try:
            self.serial_port = serial.Serial(port_name, 9600)
        except serial.SerialException as e:
            self.statusbar.showMessage(str(e))

    def send_data(self):
        if self.serial_port is not None:
            read = aio.receive(feed_01.key)
            data = read.value.encode()
            self.serial_port.write(data)

    def receive_data(self):
        if self.serial_port is not None:
            data = self.serial_port.read_all().decode(encoding="ascii", errors="replace")
            if data:
                self.textBrowser.append(data)
                var = int(data)
                print(type(data))
                aio.send(feed_00.key, var)

    def close_port(self):
        if self.serial_port is not None:
            self.serial_port.close()
            self.serial_port = None

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()