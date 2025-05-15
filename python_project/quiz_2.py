import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class Quiz2(QtWidgets.QWidget):
    def __init__(self, stack):
        super().__init__()
        uic.loadUi("quiz_2.ui", self)
        self.stack = stack
        self.nextButton.clicked.connect(self.go_to_quiz3)
        self.back_button.clicked.connect(self.go_to_quiz1)

    def go_to_quiz3(self):
        if self.findChild(QtWidgets.QRadioButton, "radioButton_C").isChecked():
            QMessageBox.information(self, "Result", "Correct!")
            self.stack.setCurrentIndex(2)  # Go to quiz_3
        else:
            QMessageBox.warning(self, "Result", "Incorrect. Try again.")

    def go_to_quiz1(self):
        self.stack.setCurrentIndex(0)  # Go back to quiz_1

class Quiz1(QtWidgets.QWidget):
    def __init__(self, stack):
        super().__init__()
        uic.loadUi("quiz_1.ui", self)
        self.stack = stack
        self.nextButton.clicked.connect(self.go_to_quiz2)
        self.back_button.clicked.connect(self.go_back)

    def go_to_quiz2(self):
        # You can also check answer here if needed
        self.stack.setCurrentIndex(1)  # Move to quiz_2

    def go_back(self):
        print("Already at the first quiz!")

class Quiz3(QtWidgets.QWidget):
    def __init__(self, stack):
        super().__init__()
        uic.loadUi("quiz_3.ui", self)
        self.stack = stack
        self.back_button.clicked.connect(self.go_to_quiz2)

    def go_to_quiz2(self):
        self.stack.setCurrentIndex(1)  # Go back to quiz_2

def main():
    app = QtWidgets.QApplication(sys.argv)

    stack = QtWidgets.QStackedWidget()
    quiz1 = Quiz1(stack)
    quiz2 = Quiz2(stack)
    quiz3 = Quiz3(stack)

    stack.addWidget(quiz1)  # Index 0
    stack.addWidget(quiz2)  # Index 1
    stack.addWidget(quiz3)  # Index 2

    stack.setFixedSize(562, 701)
    stack.setWindowTitle("Python Quiz")
    stack.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
