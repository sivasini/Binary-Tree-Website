from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'jyothi':'123','sanjna':'456','bharathi':'789','yuktha':'101','aishu':'102','siva':'103'}

@app.route('/login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('tree.html',name=name1)


@app.route('/tree')
def tree():
    return(render_template("tree.html"))


@app.route('/traversal')
def traversal():
    return(render_template("traversal.html"))


@app.route('/insert')
def insert():
    return(render_template("insert.html"))


@app.route('/properties')
def properties():
    return(render_template("properties.html"))


@app.route('/types')
def types():
    return(render_template("types.html"))

@app.route('/depth')
def depth():
    return(render_template("depth.html"))


if __name__ == '_main_':
    app.run()