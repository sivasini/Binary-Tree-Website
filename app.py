from flask import Flask, flash, redirect, render_template, request, session
from datetime import timedelta
import requests
import urllib.request
from bs4 import BeautifulSoup


def scrap_images(image_url,filename):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(image_url, filename)
    print("Succefully extracted",filename)


scrap_images("https://res.cloudinary.com/practicaldev/image/fetch/s--od-naD9n--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/975/1%2APWJiwTxRdQy8A_Y0hAv5Eg.png", 'static/bt1.png')
scrap_images("https://static.javatpoint.com/ds/images/insertion-in-binary-search-tree.png", "static/insert.png")
scrap_images("https://media.geeksforgeeks.org/wp-content/uploads/deletion-in-binary-tree.png", "static/delete.png")
scrap_images("https://www.tutorialspoint.com/data_structures_algorithms/images/inorder_traversal.jpg", "static/inorder.jpg")
scrap_images("https://www.tutorialspoint.com/data_structures_algorithms/images/preorder_traversal.jpg", "static/preorder.jpg")
scrap_images("https://www.tutorialspoint.com/data_structures_algorithms/images/postorder_traversal.jpg", "static/postorder.jpg")
scrap_images("https://cdn.programiz.com/sites/tutorial2program/files/tree_traversal_sub-tree-concept.png","static/tree.png")
scrap_images("https://media.cheggcdn.com/media/cd3/cd3ff72a-2453-4ef6-b7f5-530696f32e32/phpVqes7i", "static/euler.png")
scrap_images("https://i1.wp.com/kodebinary.com/wp-content/uploads/2019/04/image-87.png?w=809&ssl=1", "static/level.png")


def scrap_properties():
    def getdata(url):
        r = requests.get(url)
        return r.text
    htmldata = getdata("https://www.geeksforgeeks.org/binary-tree-set-2-properties/")
    soup = BeautifulSoup(htmldata, 'html.parser')
    data = ''
    for data in soup.find_all("p"):
        print(data.get_text())


app = Flask(__name__)
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=2000)
app.secret_key = 'You Will Never Guess'


@app.route('/')
def hello_world():
    return render_template("login.html")


database = {'jyothi': '123', 'sanjna': '456', 'sivasini': '457', 'yuktha': '101112'}


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name1 = request.form['username']
        pwd = request.form['password']
        if name1 not in database:
            return render_template('login.html', info='Invalid Username or Password')
        else:
            if database[name1] != pwd:
                return render_template('login.html', info='Invalid Username or Password')
            else:
                session['username'] = name1
                flash("Logged in")
                return render_template('tree.html', name=name1, user=session['username'])


@app.route('/tree')
def tree():
    return render_template("tree.html", user=session['username'])


@app.route('/traversal')
def traversal():
    return render_template("traversal.html", user=session['username'])


@app.route('/insert')
def insert():
    return render_template("insert.html", user=session['username'])


@app.route('/properties')
def properties():
    return render_template("properties.html", user=session['username'])


@app.route('/types')
def types():
    return render_template("types.html", user=session['username'])


@app.route('/depth')
def depth():
    return render_template("depth.html", user=session['username'])


@app.route('/v_insert')
def v_insert():
    return render_template("v_insert.html", user=session['username'])


@app.route('/v_depth')
def v_depth():
    return render_template("v_depth.html", user=session['username'])


@app.route('/v_height')
def v_height():
    return render_template("v_height.html", user=session['username'])


@app.route('/in')
def inorder():
    return render_template("in.html", user=session['username'])


@app.route('/pre')
def pre():
    return render_template("pre.html", user=session['username'])


@app.route('/post')
def post():
    return render_template("post.html", user=session['username'])


@app.route('/euler')
def euler():
    return render_template("euler.html", user=session['username'])


@app.route('/level')
def level():
    return render_template("level.html", user=session['username'])


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template("login.html")


@app.errorhandler(500)
def internal_error(error):
    session.pop('username', None)
    return redirect("/logout", code=302)


if __name__ == '_main_':
    app.run()
