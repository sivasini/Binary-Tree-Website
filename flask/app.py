from flask import Flask, flash, redirect, render_template, request, session, abort


app = Flask(__name__)
app.secret_key = 'You Will Never Guess'

@app.route('/')
def hello_world():
    return render_template("login.html")
database={'jyothi':'123', 'sanjna':'456', 'sivasini':'457','yuktha':'101112'}

@app.route('/login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    session['username'] = name1
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('tree.html',name=name1,user=session['username'])


@app.route('/tree')
def tree():
    return(render_template("tree.html",user=session['username']))


@app.route('/traversal')
def traversal():
    return(render_template("traversal.html",user=session['username']))


@app.route('/insert')
def insert():
    return(render_template("insert.html",user=session['username']))


@app.route('/properties')
def properties():
    return(render_template("properties.html",user=session['username']))


@app.route('/types')
def types():
    return(render_template("types.html",user=session['username']))

@app.route('/depth')
def depth():
    return(render_template("depth.html",user=session['username']))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return(render_template("login.html"))

if __name__ == '_main_':
    app.run()
