import personal_settings
from game_functions import adventures_run, play_from_main_menu, game, menu_actions
from utility_functions import check_client_active, check_text, run_hs, terminate_client


while True:
    if not check_client_active():
        if check_text('режимы', 630, 390, 110, 20, 17, 0, 0, 90, 163, 140, False):
            play_from_main_menu()
            adventures_run()
        else:
            adventures_run()
    else:
        run_hs()
        if check_text('режимы', 630, 390, 110, 20, 17, 0, 0, 90, 163, 140, False):
            play_from_main_menu()
            adventures_run()
        else:
            game()
            menu_actions()
    terminate_client()
