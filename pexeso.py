import os
import random
from functools import partial

from PyQt5 import QtGui
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

ROWS = 4
COLUMNS = 4
#adresar s obrazky (min pocet ROWS*COLUMNS/2)
PIC_PATH = "./pics"

selected_tile = None
in_timeout = False

def tile_clicked(idx, button, icon):
    global selected_tile, in_timeout

    print(idx)
    x = idx // 4
    y = idx % 4
    print(x, y)
    if in_timeout: return
    button.setIcon(QtGui.QIcon(icon))

    if selected_tile is None:
        selected_tile = button
    else:
        if selected_tile.icon != button.icon:
            in_timeout = True
            loop = QEventLoop()
            QTimer.singleShot(500, loop.quit)
            loop.exec_()
            selected_tile.setIcon(QtGui.QIcon(None))
            button.setIcon(QtGui.QIcon(None))
            selected_tile = None
            in_timeout = False
        else:
            button.setEnabled(False)
            selected_tile.setEnabled(False)
            selected_tile = None

app = QApplication([])
window = QWidget()
layout = QGridLayout()
pics = []

for pic in os.listdir(PIC_PATH):
    pics.append(os.path.join("./pics", pic))

pics = pics * 2
random.shuffle(pics)

buttons = []
for i, icon in enumerate(pics):
    ic = QtGui.QPixmap(os.path.realpath(str(icon)))
    button = QPushButton(window)
    x = i
    button.icon = icon
    button.clicked.connect(partial(tile_clicked, x, button, ic))
    layout.addWidget(button, i // 4, i % 4)
    buttons.append(button)

window.setLayout(layout)
window.show()
app.exec_()
