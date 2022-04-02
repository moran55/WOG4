from live import welcome, load_game


def main():
    welcome('Moran')
    stat, msg = load_game()
    print(msg)


if __name__ == '__main__':
    main()
