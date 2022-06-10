import flask.cli
from flask import Flask, abort, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/homepage')
@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/getagent')
def get_agent():
    user_agent = request.headers.get('User-agent')
    return '<p>browser is %s</p>' % user_agent


@app.route('/404')
def badrq():
    # return '<h1>bad request</h1>', 400
    response = make_response('<h1>a cokie</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# @app.route('/user/<id>')
# def get_user(id):
#     user=laod_user(id)
#     if not user:
#         abort(404)
#     return '<h1>hell ,%s</h1>'% user.name


@app.route('/test', methods=['GET', 'POST'])
# 请求方式在mothods中，以列表形式存在
def get_test():
    return 'get test true'


@app.route('/hello/')
def hello():
    # name = request.args.get('name', 'flask')
    # return '<h1>hello %s</h1>' % name
    """redicter重定向至指定url，也可使用url——for指定地址"""
    return redirect(url_for('get_test'))


@app.route('/gobane/<int:year>')
def go_back(year):
    return '<p>welcome to %d</p>' % (2022 - year)


@app.before_request
def do_it():
    pass  # 该方法会在每个请求执行之前运行一次


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True, load_dotenv=True)
