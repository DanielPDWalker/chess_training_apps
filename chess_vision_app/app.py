import PySimpleGUI as sg


from screens.main_screen import main_screen
from screens.training_screen import training_screen, training_screen_new_question
from squares_data import dark, light


layout = main_screen()
window = sg.Window("Chess Vision Training App", layout)
app_running = True

while app_running:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    if event == "Start":
        window.close()
        layout, chosen_square = training_screen()
        window = sg.Window("Chess Vision Training App", layout, finalize=True)

        training_question_count = 0
        correct = 0
        incorrect = 0

        event, values = window.read()

    if event == "Dark" or "Light":
        while training_question_count < 20:
            chosen_square_color = event
            if chosen_square_color in dark:
                correct_square_color = 'Dark'
            else:
                correct_square_color = 'Light'
            if chosen_square_color == correct_square_color:
                correct += 1
            else:
                incorrect += 1
            training_question_count += 1
            chosen_square = training_screen_new_question()
            window['q'].update(value=chosen_square)
            event, values = window.read()
        else:
