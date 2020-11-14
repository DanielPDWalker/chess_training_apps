import PySimpleGUI as sg
from screens.main_screen import main_screen
from screens.training_screen import training_screen


layout = main_screen()
window = sg.Window("Chess Vision Training App", layout)
app_running = True

while app_running:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    if event == "Start":
        layout = training_screen()
        window = sg.Window("Chess Vision Training App", layout)
