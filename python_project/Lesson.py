import sys
from PyQt6 import QtWidgets, uic

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = uic.loadUi("PYLearn\Lesson.ui")
    window.show()
    sys.exit(app.exec()) 