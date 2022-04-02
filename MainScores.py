from flask import Flask
import os
app = Flask(__name__)

err_file = 'templates/html_file_error.html'
win_file = 'templates/html_file_win.html'


def score_server():
    try:
        f_res = open('Scores.txt', 'r')
        score = f_res.read()
        f_res.close()
        return int(score)
    except IOError as e:
        return repr(e)


@app.route("/", methods=['GET'])
def index():
    res_score = score_server()
    try:
        success = int(res_score)
        content_tmplt = open(os.path.join(os.getcwd(), win_file), 'r')
        _str = content_tmplt.read()
        _str = _str.replace('{SCORE}', str(res_score))
        print(_str)
    except ValueError as e:
        content_tmplt = open(os.path.join(os.getcwd(), err_file), 'r')
        _str = content_tmplt.read()
        _str = _str.replace('{ERROR}', str(res_score))
        print(_str)
    return _str


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
