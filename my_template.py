import sys

import PySide6.QtWidgets as Qt


# Subclass QMainWindow to customize your application's main window
class MainWindow(Qt.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = Qt.QVBoxLayout()
        widgets = [
            Qt.QCheckBox,
            Qt.QComboBox,
            Qt.QDateEdit,
            Qt.QDateTimeEdit,
            Qt.QDial,
            Qt.QDoubleSpinBox,
            Qt.QFontComboBox,
            Qt.QLCDNumber,
            Qt.QLabel,
            Qt.QLineEdit,
            Qt.QProgressBar,
            Qt.QPushButton,
            Qt.QRadioButton,
            Qt.QSlider,
            Qt.QSpinBox,
            Qt.QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = Qt.QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = Qt.QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()