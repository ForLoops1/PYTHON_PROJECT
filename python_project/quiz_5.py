import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox


class Quiz4(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("quiz_4.ui", self)

        self.nextButton.clicked.connect(self.check_answer)
        self.back_button.clicked.connect(self.go_back)

    def check_answer(self):
        if self.radioButton_D.isChecked():  # Correct answer
            QMessageBox.information(self, "Correct", "Correct answer!")
            self.go_next()
        else:
            QMessageBox.warning(self, "Incorrect", "That is not the correct answer.")

    def go_next(self):
        self.quiz5 = Quiz5()
        self.quiz5.show()
        self.close()

    def go_back(self):
        # If needed, implement back logic (e.g., open quiz_3)
        self.close()


class Quiz5(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("quiz_5.ui", self)

        self.nextButton.clicked.connect(self.check_answer)
        self.back_button.clicked.connect(self.go_back)

    def check_answer(self):
        if self.radioButton_C.isChecked():  # Correct answer
            QMessageBox.information(self, "Correct", "Correct answer!")
            self.go_next()
        else:
            QMessageBox.warning(self, "Incorrect", "That is not the correct answer.")

    def go_next(self):
        # You can replace this with loading quiz_6.ui
        QMessageBox.information(self, "Next", "Moving to the next quiz (quiz_6).")
        self.close()

    def go_back(self):
        self.quiz4 = Quiz4()
        self.quiz4.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Quiz4()
    window.show()
    sys.exit(app.exec())
