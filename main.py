from flask import Flask, render_template
import requests

app=Flask(__name__)

blog_response=requests.get(url=" https://api.npoint.io/118320c7c3a7bf53f6ab")
posts=blog_response.json()

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/blog/Home')
def get_home_page():
    return render_template('index.html', posts=posts)

@app.route('/blog/About')
def get_about_page():
    return render_template("about.html")

@app.route('/blog/contact')
def get_contact_page():
    return render_template("contact.html")

@app.route('/blog/posts/<int:post_id>')
def get_posts(post_id):

    return render_template("post.html", post=posts[post_id-1])

if __name__=="__main__":
    app.run(debug=True)