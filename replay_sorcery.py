import os

import psutil

class ReplaySorcery(object):
    def __init__(self):
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
        print("Getting current ReplaySorcery status: ", end="")

        process_found = False
        for proc in psutil.process_iter(["name"]):
            if "replay-sorcery" in proc.info["name"]:
                process_found = True
                self.current_status = self._statuses["on"]
                break

        if not process_found:
            self.current_status = self._statuses["off"]

        print(self.current_status["name"])

    def turn_on(self):
        print("Turning ReplaySorcery on")

        os.system(self._systemd_command % "enable")

        self.get_status()

    def turn_off(self):
        print("Turning ReplaySorcery off")
        
        os.system(self._systemd_command % "disable")

        self.get_status()