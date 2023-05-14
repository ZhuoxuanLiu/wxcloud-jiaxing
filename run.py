from flask import Flask, request, jsonify
from robot import myrobot
from werobot.contrib.flask import make_view

app = Flask(__name__)
app.add_url_rule(rule='/robot/', # WeRoBot 挂载地址
                 endpoint='werobot', # Flask 的 endpoint
                 view_func=make_view(myrobot),
                 methods=['GET', 'POST'])

@app.before_request
def check_health():
    if request.method == 'POST' and request.path == '/' and request.is_json:
        data = request.get_json()
        action = data.get('action')
        if action == 'CheckContainerPath':
            # 在这里处理 CheckContainerPath 的逻辑
            return 'success'

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)