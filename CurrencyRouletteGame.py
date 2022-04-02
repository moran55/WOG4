import random
import sys
from currency_converter import CurrencyConverter
import Utils as u_p

g_difficulty = -1  # default value


def init():
    ran_num = random.randrange(1, 100)
    c = CurrencyConverter()
    curr = c.convert(1, 'USD', 'ILS')
    t = ran_num * curr
    return t


def get_money_interval(num):
    global g_difficulty
    interval = [num - (5-g_difficulty), num + (5 - g_difficulty)]
    return interval


def get_guess_from_user():
    print(f'Please chose a number:')
    bool_flag = False
    while not bool_flag:
        try:
            user_input = int(input())
            bool_flag = True
        except ValueError as e:
            print("You need to provide a number, please try again")
    return user_input


def check_if_num_in_range(_range, num):
    _range.sort()
    if _range[0] <= num <= _range[1]:
        return True
    return False


def play():
    t = init()
    interval = get_money_interval(t)
    user_guess = get_guess_from_user()
    res_game = check_if_num_in_range(interval, user_guess)
    if res_game:
        stat_msg = 'You Won!!!'
        stat = True
    else:
        stat_msg = 'You lose, try again next time :)'
        stat = False
    return stat, stat_msg


def main(diff):
    global g_difficulty
    g_difficulty = diff
    res = play()
    u_p.clear_console()
    return res


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        difficulty = int(arg)
    main(difficulty)

