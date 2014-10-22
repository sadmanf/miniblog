from flask import Flask, render_template, request, redirect
import sqlite3
import os.path
import time


app = Flask(__name__)


@app.route("/", methods = ['GET'])
def index():
    conn = sqlite3.connect('softblog.db')
    c = conn.cursor()


    
    #sinput = request.args.get("blogpost");
    c.execute('''CREATE TABLE IF NOT EXISTS posts(title text, post text, time integer, pId integer);''')
    c.execute('''CREATE TABLE IF NOT EXISTS comments
    (comment text, time real, pId integer, cId integer);''')
    
    sinsertion = '''INSERT INTO posts (title, post, time, pId) 
    values ('title', 'post', 12, 12);
    ''' 
    c.execute(sinsertion)    

    sdata = ''

    for row in c.execute('SELECT * FROM posts'):
        sdata += str(row)
        
    conn.commit()
    conn.close()
    

    posts = [("post1", "this is the first post HUrray fjawo;eij"), ("post2", "a;sodifjawo;eifja;woeifjaw;oeifjas;ldkfjha;skdjfhalskdjfhalskdjfhaskldjf")]

    return render_template("index.html", posts = posts );
    


if __name__ == "__main__":
    app.debug = True
    app.run()
