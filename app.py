import flask.cli
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/homepage')
@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/test', methods=['GET', 'POST'])
def gettest():
    return 'gettest true'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True, load_dotenv=True)
