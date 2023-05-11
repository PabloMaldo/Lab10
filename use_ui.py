from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QMainWindow, QApplication
from ui_mainwindow import Ui_MainWindow
import serial

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
            data = self.lineEdit.text().encode()
            self.serial_port.write(data)

    def receive_data(self):
        if self.serial_port is not None:
            data = self.serial_port.read_all().decode(encoding="ascii", errors="replace")
            if data:
                self.textBrowser.append(data)

    def close_port(self):
        if self.serial_port is not None:
            self.serial_port.close()
            self.serial_port = None

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()