from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget
from PyQt5 import QtGui
import random
import os
import time

ROWS = 4
COLUMNS = 4
PIC_PATH = "./pics"

selected_tile = None

def tile_clicked(button):
    idx = buttons.index(button)
    x = 0
    y = 0
    while idx > 0:
        if idx > 4:
            x = x + 1
            idx = idx - 4
        else:
            y = y + 1
            idx = idx - 1
    if selected_tile == None:
        selected_tile = [pics[idx], x, y]
        layout.addWidget(buttons[idx], x, y)
    else:
        if selected_tile[0] == pics[idx]:
            layout.addWidget(buttons[idx], x, y)
        else:
            layout.addWidget(buttons[idx], x, y)
            time.sleep(1)
            layout.addWidget(buttons_hidden[idx], selected_tile[0], selected_tile[1])
            layout.addWidget(buttons_hidden[idx], x, y)

 
app = QApplication([])
window = QWidget()
layout = QGridLayout();
pics = []

for pic in os.listdir(PIC_PATH):
    pics.append(os.path.join("./pics", pic))

pics = pics*2
print(pics)
random.shuffle(pics)

buttons = []
buttons_hidden = []
for icon in pics:
    ic = QtGui.QPixmap(os.path.realpath(str(icon)))
    button = QPushButton()
    hid_button = QPushButton()
    button.setIcon(QtGui.QIcon(ic))
    buttons.append(button)
    buttons_hidden.append(hid_button)

a = 0
for x in range(0,ROWS):
    for y in range(0,COLUMNS):
        layout.addWidget(buttons_hidden[a], x, y)
        a = a + 1
window.setLayout(layout)
window.show()
tile_clicked(buttons[6])
app.exec_()

