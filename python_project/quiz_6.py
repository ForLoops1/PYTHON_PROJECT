import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox


class Quiz5(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("quiz_5.ui", self)

        self.nextButton.clicked.connect(self.check_answer)
        self.back_button.clicked.connect(self.go_back)

    def check_answer(self):
        if self.radioButton_C.isChecked():  # Correct answer is C
            QMessageBox.information(self, "Correct", "Correct answer!")
            self.go_next()
        else:
            QMessageBox.warning(self, "Incorrect", "That is not the correct answer.")

    def go_next(self):
        self.quiz6 = Quiz6()
        self.quiz6.show()
        self.close()

    def go_back(self):
        # If you have quiz_4, you can load it here
        self.close()


class Quiz6(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("quiz_6.ui", self)

        self.nextButton.clicked.connect(self.check_answer)
        self.back_button.clicked.connect(self.go_back)

    def check_answer(self):
        if self.radioButton_D.isChecked():  # Correct answer is D: snake_case
            QMessageBox.information(self, "Correct", "Correct answer!")
            self.go_next()
        else:
            QMessageBox.warning(self, "Incorrect", "That is not the correct answer.")

    def go_next(self):
        # You can implement Quiz7 here
        QMessageBox.information(self, "Next", "Moving to the next quiz (quiz_7.ui).")
        self.close()

    def go_back(self):
        self.quiz5 = Quiz5()
        self.quiz5.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Quiz5()
    window.show()
    sys.exit(app.exec())
