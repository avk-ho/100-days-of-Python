from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"



@app.route('/')
def home():
    blog_response = requests.get(blog_url)
    posts_data = blog_response.json()
    all_posts = {}
    for post in posts_data:
        new_post = Post(
            id=post["id"],
            title=post["title"],
            subtitle=post["subtitle"],
            body=post["body"]
            )
        all_posts[new_post.ID] = new_post

    return render_template(
        "index.html",
        posts=all_posts,
        )

@app.route("/post/<int:post_id>")
def blog_post(post_id):
    blog_response = requests.get(blog_url)
    posts_data = blog_response.json()
    all_posts = {}
    for post in posts_data:
        new_post = Post(
            id=post["id"],
            title=post["title"],
            subtitle=post["subtitle"],
            body=post["body"]
        )
        all_posts[new_post.ID] = new_post
    current_post = all_posts[post_id]
    
    return render_template(
        "post.html",
        post=current_post
        )
# Having to request all the posts and checking which one we need is inefficient
# normally we would have access to a database through which we would only request
# the post we need with its ID


if __name__ == "__main__":
    app.run(debug=True)
