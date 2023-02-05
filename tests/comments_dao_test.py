
import os
import allure
import pytest
import requests
from logging import getLogger
from app.main.dao.comments_dao import CommentsDAO
from app.main.dao.posts_dao import PostsDAO
from run import app
from config import *

logger = getLogger()
comments = [pytest.param(os.path.join(COMMENTS_DATA_PATH))]
comments_keys_names = ["post_id",
                       "commenter_name",
                       "comment",
                       "pk"]



@allure.epic("Test_comments_dao")
class Test_comments_dao:


    @allure.description("Проверка типа возвращенных данных ")
    @pytest.mark.parametrize("path_comments", comments)
    def test_comments_type(self, path_comments):
        comments_dao = CommentsDAO(path_comments)
        assert type(comments_dao.get_all()) == list
        logger.info('The list is returned')
        print(f" Возвращается список "                              # print создан для отчета allure
              f"\n {comments_dao.get_all()} ")

    @allure.description("Проверка нужных ключей ")
    @pytest.mark.parametrize("path_comments", comments)
    def test_comments_keys_names(self, path_comments):
        comments_dao = CommentsDAO(path_comments)
        assert all(all(key in item for key in comments_keys_names) for item in comments_dao.get_all())
        logger.info('All the necessary keys are present')
        print(f" Все необходимые ключи присутствуют"
              f"\n {comments_keys_names}")

    @allure.description("Проверка определенного  коментария ")
    @pytest.mark.parametrize("post_id", comments)
    def test_comments_by_post_id(self,post_id):
        comments_dao = CommentsDAO(post_id)
        all_comments = comments_dao.get_all()
        first_comment = all_comments[0]
        assert first_comment["comment"] is not None, "Комментарий отсутствует"
        logger.info('The user has a comment under the post')
        print(f" В '{all_comments[0]['post_id']}' посте ,"
              f" у пользоватея '{all_comments[0]['commenter_name']}', коментарий '{first_comment['comment']}'")



posts = [pytest.param(os.path.join(POSTS_DATA_PATH))]
posts_keys_names = ["poster_name",
                    "poster_avatar",
                    "pic",
                    "content",
                    "views_count",
                    "likes_count",
                    "pk"]

@allure.epic("Test_posts_dao")
class Test_posts_dao:

    @allure.description("Проверка типа всех постов ")
    @pytest.mark.parametrize("path_posts", posts)
    def test_comments_type(self, path_posts):
        posts_dao = PostsDAO(path_posts)
        assert type(posts_dao.get_all()) == list
        logger.info('Проверка типа всех постов')
        print(f" Возвращается список "
              f"\n {posts_dao.get_all()} ")

    @allure.description("Проверка нужных ключей ")
    @pytest.mark.parametrize("path_posts", posts)
    def test_comments_keys_names(self, path_posts):
        posts_dao = PostsDAO(path_posts)
        assert all(all(key in item for key in posts_keys_names) for item in posts_dao.get_all())
        logger.info('All the necessary keys are present')
        print(f" Все необходимые ключи присутствуют"
              f"\n {posts_keys_names}")

    @allure.description("Проверка картинки поста ")
    @pytest.mark.parametrize("path_posts", posts)
    def test_comments_by_post_id(self, path_posts):
        comments_dao = PostsDAO(path_posts)
        all_comments = comments_dao.get_all()
        first_comment = all_comments[1]
        assert first_comment["pic"] is not None, "Картинки отсутствует"
        logger.info('The user has a picture in the post')
        print(f" В посте у пользователя '{all_comments[1]['poster_name']}' присутствует картинка "
              f" \n'{first_comment['pic']}' , имеет тип данных {type(first_comment['pic'])}")


