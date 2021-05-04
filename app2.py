from flask import Flask, flash, redirect, render_template, request, session
from datetime import timedelta
import requests
import urllib.request
from bs4 import BeautifulSoup


def scrap_images(image_url, filename):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(image_url, filename)
    print("Successfully extracted", filename)


scrap_images(
    "https://res.cloudinary.com/practicaldev/image/fetch/s--od-naD9n--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/975/1%2APWJiwTxRdQy8A_Y0hAv5Eg.png",
    '../flaskProject4/static/bt1.png')
scrap_images("https://static.javatpoint.com/ds/images/insertion-in-binary-search-tree.png",
             "../flaskProject4/static/insert.png")
scrap_images("https://media.geeksforgeeks.org/wp-content/uploads/deletion-in-binary-tree.png",
             "../flaskProject4/static/delete.png")
scrap_images("https://www.tutorialspoint.com/data_structures_algorithms/images/inorder_traversal.jpg",
             "../flaskProject4/static/inorder.jpg")
scrap_images("https://www.tutorialspoint.com/data_structures_algorithms/images/preorder_traversal.jpg",
             "../flaskProject4/static/preorder.jpg")
scrap_images("https://www.tutorialspoint.com/data_structures_algorithms/images/postorder_traversal.jpg",
             "../flaskProject4/static/postorder.jpg")
scrap_images("https://cdn.programiz.com/sites/tutorial2program/files/tree_traversal_sub-tree-concept.png",
             "../flaskProject4/static/tree.png")
scrap_images("https://media.cheggcdn.com/media/cd3/cd3ff72a-2453-4ef6-b7f5-530696f32e32/phpVqes7i",
             "../flaskProject4/static/euler.png")
scrap_images("https://i1.wp.com/kodebinary.com/wp-content/uploads/2019/04/image-87.png?w=809&ssl=1",
             "../flaskProject4/static/level.png")
scrap_images("https://austingwalters.com/wp-content/uploads/2014/10/binary-tree-1-search.gif", "static/gif1.gif")
scrap_images("https://upload.wikimedia.org/wikipedia/commons/1/19/Morse-code-tree.svg", "static/morsecode1.svg")
scrap_images("https://hrexach.files.wordpress.com/2015/07/morse.jpg", "static/morsecode2.jpg")
scrap_images("https://i.imgur.com/HkWgOmv.gif", "static/fractal.gif")
#scrap_images("https://image.jimcdn.com/app/cms/image/transf/dimension=1920x400:format=gif/path/sbaefc454c475f4e6/image/i071afc3bcd8c9e3a/version/1510672986/image.gif","static/fractal2.gif")
scrap_images("http://orig09.deviantart.net/0cf5/f/2009/109/3/4/fractal_tree_by_tararoys.gif", "static/airport.gif")
scrap_images("http://www.math.union.edu/research/fractaltrees/labels.gif", "static/fractal3.gif")
scrap_images("https://storage.googleapis.com/cs-unplugged.appspot.com/static/img/topics/binary_detective.gif", "static/bst1.gif")
scrap_images("https://blog.penjee.com/wp-content/uploads/2015/11/binary-search-tree-sorted-array-animation.gif", "static/bst2.gif")


def scrap_properties():
    def getdata(url):
        r = requests.get(url)
        return r.text

    htmldata = getdata("https://www.tutorialspoint.com/discrete_mathematics/introduction_to_trees.htm")
    soup = BeautifulSoup(htmldata, 'html.parser')
    data = ''
    for data in soup.find_all("p"):
        print(data.get_text())




app = Flask(_name_)
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
    source = requests.get("https://www.tutorialspoint.com/discrete_mathematics/introduction_to_trees.htm").text
    soup = BeautifulSoup(source, 'html.parser')
    summary = soup.find('div', class_='mui-col-md-6 tutorial-content')
    article = summary.p.text
    s = requests.get("https://www.upgrad.com/blog/5-types-of-binary-tree/#:~:text=A%20binary%20tree%20is%20a,nodes%20are%20the%20parent%20nodes.").text
    so = BeautifulSoup(s, 'html.parser')
    binary = so.find_all('p')
    s = requests.get("https://www.upgrad.com/blog/5-types-of-binary-tree/#:~:text=A%20binary%20tree%20is%20a,nodes%20are%20the%20parent%20nodes.").text
    so = BeautifulSoup(s, 'lxml')
    binary = so.find_all('p')

    point1 = binary[3].text
    point2 = binary[4].text

    return render_template("tree.html", **locals(),user=session['username'])








@app.route('/traversal')
def traversal():
    s = requests.get("https://www.tutorialspoint.com/data_structures_algorithms/tree_traversal.htm").text
    so = BeautifulSoup(s, 'lxml')
    binary = so.find_all('p')

    point1 = binary[0].text
    point2=binary[1].text

    return render_template("traversal.html",**locals(), user=session['username'])


@app.route('/insert')
def insert():
    return render_template("insert.html", user=session['username'])


@app.route('/properties')
def properties():

    return render_template("properties.html",**locals() ,user=session['username'])


@app.route('/types')
def types():
    s = requests.get("https://www.upgrad.com/blog/5-types-of-binary-tree/#:~:text=A%20binary%20tree%20is%20a,nodes%20are%20the%20parent%20nodes.").text
    so = BeautifulSoup(s, 'lxml')
    binary = so.find_all('p')

    point1 = binary[13].text
    point2 = binary[14].text
    point3 = binary[17].text
    point4 = binary[20].text
    return render_template("types.html", **locals(),user=session['username'])

'''s = requests.get("https://www.tutorialspoint.com/data_structures_algorithms/binary_search_tree.htm").text
a= requests.get("https://mdkulkarni76.medium.com/height-and-depth-of-a-binary-tree-2a9f115eeee9").text
so = BeautifulSoup(s, 'lxml')
binary = so.find('ul',class_="list")
b=so.find_all('p')
point1=b[0].text
point2=b[2].text
print(point1)
print(point2)'''
'''point2=binary[5].text
point1 = binary[3].text
print(point2)'''
print(binary.text)
@app.route('/depth')
def depth():
    s = requests.get("https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/").text
    a = requests.get("https://mdkulkarni76.medium.com/height-and-depth-of-a-binary-tree-2a9f115eeee9").text
    so = BeautifulSoup(a, 'lxml')
    binary = so.find_all('p')
    point2 = binary[5].text
    point1 = binary[4].text
    s2 = BeautifulSoup(s, 'lxml')
    bi = s2.find_all('p')
    point3 = bi[2].text
    return render_template("depth.html", **locals(),user=session['username'])


@app.route('/practice')
def practice():
    return render_template("practice.html", user=session['username'])


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

@app.route('/application')
def application():
    return render_template("application.html", user=session['username'])


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template("login.html")


@app.errorhandler(500)
def internal_error(error):
    session.pop('username', None)
    return redirect("/logout", code=302)


if _name_ == 'main':
    app.run(port=880)
