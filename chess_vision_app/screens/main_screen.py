import PySimpleGUI as sg


def main_screen():
    main_screen_layout = [
        [sg.Text("Chess Vision Training App", justification="center",
                 size=(20, 1), font=("arial", 25))],
        [sg.Button("Start", font=("arial", 12),
                   size=(6, 1), pad=(160, 25))],
        [sg.Button("Close", font=("arial", 12),
                   size=(6, 1), pad=(160, 10))],
    ]
    return main_screen_layout
