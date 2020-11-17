import PySimpleGUI as sg
import random as r

from squares_data import all_squares_list


def training_screen():
    chosen_square = training_screen_new_question()

    training_screen_layout = [
        [sg.Text(chosen_square, justification="center",
                 font=("arial", 25), size=(10, 2), key='q')],
        [
            sg.Button("Dark", font=("arial", 12),
                      size=(6, 1)),
            sg.Button("Light", font=("arial", 12),
                      size=(6, 1))],
        [sg.Button("Close", font=("arial", 12),
                   size=(5, 1))]
    ]

    return training_screen_layout, chosen_square


def training_screen_new_question():
    return r.choice(all_squares_list)
