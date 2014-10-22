from flask import Flask, render_template, request, redirect
import sqlite3
import os.path
import time


app = Flask(__name__)

#Must Run Commit After Function is called
def addPost (postdata, txtpostdata, time, pID, curs):

#    sinsertion = "INSERT INTO posts (title, post, time, pId) values ('" + title + "','" + post+ "'," + str(time) + "," + str(pID) + ");"

    sinsertion = "INSERT INTO posts (title, post, time, pId) values ('" + str(postdata) +  "', '" + txtpostdata + "', " + str(time) + ", " + str(pID) + ");"
    


    curs.execute(sinsertion)

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



@app.route("/", methods = ['GET'])
def index():
    conn = sqlite3.connect('softblog.db')
    c = conn.cursor()


    
    postdata = request.args.get("post");
    txtpostdata = request.args.get("txtpost");

    c.execute('''CREATE TABLE IF NOT EXISTS posts(title text, post text, time integer, pId integer);''')
    c.execute('''CREATE TABLE IF NOT EXISTS comments
    (comment text, time real, pId integer, cId integer);''')
    
    addPost(postdata, txtpostdata, 18.781, 199, c)

    sdata = ''

    for row in c.execute('SELECT * FROM posts'):
        sdata += str(row)

    conn.commit()
    conn.close()
    """
<<<<<<< HEAD
    

    posts = [("post1", "this is the first post HUrray fjawo;eij"), ("post2", "a;sodifjawo;eifja;woeifjaw;oeifjas;ldkfjha;skdjfhalskdjfhalskdjfhaskldjf")]

    return render_template("index.html", posts = posts );
=======
    print sdata
    
    return render_template("index.html", sinput = sdata);
>>>>>>> f6ac7638c0d5fd5a4795753959bf3bd77c3cc521
    
"""

if __name__ == "__main__":
    app.debug = True
    app.run()
