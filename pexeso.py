import os
import random
from functools import partial

from PyQt5 import QtGui
from PyQt5.QtCore import QEventLoop, QTimer, QSize
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

#počet řádků
ROWS = 4
#počet sloupců
COLUMNS = 4
#adresář s obrázky (min pocet ROWS*COLUMNS/2)
PIC_PATH = "./pics"
#čas zobrazení špatného páru v ms
SHOW_TIME = 500

selected_tile = None
in_timeout = False

#click handler (idx = index buttonu v  poli, button, icon = ikona/obrázek a buttonu)
def tile_clicked(idx, button, icon):
    global selected_tile, in_timeout

    print(idx)
    #zjištění souřadnic buttonu
    x = idx // 4
    y = idx % 4
    print(x, y)
    if in_timeout: return
    #zobrazení obrázku
    button.setIcon(QtGui.QIcon(icon))

    #pokud neni zadne policko otevrene, ulozi se
    if selected_tile is None:
        selected_tile = button
    #pokud uz jedno otevrene je, srovnaji se jejich obrazky -> pokud jsou stene, tlacitka se vypnou, pokud ne,
    # zustanou otevrena SHOW_TIME milisekund a pak se zavrou
    else:
        #pokud obrazky nejsou stejne
        if selected_tile.icon != button.icon:
            #timeout check
            in_timeout = True
            #timer
            loop = QEventLoop()
            QTimer.singleShot(SHOW_TIME, loop.quit)
            loop.exec_()
            #"schovani policek"
            selected_tile.setIcon(QtGui.QIcon(None))
            button.setIcon(QtGui.QIcon(None))
            selected_tile = None
            in_timeout = False
            #pokud jsou stejne
        else:
            #vypnuti tlacitek
            button.setEnabled(False)
            selected_tile.setEnabled(False)
            selected_tile = None

#definice onka aplikace
app = QApplication([])
window = QWidget()
layout = QGridLayout()
#pole nactenych obrazku z adresare
pics = []

#cteni obrazku ze slozky PIC_PATH
for pic in os.listdir(PIC_PATH):
    pics.append(os.path.join("./pics", pic))

#double pole obrázků (na pexeso jsou potreba od kazdeho 2)
pics = pics * 2
#zamichani
random.shuffle(pics)

#pole tlacitek(policek)
buttons = []
#vytvoreni layoutu okna  buttonu, prirazni obrazku k buttonum
for i, icon in enumerate(pics):
    #vytvoreni ikony pro tlacitko
    ic = QtGui.QPixmap(os.path.realpath(str(icon)))
    #vytvoreni buttonu
    button = QPushButton(window)
    #nastaveni velikosti
    btn_size = QSize()
    btn_size.setHeight(50)
    btn_size.setWidth(50)
    button.setFixedSize(btn_size)
    button.setIconSize(btn_size)
    x = i
    button.icon = icon
    #pripjeni funcke na handling clicku
    button.clicked.connect(partial(tile_clicked, x, button, ic))
    #umisteni tlacitka do okna
    layout.addWidget(button, i // 4, i % 4)
    buttons.append(button)

#zobrazeni okna a spusteni aplikace
window.setLayout(layout)
window.show()
app.exec_()
