from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QCheckBox, QMessageBox
from PyQt5.QtCore import QThread
import pyautogui
from Threads.ClickerThread import ClickerThread




# Function to check if a click position is within the screen boundaries.

def is_valid_position(position):
    screen_width, screen_height = pyautogui.size()
    x, y = position
    return 0 <= x < screen_width and 0 <= y < screen_height





class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        
        layout = QVBoxLayout()

        self.interval_label = QLabel("Intervalo en segundos:", self)
        layout.addWidget(self.interval_label)

        self.interval_input = QLineEdit(self)
        self.interval_input.setText("45")
        layout.addWidget(self.interval_input)

        self.position_labels = []
        self.x_position_inputs = []
        self.y_position_inputs = []
        self.check_boxes = []

        for i in range(1, 5):
            position_label = QLabel(f"Posición del click {i} (x, y):", self)
            layout.addWidget(position_label)
            self.position_labels.append(position_label)

            position_layout = QHBoxLayout()

            check_box = QCheckBox(self)
            position_layout.addWidget(check_box)
            self.check_boxes.append(check_box)

            x_position_input = QLineEdit(self)
            x_position_input.setPlaceholderText("x")
            position_layout.addWidget(x_position_input)
            self.x_position_inputs.append(x_position_input)

            y_position_input = QLineEdit(self)
            y_position_input.setPlaceholderText("y")
            position_layout.addWidget(y_position_input)
            self.y_position_inputs.append(y_position_input)

            layout.addLayout(position_layout)

        self.start_button = QPushButton('Iniciar clicks', self)
        self.start_button.clicked.connect(self.start_clicking)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton('Parar clicks', self)
        self.stop_button.clicked.connect(self.stop_clicking)
        layout.addWidget(self.stop_button)

        self.status_label = QLabel("Estado: No está clickando.", self)
        layout.addWidget(self.status_label)


        self.clicker_thread = ClickerThread()

        self.setLayout(layout)
        self.setWindowTitle('Clicks automáticos')
        self.show()

    def is_valid_position(position):
        screen_width, screen_height = pyautogui.size()
        x, y = position
        return 0 <= x < screen_width and 0 <= y < screen_height

    def start_clicking(self):
        interval = int(self.interval_input.text())
        if interval < 5:
            QMessageBox.warning(self, "Warning", "Por razones de seguridad, el intervalo de clicks no puede ser inferior a 5 segundos.")
            return
        positions = []

        for check_box, x_input, y_input in zip(self.check_boxes, self.x_position_inputs, self.y_position_inputs):
            if check_box.isChecked():
                x = int(x_input.text()) if x_input.text() else 0
                y = int(y_input.text()) if y_input.text() else 0
                position = (x, y)

                if is_valid_position(position):
                    positions.append(position)

        self.clicker_thread.start_clicking(interval, positions)
        self.status_label.setText("Estado: Clickando ...") # Update status to "Clicking"

    def stop_clicking(self):
        self.clicker_thread.stop_clicking()
        self.status_label.setText("Estado: No está clickando.") # Update status to "Not Clicking"
