from flask import Flask, render_template
import requests
from datetime import datetime
from post import Post

app = Flask(__name__)

API_ENDPOINT = "https://api.npoint.io/674f5423f73deab1e9a7"

posts = requests.get(API_ENDPOINT).json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["image_url"])
    post_objects.append(post_obj)

@app.route('/')
def get_home_page():
    current_year = datetime.now().year
    return render_template("index.html", posts = post_objects, year=current_year)

@app.route('/about')
def get_about_page():
    return render_template("about.html")

@app.route("/post/<int:index>")
def get_posts_page(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


@app.route("/contact")
def get_contact_page():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

