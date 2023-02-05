from flask import Blueprint, render_template, request, redirect
from app.main.dao.posts_dao import PostsDAO
from app.main.dao.comments_dao import CommentsDAO
from app.main.dao.text_dao import TextDAO
from app.main.dao.bookmarks_dao import BookmarksDAO
from config import POSTS_DATA_PATH, COMMENTS_DATA_PATH, BOOKMARKS_DATA_PATH


pages_blueprint = Blueprint('pages_blueprint', __name__, template_folder="templates")

posts_dao, comments_dao = PostsDAO(POSTS_DATA_PATH), CommentsDAO(COMMENTS_DATA_PATH)
text_dao = TextDAO()
bookmarks_dao = BookmarksDAO(BOOKMARKS_DATA_PATH)


@pages_blueprint.route('/')
def page_index():
    posts = posts_dao.get_all()
    return render_template("index.html", posts=posts, count_bookmarks=len(bookmarks_dao.get_all()))


@pages_blueprint.route('/posts/<int:post_pk>')
def page_post(post_pk):
    post = posts_dao.get_by_pk(post_pk)
    post["content"] = text_dao.make_nice_text(post["content"])
    comments = comments_dao.get_by_post_id(post_pk)
    return render_template("post.html", post=post, comments=comments)


@pages_blueprint.route('/search')
def page_search():
    s = request.args.get("s"," ")
    posts = posts_dao.search_by_keyword(s)
    return render_template("search.html", posts=posts, search_text=s)


@pages_blueprint.route('/users/<name>')
def page_user(name):
    posts = posts_dao.get_by_user(name)
    return render_template("user-feed.html", posts=posts, user_name=name)


@pages_blueprint.route('/tag/<tagname>')
def page_tag(tagname):
    posts = posts_dao.search_by_keyword("#"+tagname)
    posts = [post for post in posts if tagname in text_dao.find_all_tags(post["content"])]
    print(posts)
    return render_template("tag.html", posts=posts, tagname=tagname)


@pages_blueprint.route('/bookmarks/add/<int:post_id>')
def page_bookmarks_add(post_id):
    post = posts_dao.get_by_pk(post_id)
    bookmarks_dao.add(post)
    
    return redirect("/", code = 302)


@pages_blueprint.route('/bookmarks/remove/<int:post_id>')
def page_bookmarks_delete(post_id):
    post = posts_dao.get_by_pk(post_id)
    bookmarks_dao.delete(post)
    
    return redirect("/", code = 302)


@pages_blueprint.route('/bookmarks/')
def page_bookmarks():
    posts = bookmarks_dao.get_all()
    
    return render_template("bookmarks.html", posts=posts)