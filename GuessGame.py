import random
import sys
import Utils as u_p

g_difficulty = -1  # default value
g_secret_number = -1


def generate_number():
    global g_secret_number, g_difficulty
    g_secret_number = random.randrange(1, g_difficulty)
    print(g_secret_number)
    return True


def get_guess_from_user():
    global g_difficulty
    print(f'Please chose a number between 1 to {g_difficulty}')
    bool_flag = False
    while not bool_flag:
        try:
            user_input = int(input())
            if user_input > g_difficulty or user_input < 1:
                print(f"Please provide a number between 1 and {g_difficulty}")
                continue
            bool_flag = True
        except ValueError as e:
            print("You need to provide a number, please try again")
    return user_input


def compare_results(num):
    global g_secret_number
    if num == g_secret_number:
        return True
    return False


def play():
    generate_number()
    user_num = get_guess_from_user()
    res_game = compare_results(user_num)
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
