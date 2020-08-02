## Description

**ReplaySorceryGUI** is an attempt to easily control the status of [ReplaySorcery](https://github.com/matanui159/ReplaySorcery) process as one might not want to have it on 100% of the time due to either privacy reasons or potential memory leaks.

## Dependencies

- Python 3
- PyQt5
- psutil
- ReplaySorcery

First two can be installed on Debian/Ubuntu by running:

    sudo apt-get install python3 python3-pyqt5 python3-psutil

ReplaySorcery has to be installed by following instructions on [its own GitHub page](https://github.com/matanui159/ReplaySorcery).

    git clone https://github.com/matanui159/ReplaySorcery.git
    git submodule update --init
    cmake -B bin -DCMAKE_BUILD_TYPE=Release
    make -C bin
    sudo make -C bin install

## Usage

Start the GUI
    
    python3 gui.py

## Screenshot
![Screenshot of ReplaySorceryGUI window](https://github.com/hardpenguin/replay-sorcery-gui/raw/master/screenshot.png)

## Todo

- proper building (PyInstaller?)
- perhaps .deb for Debian distros