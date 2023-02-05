from flask import Blueprint, jsonify
import logging
from app.main.dao.posts_dao import PostsDAO
from config import POSTS_DATA_PATH

logger = logging.getLogger("one")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/api.log", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao= PostsDAO(POSTS_DATA_PATH)


@api_blueprint.route('/api/posts/')
def api_all_posts():
    logger.info('Запрос /api/posts/')
    posts = posts_dao.get_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:pk>')
def api_one_post(pk):
    logger.info(f'Запрос /api/posts/{pk}')
    post = posts_dao.get_by_pk(pk)
    return jsonify(post)