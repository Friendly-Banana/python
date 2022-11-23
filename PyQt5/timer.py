#!/usr/bin/python3

from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)
from PySide2.QtGui import QPainter, QBrush, QPen, QColor, QIcon
from PySide2.QtMultimedia import QSound
from PySide2.QtCore import QTimer, QTime, QFile, QIODevice, Qt
from PySide2.QtUiTools import QUiLoader

from os.path import join, dirname


def get_path(filename: str):
    return join(dirname(__file__), filename)


def loadUI():
    ui_file_name = "mainwindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
        exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.show()


class Timer(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Timer, self).__init__(*args, **kwargs)

        self.setWindowTitle("Timer")
        self.setWindowIcon(QIcon(get_path("clock.svg")))
        self.setStyleSheet(
            "QMainWindow {background-color: #2c3e50} QPushButton {background-color: #34495e; color: #ecf0f1}"
        )
        self.width, self.height = 500, 500
        self.setGeometry(0, 0, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = app.primaryScreen().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.r, self.g = 0, 255
        self.stopped = False
        self.alarm = QSound(get_path("alarm music.wav"))
        # time in seconds
        self.interval = 15 * 60
        self.finishTime = QTime.currentTime().addSecs(self.interval)
        self.times = QPushButton(self.finishTime.toString("hh:mm:ss"), self)
        self.times.blockSignals(True)
        self.times.clicked.connect(self.restart)
        self.times.setGeometry(0, 0, 200, 100)
        self.times.move(
            self.width / 2 - self.times.width() / 2,
            self.height / 2 - self.times.height() / 2,
        )

        timer = QTimer(self)
        # action to do when timer has finished
        timer.timeout.connect(self.showTime)
        # 60 FPS
        timer.start(16)

    def stop(self):
        if self.stopped:
            return
        self.stopped = True
        self.times.setText("Restart")
        self.alarm.play()
        self.times.blockSignals(False)
        self.repaint()

    def restart(self):
        self.r, self.g = 0, 255
        self.stopped = False
        self.finishTime = QTime.currentTime().addSecs(self.interval)
        self.alarm.stop()
        self.times.blockSignals(True)

    def showTime(self):
        if self.stopped:
            return

        currentTime = QTime.currentTime()
        if currentTime.msecsTo(self.finishTime) <= 0:
            self.stop()
            return

        diff = currentTime.secsTo(self.finishTime)
        displayTxt = f'Remaining: {QTime(0, diff // 60, diff % 60).toString("mm:ss")}\nCurrent time: {currentTime.toString("hh:mm:ss")}'
        self.times.setText(displayTxt)
        self.repaint()

    def paintEvent(self, e):
        hcenter, vcenter = int(self.width / 2 - 150), int(self.height / 2 - 150)
        percent = QTime.currentTime().msecsTo(self.finishTime) / (self.interval * 1000)
        if percent < 0.5:
            self.g = percent * 255 * 2
            self.r = 255
        else:
            self.g = 255
            self.r = (1 - percent) * 255 * 2

        blue = QColor("#2c3e50")
        gradient = QColor(int(self.r), int(self.g), 0)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # solid circle inside
        painter.setBrush(QBrush(blue, Qt.SolidPattern))
        painter.drawEllipse(hcenter, vcenter, 300, 300)

        # Fading circle outside
        painter.setPen(QPen(gradient, 8, Qt.SolidLine))
        painter.drawArc(hcenter, vcenter, 300, 300, 90 * 16, 360 * percent * 16)
        painter.end()


app = QApplication()

window = Timer()
window.show()

app.exec_()
