from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
from random import randint

def show_winner():
    num = randint(0,9)
    winner.setText(str(num))
    
    num2 = randint(0,9)
    win.setText(str(num2))
    if num == num2:
        text.setText("Ви виграли! Зіграйте знову")
    else:
        text.setText("Ви програли! Зіграйте знову")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Лотерея")
window.move(100,100)
window.resize(400,400)

button = QPushButton("Випробувати удачу")
text = QLabel("Натисни, щоб взяти участь")
winner = QLabel("?")
win = QLabel("?")

line = QVBoxLayout()
line.addWidget(text,alignment= Qt.AlignCenter)
line.addWidget(winner,alignment= Qt.AlignCenter)
line.addWidget(win,alignment= Qt.AlignCenter)
line.addWidget(button,alignment= Qt.AlignCenter)
window.setLayout(line)

button.clicked.connect(show_winner)

window.show()
app.exec_()