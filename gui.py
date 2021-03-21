#!/usr/bin/python3

import sys
import os
import signal

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from replay_sorcery import ReplaySorcery

signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QApplication([])

dir_name = os.path.dirname(sys.argv[0])        
full_path = os.path.abspath(dir_name)
icon_filename = 'icon.png'
icon_path = os.path.join(full_path, icon_filename)

class ReplaySorceryGUI(QWidget):

   def __init__(self, debug):
      self.debug = debug
      self.rs = ReplaySorcery(self.debug)

      QWidget.__init__(self)
      self.setWindowTitle('ReplaySorceryGUI')
      self.setWindowIcon(QIcon(icon_path))
      self.setMinimumWidth(300)

      app_layout = QHBoxLayout()

      # left side

      left_layout = QVBoxLayout()
      left_layout.setAlignment(Qt.AlignCenter)

      self.icon = QPixmap(icon_path)
      self.icon = self.icon.scaled(92, 92)
      self.icon_label = QLabel()
      self.icon_label.setPixmap(self.icon)
      self.icon_label.setAlignment(Qt.AlignCenter)
      left_layout.addWidget(self.icon_label)

      self.instructions_text = QLabel()
      self.instructions_text.setText("Ctrl+Super+R to save\nthe last 30 seconds\n")
      left_layout.addWidget(self.instructions_text)

      self.status_text = QLabel()
      self.update_status_text()
      left_layout.addWidget(self.status_text)

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
         left_layout.addWidget(button)

      # right side

      right_layout = QVBoxLayout()
      right_layout.setAlignment(Qt.AlignCenter)

      # both sides

      app_layout.addLayout(left_layout)
      app_layout.addLayout(right_layout)

      self.setLayout(app_layout)

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
      if self.debug > 0:
         print("Exiting ReplaySorceryGUI")
      sys.exit()

window = ReplaySorceryGUI(1)
window.show()
if window.debug > 0:
   print("ReplaySorceryGUI started")
app.exec_()
