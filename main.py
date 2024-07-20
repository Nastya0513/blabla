from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint

app = QApplication([]) #створюємо програму 

main_win = QWidget()
main_win.setWindowTitle('Визначений переможця')
main_win.resize(400,200)

# кнопка
button = QPushButton('Згенерувати')
text = QLabel('Натисніть,щоб дізнатись переможця')
winner = QLabel('?')

# розташування

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
main_win.setLayout(line)

def random():
    number = randint(0,99)
    winner.setText(str(number))
    text.setText('Переможець:')

button.clicked.connect(random)

main_win.show()
app.exec()
