import sys
import serial
import serial.tools.list_ports
import csv

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QGroupBox, QGridLayout, QPushButton, QComboBox, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Vibra SensePro'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: lightgray;")
        self.setWindowIcon(QIcon('icon.png'))

        self.layout = QVBoxLayout()

        self.iconLabel = QLabel(self)
        self.iconLabel.setPixmap(QIcon('icon.png').pixmap(250, 250))
        self.iconLabel.setAlignment(Qt.AlignCenter)

        self.nameLabel = QLabel('Vibra SensePro', self)
        self.nameLabel.setTextFormat(Qt.RichText)
        font = QFont('Cabiri', 16)
        font.setBold(True)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.iconLabel)
        self.layout.addWidget(self.nameLabel)

        self.setLayout(self.layout)

        self.btn_next = QPushButton('Next', self)
        self.btn_next.setGeometry(400, 470, 100, 30)
        self.btn_next.clicked.connect(self.next)

    def next(self):
        self.dialog = ComManager()
        self.dialog.show()

class ComManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.com_refresh()

    def initUI(self):
        self.setWindowTitle("Vibra SensePro")
        self.setGeometry(100, 100, 500, 500)
        self.setWindowIcon(QIcon('icon.png'))

        self.frame = QGroupBox("Com Manager", self)
        self.frame.setStyleSheet("QGroupBox { background-color: lightgray; border: 1px solid blue; }")
        self.frame.setGeometry(10, 10, 480, 480)

        self.label_com = QLabel("Available Port(s):", self.frame)
        self.label_com.setStyleSheet("background-color: gray;")

        self.label_bd = QLabel("Baud Rate:", self.frame)
        self.label_bd.setStyleSheet("background-color: gray;")

        self.drop_com = QComboBox(self.frame)
        self.drop_com.setMinimumWidth(100)
        self.drop_com.addItem('-')

        self.drop_baud = QComboBox(self.frame)
        self.drop_baud.setMinimumWidth(100)
        self.drop_baud.addItem('-')
        self.drop_baud.addItems(['9600', '19200', '38400', '57600', '115200', '250000'])

        self.btn_refresh = QPushButton("Refresh", self.frame)
        self.btn_refresh.clicked.connect(self.com_refresh)
        self.btn_connect = QPushButton("Connect", self.frame)
        self.btn_connect.clicked.connect(self.connect)

        self.publish()

    def publish(self):
        self.layout = QGridLayout(self.frame)
        self.layout.addWidget(self.label_com, 1, 1)
        self.layout.addWidget(self.label_bd, 2, 1)
        self.layout.addWidget(self.drop_com, 1, 2)
        self.layout.addWidget(self.drop_baud, 2, 2)
        self.layout.addWidget(self.btn_refresh, 3, 1)
        self.layout.addWidget(self.btn_connect, 3, 3)
        self.frame.setLayout(self.layout)

    def com_refresh(self):
        self.drop_com.clear()
        self.drop_com.addItem('-')
        ports = serial.tools.list_ports.comports()
        if ports:
            for port in ports:
                self.drop_com.addItem(port.device)
        else:
            self.drop_com.addItems(['COM1', 'COM2'])
        self.drop_com.setCurrentIndex(0)

    def connect(self):
        self.dialog1 = MainWindow(self.drop_com.currentText(), self.drop_baud.currentText())
        self.dialog1.show()

class SerialThread(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        try:
            self.ser = serial.Serial(port, baudrate)
        except serial.SerialException as e:
            self.ser = None
            self.error_message = str(e)

    def run(self):
        if not self.ser:
            return
        self.running = True
        while self.running:

            if self.ser.in_waiting:
                try:
                    data = self.ser.readline().decode('utf-8').strip()
                    self.data_received.emit(data)
                except UnicodeDecodeError:
                    pass
                except TypeError:
                    pass
    def stop(self):
        if self.ser:
            self.running = False
            self.ser.close()

class MainWindow(QMainWindow):
    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Vibra SensePro")
        self.setGeometry(100, 100, 500, 500)
        self.setWindowIcon(QIcon('icon.png'))

        self.frame = QGroupBox("Data Collection", self)
        self.frame.setStyleSheet("QGroupBox { background-color: lightgray; border: 1px solid blue; }")
        self.frame.setGeometry(10, 10, 480, 480)

        self.start_button = QPushButton("Start", self)
        self.start_button.setFixedSize(250, 30)
        self.start_button.clicked.connect(self.start_data_collection)
        
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setFixedSize(250, 30)
        self.stop_button.clicked.connect(self.stop_data_collection)

        self.save_button = QPushButton("Save", self)
        self.save_button.setFixedSize(250, 30)
        self.save_button.clicked.connect(self.save_data)

        self.start_label = QLabel("Start collecting data...", self)
        self.start_label.setAlignment(Qt.AlignCenter)
        self.start_label.hide()  # Initially hide the start label

        self.stop_label = QLabel("Stop collecting data...", self)
        self.stop_label.setAlignment(Qt.AlignCenter)
        self.stop_label.hide()  # Initially hide the stop label

        self.layout = QGridLayout(self.frame)
        self.layout.addWidget(self.start_button, 1, 1)
        self.layout.addWidget(self.start_label, 1, 2)
        self.layout.addWidget(self.stop_button, 2, 1)
        self.layout.addWidget(self.stop_label, 2, 2)
        self.layout.addWidget(self.save_button, 3, 1)
        #self.layout.addWidget(self.finish_button, 4, 2)
        self.frame.setLayout(self.layout)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        self.finish_button = QPushButton('Finish', self)
        self.finish_button.setGeometry(380, 450, 100, 30)
        self.finish_button.clicked.connect(QApplication.instance().quit)

        self.data_thread = None
        self.data = []

    def start_data_collection(self):
        if self.port and self.baudrate:
            self.data_thread = SerialThread(self.port, int(self.baudrate))
            if not self.data_thread.ser:
                QMessageBox.critical(self, "Error", f"Failed to open serial port: {self.data_thread.error_message}")
                return
            self.data_thread.data_received.connect(self.update_data)
            self.data_thread.start()
            self.start_label.show()
            self.stop_label.hide()

    def stop_data_collection(self):
        if self.data_thread:
            self.data_thread.stop()
            self.start_label.hide()
            self.stop_label.show()

    def update_data(self, data):
        print(f"Received data: {data}")  # Debug print
        self.data.append(data)
        # Assuming you have a QLabel to display data. Create one if not
        if not hasattr(self, 'data_label'):
            self.data_label = QLabel(self)
            self.layout.addWidget(self.data_label, 5, 1, 1, 2)
        self.data_label.setText(f"Data: {data}")


    def save_data(self):
        self.stop_label.hide()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Data", "", "CSV Files (*.csv)")
        if file_path:
            with open(file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["AX", "AY", "AZ", "Hours", "Minutes", "Seconds", "Milliseconds"])  # Updated CSV Header
                for line in self.data:
                    parts = line.split()  # Split the line by whitespace
                    if len(parts) == 7:  # Ensure that we have the expected number of parts
                        ax = parts[1]  # Extract AX value
                        ay = parts[3]  # Extract AY value
                        az = parts[5]  # Extract AZ value
                        timestamp = parts[6]  # Extract Timestamp as a single part

                        # Split the timestamp into hours, minutes, seconds, milliseconds
                        time_parts = timestamp.split('.')
                        if len(time_parts) == 4:  # Ensure correct timestamp format
                            hours = time_parts[0]
                            minutes = time_parts[1]
                            seconds = time_parts[2]
                            milliseconds = time_parts[3]

                            # Write data to CSV with the split timestamp
                            writer.writerow([ax, ay, az, hours, minutes, seconds, milliseconds])

            QMessageBox.information(self, "Success", f"Data saved to {file_path}")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
