import json

class PostsDAO:
    def __init__(self, path):
        self.path = path
        
        
    def get_all(self):
        """возвращает все посты"""
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)
        
        
    def get_by_user(self, user_name):
        """возвращает посты определенного пользователя.
        Функция должна вызывать ошибку `ValueError`
        если такого пользователя нет и пустой список,
        если у пользователя нет постов."""
        if user_name in (" ", ""):
            return []
        
        current_posts = []
        
        for post in self.get_all():
            if post["poster_name"] == user_name:
                current_posts.append(post)
        return current_posts

        
    def search_by_keyword(self, query):
        """возвращает список постов по ключевому слову"""
        if query in (" ", ""):
            return []
        
        current_posts = []
        
        for post in self.get_all():
            if query.lower() in post["content"].lower():
                current_posts.append(post)
        return current_posts
        
        
    def get_by_pk(self, pk):
        """возвращает один пост по его идентификатору."""
        for post in self.get_all():
            if post['pk'] == pk:
                return post
        return {}
