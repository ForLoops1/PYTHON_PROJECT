import sys
from PyQt6 import QtWidgets, uic

class FirstPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Quiz.ui", self)  # adjust filename if needed

        # Connect the button to the method
        self.nextButton.clicked.connect(self.open_multiple_choices)

    def open_multiple_choices(self):
        self.multiple_choice_window = MultipleChoicesPage()
        self.multiple_choice_window.show()
        self.close()  # or self.hide() if you want to come back

class MultipleChoicesPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"multipleChoices.ui", self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FirstPage()
    window.show()
    sys.exit(app.exec())
