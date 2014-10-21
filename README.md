miniblog
========


Roles
Cooper - Flask App
Genji  - HTML/Styling
Benedict&Sadman  - Figuring out SQLite


Assignment : 
Here it is:

It's a simple blog engine.

When: Due Wednesday morning (10/22)

Base project:

You will store a single blog where people can add comments to posts.


Pages:

Index page: /

This page will list the titles of all the posts and have a form where one can enter a new title and post. The title should be unique.

If the user clicks on a title, it will take them to a "blog post page"

blog post page: /title

This will take the user to an individual post. Use the <name> feature of flask for the routing. See the flask documentation if you don't remember this.

This page will show the title and post as well as all the comments. There should be a form to add a new comment.

There should also be a way to get back to the main page.

database stuff:

You'll need a table for the posts with titles and posts and a table for comments where each comment will link to a post.

Extras:

think about adding features like:
1. adding usernames to posts and or comments.
2. Adding multiple blogs (this isn't hard, buit since it adds a layer of complexity it will add a bunch of time.

Timing:
I'm thinking of giving you Monday and Tuesday as lab days + you'll have this weekend.

Sound fair?

MZ
