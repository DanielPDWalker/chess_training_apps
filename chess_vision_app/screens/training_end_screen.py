import PySimpleGUI as sg


def training_end_screen(correct, total_questions):

    training_end_screen_layout = [
        [sg.Text(f"You scored {correct}/{total_questions}", justification="center",
                 font=("arial", 25), size=(10, 2), key='score_text')],
        [
            sg.Button("Re-Start", font=("arial", 12),
                      size=(10, 1)),
            sg.Button("Main Menu", font=("arial", 12),
                      size=(10, 1))],
        [sg.Button("Close", font=("arial", 12),
                   size=(5, 1))]
    ]

    return training_end_screen_layout
