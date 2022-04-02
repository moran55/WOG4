import random
import sys
import os
import time
import Utils as u_p

g_difficulty = -1  # default value


def generate_sequence():
    global g_difficulty
    num_list = []
    list_len = g_difficulty
    while len(num_list) < list_len:
        try:
            ran_num = random.randrange(1, 101)
            if ran_num not in num_list:
                num_list.append(ran_num)
        except Exception as e:
            print(e)
    return num_list


def get_list_from_user():
    global g_difficulty
    num_list = []
    list_len = g_difficulty
    print('Please provide the numbers you saw: ')
    while len(num_list) < list_len:
        try:
            if len(num_list) >= 1:
                print('Please provide another number:')
            user_num = int(input())
            if user_num not in num_list:
                num_list.append(user_num)
            else:
                print('You chose this number previously.')
        except ValueError as e:
            print('You need to provide a numeric value...')
            continue
    return num_list


def is_list_equal(user_input, sys_input):
    user_input.sort()
    sys_input.sort()
    if user_input == sys_input:
        return True
    else:
        return False


def play():
    sys_nums = generate_sequence()
    print(f'The numbers you need to remember are: {sys_nums}')
    time.sleep(0.7)
    u_p.clear_console()
    user_nums = get_list_from_user()
    equal_stat = is_list_equal(user_nums, sys_nums)
    if equal_stat:
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
