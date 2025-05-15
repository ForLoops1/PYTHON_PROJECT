import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox


class Quiz3(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("quiz_3.ui", self)

        self.nextButton.clicked.connect(self.check_answer)
        self.back_button.clicked.connect(self.go_back)

    def check_answer(self):
        if self.radioButton_B_2.isChecked():  # Correct answer: B (KeyError)
            QMessageBox.information(self, "Correct", "Correct answer!")
            self.go_next()
        else:
            QMessageBox.warning(self, "Incorrect", "That is not the correct answer.")

    def go_next(self):
        self.quiz4 = Quiz4()
        self.quiz4.show()
        self.close()

    def go_back(self):
        # Add Quiz2 if needed
        self.close()


class Quiz4(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("quiz_4.ui", self)

        self.nextButton.clicked.connect(self.check_answer)
        self.back_button.clicked.connect(self.go_back)

    def check_answer(self):
        # You can update the correct answer logic for quiz 4 here
        QMessageBox.information(self, "Info", "Add correct answer logic for Quiz 4.")
        self.close()

    def go_back(self):
        self.quiz3 = Quiz3()
        self.quiz3.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Quiz3()
    window.show()
    sys.exit(app.exec())
