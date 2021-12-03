from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contatcts():
    return render_template("contacts.html")

@app.route('/greeting/<string:user>/<int:age>')
def greeting(user,age):
    return f'Hello {user} and have {age}'

if __name__ == '__main__':
    app.run(debug=True)