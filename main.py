from typing import Text
import PySimpleGUI as gui
import time

val = int(0)
cps = int(0)

layout = [[gui.Button("Add 1")],[gui.Text(str(val), key='count')],[gui.Text('CPS: '+str(cps), key='cpscount')]]
window = gui.Window("Hello World", layout, margins=(100, 50))
while True:
    event, values = window.read()
    if event == "Add 1":
        val = val + int(1)
        window['count'].update(val)
        window['cpscount'].update('CPS: ' + str(cps))
    if event == gui.WIN_CLOSED:
        break
