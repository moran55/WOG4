import CurrencyRouletteGame as CR_G
import GuessGame as G_G
import MemoryGame as M_G
import Score as s


def welcome(name):
    print(f'Hello {name} and welcome to the World Of Games (WOG). \nHere you can find '
          f'many cool games you can play')


games_dict = {
    1: 'Memory game',
    2: 'Guess game',
    3: 'Currency Roulette game'
}


def load_game():
    try:
        print('Please choose a game to play:\n'
              '1. Memory Game - a sequence of numbers will appear for 1 second '
              'and you have to guess it back.\n'
              '2. Guess Game - guess a number and see if you chose like the computer.\n'
              '3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n')
        print('Please choose the number of game you want to play...')
        b_g_input = False
        numeric_choice = -1
        while not b_g_input:
            user_game_input = input()
            try:
                numeric_choice = int(user_game_input)
            except ValueError as e:
                print('You need to provide a numeric value...')
                continue
            if not 0 < numeric_choice < 4:
                print('Please choose a valid game number between 1 to 3')
                continue
            b_g_input = True
        print('You chose: ' + games_dict[numeric_choice] + '!')
        b_d_input = False
        print('Please choose game difficulty from 1 to 5:')
        while not b_d_input:
            user_diff_input = input()
            try:
                numeric_diff = int(user_diff_input)
            except ValueError as e:
                print('You need to provide a numeric value...\n '
                      'Please try again and choose a number between 1 to 5')
                continue
            if not 0 < numeric_diff < 6:
                print('Please choose a valid difficulty level between 1 to 5')
                continue
            b_d_input = True
        print('You chose difficulty level: ' + user_diff_input + '!')
        if numeric_choice == 1:
            res_stat, res_game = M_G.main(numeric_diff)
        elif numeric_choice == 2:
            res_stat, res_game = G_G.main(numeric_diff)
        elif numeric_choice == 3:
            res_stat, res_game = CR_G.main(numeric_diff)
        if res_stat:
            s.add_score(numeric_diff)
    except Exception as e:
        return False, f'There was an error {e}'
    return True, res_game
