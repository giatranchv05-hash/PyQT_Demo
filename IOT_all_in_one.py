# -*- coding: utf-8 -*-
import sys
import random
from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import image_


class IOTWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ZENDA IOT")
        self.resize(900, 700)
         # ===== MAIN STYLE =====
        self.setStyleSheet("""
        QMainWindow {
            background-color: #F2F2F2;
        }
        QPushButton {
            background-color: white;
            border: 1px solid #B0B0B0;
            border-radius: 6px;
            padding: 4px 10px;
        }
        QPushButton:hover {
            background-color: #EDEAFF;
        }
        """)


        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        # ===== LOGO =====
        self.logo_hcmute = QtWidgets.QLabel(self.centralwidget)
        self.logo_hcmute.setGeometry(10, 10, 90, 90)
        pixmap = QtGui.QPixmap("logo.jpg")
        self.logo_hcmute.setPixmap(pixmap)
        self.logo_hcmute.setScaledContents(True)


        # ===== TITLE =====
        self.label = QtWidgets.QLabel("ZENDA", self.centralwidget)
        self.label.setGeometry(140, 35, 200, 40)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        # ===== OVEN =====
        self.oven_img = QtWidgets.QLabel(self.centralwidget)
        self.oven_img.setGeometry(10, 90, 300, 120)
        self.oven_img.setStyleSheet("image: url(:/myimage/oven_off.png);")

        self.btn_oven_on = QtWidgets.QPushButton("ON", self.centralwidget)
        self.btn_oven_on.setGeometry(20, 210, 70, 30)
        self.btn_oven_off = QtWidgets.QPushButton("OFF", self.centralwidget)
        self.btn_oven_off.setGeometry(200, 210, 70, 30)

        # ===== LAMP =====
        self.lamp_img = QtWidgets.QLabel(self.centralwidget)
        self.lamp_img.setGeometry(10, 260, 300, 120)
        self.lamp_img.setStyleSheet("image: url(:/myimage/lamp_off.png);")

        self.btn_lamp_on = QtWidgets.QPushButton("ON", self.centralwidget)
        self.btn_lamp_on.setGeometry(20, 380, 70, 30)
        self.btn_lamp_off = QtWidgets.QPushButton("OFF", self.centralwidget)
        self.btn_lamp_off.setGeometry(200, 380, 70, 30)

        # ===== FAN =====
        self.fan_img = QtWidgets.QLabel(self.centralwidget)
        self.fan_img.setGeometry(10, 430, 300, 120)
        self.fan_img.setStyleSheet("image: url(:/myimage/fan_off.png);")

        self.btn_fan_on = QtWidgets.QPushButton("ON", self.centralwidget)
        self.btn_fan_on.setGeometry(20, 560, 70, 30)
        self.btn_fan_off = QtWidgets.QPushButton("OFF", self.centralwidget)
        self.btn_fan_off.setGeometry(200, 560, 70, 30)

        # ===== SENSOR GROUP =====
        self.groupBox = QtWidgets.QGroupBox("THÔNG SỐ MÔI TRƯỜNG",self.centralwidget)
        self.groupBox.setGeometry(380, 30, 280, 160)
        self.groupBox.setStyleSheet("""
        QGroupBox {
            background-color: #E6E1FF;
            font-weight: bold;
        }
        """)
        layout = QtWidgets.QFormLayout(self.groupBox)

        self.lcd_temp = QtWidgets.QLCDNumber()
        self.lcd_humid = QtWidgets.QLCDNumber()
        self.lcd_light = QtWidgets.QLCDNumber()
        lcd_style = """
        QLCDNumber {
            background-color: #FFFFFF;
            border-radius: 6px;
        }
        """

        layout.addRow("Nhiệt độ", self.lcd_temp)
        layout.addRow("Độ ẩm", self.lcd_humid)
        layout.addRow("Ánh sáng", self.lcd_light)

        # ===== CHART =====
        self.chart_box = QtWidgets.QGroupBox("BIỂU ĐỒ MÔI TRƯỜNG", self.centralwidget)
        self.chart_box.setGeometry(330, 220, 500, 360)
        self.chart_box.setStyleSheet("""
        QGroupBox {
            background-color: #E6E1FF;
            border-radius: 10px;
        }
        """)
        chart_layout = QtWidgets.QVBoxLayout(self.chart_box)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        chart_layout.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)

        self.data = []

        # ===== TIMER =====
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_sensor)
        self.timer.start(1000)

        # ===== SIGNALS =====
        self.btn_oven_on.clicked.connect(lambda: self.oven_img.setStyleSheet("image: url(:/myimage/oven_on.png);"))
        self.btn_oven_off.clicked.connect(lambda: self.oven_img.setStyleSheet("image: url(:/myimage/oven_off.png);"))

        self.btn_lamp_on.clicked.connect(lambda: self.lamp_img.setStyleSheet("image: url(:/myimage/lamp_on.png);"))
        self.btn_lamp_off.clicked.connect(lambda: self.lamp_img.setStyleSheet("image: url(:/myimage/lamp_off.png);"))

        self.btn_fan_on.clicked.connect(lambda: self.fan_img.setStyleSheet("image: url(:/myimage/fan_on.png);"))
        self.btn_fan_off.clicked.connect(lambda: self.fan_img.setStyleSheet("image: url(:/myimage/fan_off.png);"))

    # ===== UPDATE SENSOR =====
    def update_sensor(self):
        temp = random.randint(25, 40)
        humid = random.randint(40, 90)
        light = random.randint(100, 1000)

        self.lcd_temp.display(temp)
        self.lcd_humid.display(humid)
        self.lcd_light.display(light)

        self.data.append(temp)
        if len(self.data) > 20:
            self.data.pop(0)

        self.ax.clear()
        self.ax.plot(self.data)
        self.ax.set_title("Nhiệt độ")
        self.canvas.draw()


# ===== RUN DIRECTLY =====
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = IOTWindow()
    window.show()
    sys.exit(app.exec_())
