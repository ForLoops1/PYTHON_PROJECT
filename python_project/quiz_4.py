import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox


class Quiz1(QtWidgets.QWidget):
    def __init__(self, stack):
        super().__init__()
        uic.loadUi("quiz_1.ui", self)
        self.stack = stack
        self.nextButton.clicked.connect(self.go_to_quiz2)

    def go_to_quiz2(self):
        self.stack.setCurrentIndex(1)


class Quiz2(QtWidgets.QWidget):
    def __init__(self, stack):
        super().__init__()
        uic.loadUi("quiz_2.ui", self)
        self.stack = stack
        self.back_button.clicked.connect(self.go_to_quiz1)
        self.nextButton.clicked.connect(self.check_answer)

    def go_to_quiz1(self):
        self.stack.setCurrentIndex(0)

    def check_answer(self):
        if self.findChild(QtWidgets.QRadioButton, "radioButton_C").isChecked():
            QMessageBox.information(self, "Result", "Correct!")
            self.stack.setCurrentIndex(2)
        else:
            QMessageBox.warning(self, "Result", "Incorrect. Try again.")


class Quiz3(QtWidgets.QWidget):
    def __init__(self, stack):
        super().__init__()
        uic.loadUi("quiz_3.ui", self)
        self.stack = stack
        self.back_button.clicked.connect(self.go_to_quiz2)
        self.nextButton.clicked.connect(self.check_answer)

    def go_to_quiz2(self):
        self.stack.setCurrentIndex(1)

    def check_answer(self):
        if self.findChild(QtWidgets.QRadioButton, "radioButton_B").isChecked():
            QMessageBox.information(self, "Result", "Correct!")
            self.stack.setCurrentIndex(3)
        else:
            QMessageBox.warning(self, "Result", "Incorrect. Try again.")


class Quiz4(QtWidgets.QWidget):
    def __init__(self, stack):
        super().__init__()
        uic.loadUi("quiz_4.ui", self)
        self.stack = stack
        self.back_button.clicked.connect(self.go_to_quiz3)
        self.nextButton.clicked.connect(self.check_answer)

    def go_to_quiz3(self):
        self.stack.setCurrentIndex(2)

    def check_answer(self):
        if self.findChild(QtWidgets.QRadioButton, "radioButton_D").isChecked():
            QMessageBox.information(self, "Result", "Correct!")
            self.stack.setCurrentIndex(4)
        else:
            QMessageBox.warning(self, "Result", "Incorrect. Try again.")


class Quiz5(QtWidgets.QWidget):
    def __init__(self, stack):
        super().__init__()
        uic.loadUi("quiz_5.ui", self)
        self.stack = stack
        self.back_button.clicked.connect(self.go_to_quiz4)

    def go_to_quiz4(self):
        self.stack.setCurrentIndex(3)


def main():
    app = QtWidgets.QApplication(sys.argv)

    stack = QtWidgets.QStackedWidget()
    quiz1 = Quiz1(stack)
    quiz2 = Quiz2(stack)
    quiz3 = Quiz3(stack)
    quiz4 = Quiz4(stack)
    quiz5 = Quiz5(stack)

    stack.addWidget(quiz1)  # index 0
    stack.addWidget(quiz2)  # index 1
    stack.addWidget(quiz3)  # index 2
    stack.addWidget(quiz4)  # index 3
    stack.addWidget(quiz5)  # index 4

    stack.setFixedSize(567, 719)
    stack.setWindowTitle("PYLearn - Python Quiz")
    stack.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
