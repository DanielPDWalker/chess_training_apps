import PySimpleGUI as sg


def main_screen():
    app_description = """This app is a mini quiz on what color the squares of a chess board are. 
    
    You will be shown 20 random squares in algebraic notation, and you will have to decide if they are light or dark squares."""
    main_screen_layout = [
        [sg.Text("Chess Vision Training App", justification="center",
                 size=(20, 1), font=("arial", 25))],
        [sg.Text(app_description, justification="center",
                 font=("arial", 12), size=(40, 6))],
        [sg.Button("Start", font=("arial", 12),
                   size=(6, 1), pad=(160, 15))],
        [sg.Button("Close", font=("arial", 12),
                   size=(6, 1), pad=(160, 10))],
    ]
    return main_screen_layout
