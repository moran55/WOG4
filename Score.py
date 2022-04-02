import Utils as u
import os

total_score = 0
POINTS_OF_WINNING = 0


def add_score(difficulty):
    points_to_add = (difficulty*3)+5
    try:
        score_file = open(u.SCORES_FILE_NAME, 'r')
        content = score_file.read()
        if content:
            _sum = int(content) + points_to_add
            content = str(_sum)
            open(u.SCORES_FILE_NAME, 'w').write(content)
    except IOError as e:
        score_file = open(u.SCORES_FILE_NAME, 'w')
        score_file.write(str(points_to_add))
    finally:
        score_file.close()
    return True


