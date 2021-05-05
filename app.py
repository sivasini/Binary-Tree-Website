from flask import Flask, flash, redirect, render_template, request, session
from datetime import timedelta
import requests
import urllib.request
from bs4 import BeautifulSoup
import csv

def scrap_images(image_url, filename):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(image_url, filename)
    print("Successfully extracted", filename)

'''
scrap_images("https://res.cloudinary.com/practicaldev/image/fetch/s--od-naD9n--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/975/1%2APWJiwTxRdQy8A_Y0hAv5Eg.png", 'static/bt1.png')
scrap_images("https://static.javatpoint.com/ds/images/insertion-in-binary-search-tree.png", "static/insert.png")
scrap_images("https://media.geeksforgeeks.org/wp-content/uploads/deletion-in-binary-tree.png", "static/delete.png")
scrap_images("https://www.tutorialspoint.com/data_structures_algorithms/images/inorder_traversal.jpg", "static/inorder.jpg")
scrap_images("https://www.tutorialspoint.com/data_structures_algorithms/images/preorder_traversal.jpg", "static/preorder.jpg")
scrap_images("https://www.tutorialspoint.com/data_structures_algorithms/images/postorder_traversal.jpg", "static/postorder.jpg")
scrap_images("https://cdn.programiz.com/sites/tutorial2program/files/tree_traversal_sub-tree-concept.png","static/tree.png")
scrap_images("https://media.cheggcdn.com/media/cd3/cd3ff72a-2453-4ef6-b7f5-530696f32e32/phpVqes7i", "static/euler.png")
scrap_images("https://i1.wp.com/kodebinary.com/wp-content/uploads/2019/04/image-87.png?w=809&ssl=1", "static/level.png")
scrap_images("https://austingwalters.com/wp-content/uploads/2014/10/binary-tree-1-search.gif", "static/gif1.gif")
scrap_images("https://upload.wikimedia.org/wikipedia/commons/1/19/Morse-code-tree.svg", "static/morsecode1.svg")
scrap_images("https://hrexach.files.wordpress.com/2015/07/morse.jpg", "static/morsecode2.jpg")
scrap_images("https://i.imgur.com/HkWgOmv.gif", "static/fractal.gif")
#scrap_images("https://image.jimcdn.com/app/cms/image/transf/dimension=1920x400:format=gif/path/sbaefc454c475f4e6/image/i071afc3bcd8c9e3a/version/1510672986/image.gif","static/fractal2.gif")
scrap_images("http://orig09.deviantart.net/0cf5/f/2009/109/3/4/fractal_tree_by_tararoys.gif", "static/airport.gif")
scrap_images("http://www.math.union.edu/research/fractaltrees/labels.gif", "static/fractal3.gif")
scrap_images("https://storage.googleapis.com/cs-unplugged.appspot.com/static/img/topics/binary_detective.gif", "static/bst1.gif")
scrap_images("https://blog.penjee.com/wp-content/uploads/2015/11/binary-search-tree-sorted-array-animation.gif", "static/bst2.gif")
'''

def scrape_video():
    url = 'https://www.youtube.com/watch?v=s2Yyk3qdy3o'
    video_name = url.split('=')[-1]
    print("Downloading file:", video_name)
    r = requests.get(url)
    with open('video.mp4', 'wb') as f:
        f.write(r.content)
    #urllib.request.urlretrieve(url, "video.mp4")
    return video_name

def scrape_pratice():
    URL = "https://medium.com/techie-delight/binary-tree-interview-questions-and-practice-problems-439df7e5ea1f"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')

    quotes = []  # a list to store quotes

    table = soup.find('section', attrs={'class': 'cq cr cs ct cu'})

    for row in table.findAll('li'):
        quote={}
        quote['url'] = row.a['href']
        quote['name'] = row.a.text
        quotes.append(quote)

    filename = 'static/practice.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f, ['url', 'name'])
        w.writeheader()
        for quote in quotes:
            w.writerow(quote)
    return quotes

def scrap_link():
    wiki_link = 'https://medium.com/techie-delight/binary-tree-interview-questions-and-practice-problems-439df7e5ea1f'
    req = requests.get(wiki_link)
    soup3 = BeautifulSoup(req.content, 'html.parser')
    #print(soup3.prettify())
    lin = soup3.find_all("a", class_="ei hn")
    #for link in lin:
        #print(link.get("href"))
    quotes = []  # a list to store quotes
    for links in lin:
        q = {}
        q['ref'] = links.get('href')
        q['text'] = links.text
        quotes.append(q)
    #print(quotes)
    filename = 'static/fileone.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f, ['ref', 'text'])
        w.writeheader()
        for quote in quotes:
            w.writerow(quote)
scrap_link()


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
                return redirect('/tree', code=302)

'''
@app.route('/tree')
def tree():
    return render_template("tree.html", user=session['username'])
'''
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
    so = BeautifulSoup(s, 'html.parser')
    binary = so.find_all('p')

    point1 = binary[3].text
    point2 = binary[4].text

    return render_template("tree.html", **locals(),user=session['username'])


'''
@app.route('/traversal')
def traversal():
    return render_template("traversal.html", user=session['username'])
'''

@app.route('/traversal')
def traversal():
    s = requests.get("https://www.tutorialspoint.com/data_structures_algorithms/tree_traversal.htm").text
    so = BeautifulSoup(s, 'html.parser')
    binary = so.find_all('p')

    point1 = binary[0].text
    point2=binary[1].text

    return render_template("traversal.html",**locals(), user=session['username'])

@app.route('/insert')
def insert():
    return render_template("insert.html", user=session['username'])


@app.route('/properties')
def properties():
    return render_template("properties.html", user=session['username'])

'''
@app.route('/types')
def types():
    return render_template("types.html", user=session['username'])


@app.route('/depth')
def depth():
    return render_template("depth.html", user=session['username'])
'''

@app.route('/types')
def types():
    s = requests.get("https://www.upgrad.com/blog/5-types-of-binary-tree/#:~:text=A%20binary%20tree%20is%20a,nodes%20are%20the%20parent%20nodes.").text
    so = BeautifulSoup(s, 'html.parser')
    binary = so.find_all('p')

    point1 = binary[13].text
    point2 = binary[14].text
    point3 = binary[17].text
    point4 = binary[20].text
    return render_template("types.html", **locals(), user=session['username'])

@app.route('/depth')
def depth():
    s = requests.get("https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/").text
    a = requests.get("https://mdkulkarni76.medium.com/height-and-depth-of-a-binary-tree-2a9f115eeee9").text
    so = BeautifulSoup(a, 'html5lib')
    binary = so.find_all('p')
    point2 = binary[5].text
    point1 = binary[4].text
    s2 = BeautifulSoup(s, 'html5lib')
    bi = s2.find_all('p')
    point3 = bi[2].text
    return render_template("depth.html", **locals(), user=session['username'])


@app.route('/practice')
def practice():
    quotes = scrape_pratice()
    video_name=scrape_video()
    list_url = []
    list_name = []
    for i in quotes:
        list_url.append(i['url'])
        list_name.append(i['name'])

    return render_template("practice.html", url=list_url,name=list_name, video=video_name, user=session['username'])



@app.route('/v_insert')
def v_insert():
    return render_template("v_insert.html", user=session['username'])


@app.route('/v_depth')
def v_depth():
    return render_template("v_depth.html", user=session['username'])

@app.route('/anim')
def anim():
    return render_template("anim.html", user=session['username'])

@app.route('/v_bst')
def v_bst():
    return render_template("v_bst.html", user=session['username'])


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
    app.run(debug=True)
