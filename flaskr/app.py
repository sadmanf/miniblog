from flask import Flask, render_template, request, redirect
import sqlite3
import os.path
import time


app = Flask(__name__)

#posts = [("post1", "this is the first post HUrray fjawo;eij"), ("post2", "a;sodifjawo;eifja;woeifjaw;oeifjas;ldkfjha;skdjfhalskdjfhalskdjfhaskldjf")]

#Must Run Commit After Function is called
def addPost (postdata, txtpostdata, time, curs):

#    sinsertion = "INSERT INTO posts (title, post, time, pId) values ('" + title + "','" + post+ "'," + str(time) + "," + str(pID) + ");"

    sinsertion = "INSERT INTO posts (title, post, time) values (" + "'" + str(postdata) +  "', '" + txtpostdata + "', " + str(time) + ");"



    curs.execute(sinsertion)

def getPosts (curs):
  result = curs.execute('SELECT * FROM posts')
  for row in result:
    print row
  return result

def trending(a):
    one = 0
    oneCount = 0
    two = 0
    twoCount = 0
    three = 0
    threeCount = 0
    for post in a:
        count = 0
        for time in post:
            if time - time.time() <= 86400:
                count += 1
        if count > oneCount:
            three = two
            threeCount = twoCount
            two = one
            twoCount = oneCount
            one = post[0]
            oneCount = count
        elif count >= twoCount:
            three = two
            threeCount = twoCount
            two = post[0]
            twoCount = count
        elif count >= threeCount:
            three = post[0]
            threeCount = count
    return [one,two,three]


@app.route("/")
def index():
    conn = sqlite3.connect('softblog.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts(title text UNIQUE, post text, time integer);''')
    c.execute('''CREATE TABLE IF NOT EXISTS comments
    (comment text, time real, pId integer);''')
    #Insert code here to fetch all of the posts and set posts to that. - genji
    
    
    c.execute("select * from posts")
    #print [str(x[0]) for x in c.fetchall()]
    titles = []
    posts = []
    for x in c.fetchall():
        posts.append(x) 

 #       print(str(x[0]))
  #      print(str(x[1]))

        
    posts = posts[::-1]
    print titles
    # posts = posts[::-1]
    #length = len(posts)
#    print length
    #Insert code here to fetch the trending posts now. -genji
    return render_template("index.html", location="Home",posts=posts, trending=posts)

@app.route("/new-post", methods=['POST'])
def newPost():
    if request.method=='POST':
        name = request.form['username']
        content = request.form['post-content']
        print name
        print content
        conn = sqlite3.connect('softblog.db')
        c = conn.cursor()

        addPost(name, content, time.time(), c)
        #INSERT CODE HERE TO ADD A NEW POST. -genji

        getPosts(c)
            
        conn.commit()
        conn.close()

    return redirect("http://localhost:5000")

@app.route("/<post_id>")
def post(post_id=None):
    print "Post ID: " + post_id
    return render_template("post.html",location=posts[int(post_id)][0])

@app.route("/<post_id>/new-comment")
def addComment(post_id=None):
    #INSERT CODE HERE TO ADD A NEW COMMENT TO THE POST -genji
    if request.method=='POST':
        username = request.form('username')
        content = request.form('comment')
    return redirect("http://localhost:5000/"+post_id)


if __name__ == "__main__":
    app.debug = True
    app.run()
