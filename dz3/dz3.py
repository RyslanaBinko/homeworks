from flask import Flask, render_template
from flask import request, make_response
from flask import session

app = Flask(__name__)
app.secret_key = b"-56hjk/"


@app.route('/')
def index():
    visited = 0
    if request.cookies.get('visited'):
        visited = int(request.cookies.get('visited'))
    if session.get('username'):
        username = session['username']
    else:
        session['username'] = "anonymous"
        username = session['username']

    response = make_response(
        render_template('index.html', visited=visited, username=username))

    response.set_cookie('visited', str(visited + 1))
    return response


@app.route("/login", methods=['POST', 'GET'])
def login():
    response = make_response(render_template('login.html'))
    if session.get('username'):
        username = session['username']
        return f'You logged as <b> {username} </b> user'
    else:
        if request.method == "GET":
            return response
        elif request.method == "POST":
            session['username'] = request.form["username"]
            username = session['username']
            return f'You logged as <b> {username} </b> user'


@app.route('/logout')
def delete_session():
    session.pop('username', None)
    return render_template("logout.html")


app.run(debug=True)
