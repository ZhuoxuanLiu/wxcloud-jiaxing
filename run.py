from flask import Flask
from robot import myrobot
from werobot.contrib.flask import make_view

app = Flask(__name__)
app.add_url_rule(rule='/robot/', # WeRoBot 挂载地址
                 endpoint='werobot', # Flask 的 endpoint
                 view_func=make_view(myrobot),
                 methods=['GET', 'POST'])

@app.route('/', methods=['GET', 'POST'])
def check_health():
    return 'success'

app.run(host='0.0.0.0', port=80, debug=False)