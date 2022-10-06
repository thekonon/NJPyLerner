import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPalette
                                                     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    label = QLabel("Hello World", alignment=Qt.AlignCenter)
    my_BG = QPalette('red')
    label.setPalette(my_BG)
    label.show()
    sys.exit(app.exec())