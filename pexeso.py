from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget
from PyQt5 import QtGui
from pathlib import Path
import random
import os

ROWS = 4
COLUMNS = 4

selected_tile = None

app = QApplication([])
window = QWidget()
layout = QGridLayout();

path = Path("./pics").glob('**/*')
pics = [(x for x in path if x.is_file())]
print(pics)
random.shuffle(pics)
a = 0
buttons = []
for icon in pics:
    ic = QtGui.QPixmap(os.path.realpath(str(icon)))
    button = QPushButton()
    a = a + 1
    print(a)
    button.setIcon(QtGui.QIcon(ic))
    buttons.append(button)
   


for x in range(0,ROWS):
    for y in range(0,COLUMNS):
        layout.addWidget(buttons.pop(0),x,y)
window.setLayout(layout)
window.show()
app.exec_()

def tileClick():
    #set selected tile
    #
