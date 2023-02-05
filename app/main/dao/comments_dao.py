import json


class CommentsDAO:
    def __init__(self, path):
        self.path = path
    
    
    def get_all(self) -> list:
        """возвращает все комментарии"""
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)
    
    
    def get_by_post_id(self, post_id) -> list:
        """возвращает комментарии определенного поста.
        Функция должна вызывать ошибку `ValueError`
        если такого поста нет и пустой список, 
        если у поста нет комментов."""
        current_comments = []
        
        for post in self.get_all():
            if post["post_id"] == post_id:
                current_comments.append(post)
        return current_comments