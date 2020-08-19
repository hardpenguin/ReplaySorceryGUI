import os

import psutil

class ReplaySorcery(object):
    def __init__(self, debug=1):
        self.debug = debug
        
        self._statuses = {
                            "unknown": {
                                "name": "Unknown",
                                "color": "yellow"
                            },

                            "on": {
                                "name": "On",
                                "color": "green"
                            },

                            "off": {
                                "name": "Off",
                                "color": "red"
                            }
                        }

        self.current_status = self._statuses["unknown"]

        self._systemd_command = "systemctl --user %s --now replay-sorcery"

        self.get_status()

    def get_status(self):
        if self.debug > 1:
            print("Getting current ReplaySorcery status: ", end="")

        process_found = False
        for proc in psutil.process_iter(["name"]):
            if "replay-sorcery" in proc.info["name"]:
                process_found = True
                self.current_status = self._statuses["on"]
                break

        if not process_found:
            self.current_status = self._statuses["off"]

        if self.debug > 1:
            print(self.current_status["name"])

    def turn_on(self):
        if self.debug > 0:
            print("Turning ReplaySorcery on")

        os.system(self._systemd_command % "enable")

        self.get_status()

    def turn_off(self):
        if self.debug > 0:
            print("Turning ReplaySorcery off")
        
        os.system(self._systemd_command % "disable")

        self.get_status()