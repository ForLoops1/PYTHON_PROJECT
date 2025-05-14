import sys
from PyQt6 import QtWidgets, uic

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = uic.loadUi("multipleChoices.ui")

    # === Set your question and options dynamically ===
    # You must know the object names set in Qt Designer for the QLabel and QRadioButtons.
    # Let's assume:
    # QLabel for question → objectName: questionLabel
    # QRadioButton options → objectNames: optionA, optionB, optionC, optionD

    window.findChild(QtWidgets.QLabel, "questionLabel").setText("What is the output of print(2 ** 3)?")
    window.findChild(QtWidgets.QRadioButton, "optionA").setText("A. 6")
    window.findChild(QtWidgets.QRadioButton, "optionB").setText("B. 8")
    window.findChild(QtWidgets.QRadioButton, "optionC").setText("C. 9")
    window.findChild(QtWidgets.QRadioButton, "optionD").setText("D. Error")

    # === Show window ===
    window.show()
    sys.exit(app.exec())
