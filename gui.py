#!/usr/bin/python3

import sys
import signal

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from replay_sorcery import ReplaySorcery

signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QApplication([])

class ReplaySorceryGUI(QWidget):

   def __init__(self):
      QWidget.__init__(self)
      self.setWindowTitle('ReplaySorceryGUI')
      self.setMinimumWidth(300)

      layout = QVBoxLayout()
      layout.setAlignment(Qt.AlignCenter)

      self.rs = ReplaySorcery()

      # self.icon = QPixmap("icon.png")
      # self.icon = self.icon.scaled(92, 92)
      # self.icon_label = QLabel()
      # self.icon_label.setPixmap(self.icon)
      # layout.addWidget(self.icon_label)

      self.status_text = QLabel()
      self.update_status_text()
      layout.addWidget(self.status_text)

      self.timer = QTimer(self)
      self.timer.timeout.connect(self.update_status_text)  
      self.timer.start(1000)

      button_size = QSize(150, 40)

      buttons = []
      turn_on_button = QPushButton("Turn on")
      buttons.append(turn_on_button)
      turn_on_button.clicked.connect(self.turn_on_action)

      turn_off_button = QPushButton("Turn off")
      buttons.append(turn_off_button)
      turn_off_button.clicked.connect(self.turn_off_action)

      refresh_button = QPushButton("Refresh")
      buttons.append(refresh_button)
      refresh_button.clicked.connect(self.refresh_action)

      quit_button = QPushButton("Quit")
      buttons.append(quit_button)
      quit_button.clicked.connect(self.quit_action)

      for button in buttons:
         button.setFixedSize(button_size)
         layout.addWidget(button)

      self.setLayout(layout)

   def update_status_text(self):
      text_string = "ReplaySorcery: %s" % self.rs.current_status["name"]
      self.status_text.setText(text_string)
      color_string = 'color: %s' % self.rs.current_status["color"]
      self.status_text.setStyleSheet(color_string)
      self.rs.get_status()

   def turn_on_action(self):
      self.rs.turn_on()

   def turn_off_action(self):
      self.rs.turn_off()

   def refresh_action(self):
      self.rs.get_status()

   def quit_action(self):
      print("Exiting ReplaySorceryGUI")
      sys.exit()

window = ReplaySorceryGUI()
window.show()
print("ReplaySorceryGUI started")
app.exec_()
