from flask import Flask, abort, render_template, request, redirect, url_for, make_response, jsonify

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
    response = make_response('<h1>a cokie</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/test', methods=['GET', 'POST'])
# 请求方式在mothods中，以列表形式存在
def get_test():
    return 'get test true'


@app.route('/hello/')
def hello():
    """redicter重定向至指定url，也可使用url——for指定地址"""
    return redirect(url_for('get_test'))


@app.route('/gobane/<int:year>')
def go_back(year):
    return '<p>welcome to %d</p>' % (2022 - year)


@app.before_request
def do_it():
    pass  # 该方法会在每个请求执行之前运行一次


@app.route('/json/')
def jsonx():
    data = {
        'name': '夏志峰'
    }
    '''
    输入json格式参数，返回时直接使用jsonfly返回格式为json的json串，旧版存在ascli编码问题，新版直接转化不需要关闭
    '''
    # response= make_response(json.dumps(data,ensure_ascii=False))
    # response.mimetype='application/json'
    return jsonify(data)


@app.route('/abc', methods=['GET', 'POST'])
def abc():
    if request.method == 'GET':
        return render_template('homepage.html')
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'xiazhifeng' and password == '123':
            return 'login pass'
        else:
            abort(500)
            return None


# 定义错误执行步骤
@app.errorhandler(404)
def error_html(err):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True, load_dotenv=True)
