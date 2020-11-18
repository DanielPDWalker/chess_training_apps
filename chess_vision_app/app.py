import PySimpleGUI as sg


from screens.main_screen import main_screen
from screens.training_active_screen import training_active_screen, training_active_screen_new_question
from screens.training_end_screen import training_end_screen
from squares_data import dark, light


layout = main_screen()
window = sg.Window("Chess Vision Training App", layout)
app_running = True

while app_running:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    if event == "Start" or "Re-Start":
        window.close()
        layout, chosen_square = training_active_screen()
        window = sg.Window("Chess Vision Training App", layout, finalize=True)

        training_question_count = 0
        correct = 0

        event, values = window.read()

    if event == "Dark" or "Light":
        while training_question_count < 20:
            if event == "Close" or event == sg.WIN_CLOSED:
                break
            chosen_square_color = event
            if chosen_square in dark:
                correct_square_color = 'Dark'
            else:
                correct_square_color = 'Light'
            if chosen_square_color == correct_square_color:
                correct += 1
            training_question_count += 1
            chosen_square = training_active_screen_new_question()
            window['q'].update(value=chosen_square)
            event, values = window.read()
        else:
            if event == "Close" or event == sg.WIN_CLOSED:
                break
            window.close()
            layout = training_end_screen(correct, training_question_count)
            window = sg.Window("Chess Vision Training App",
                               layout, finalize=True)

    if event == "Main Menu":
        window.close()
        layout = main_screen()
        window = sg.Window("Chess Vision Training App", layout)
