
from PyQt5.QtCore import QThread
import pyautogui
import time












# QThread subclass for managing automatic clicking.

class ClickerThread(QThread):
    def __init__(self):
        super().__init__()
        self.running = False
        self.interval = 45
        self.positions = [(0, 0)]
        pyautogui.FAILSAFE = False

    def run(self):
        while self.running:
            for position in self.positions:
                if not self.running:
                    break
                time.sleep(self.interval)
                pyautogui.click(*position)


    def start_clicking(self, interval, positions):
        self.interval = interval
        self.positions = positions
        self.running = True
        self.start()

    def stop_clicking(self):
        self.running = False
