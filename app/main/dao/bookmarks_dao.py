import json

class BookmarksDAO:
    def __init__(self, path):
        self.path = path
    
    def get_all(self) -> list:
        """возвращает все закладки"""
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)
    
    
    def add(self, content) -> None:
        """добавляет закладку"""
        file_content = self.get_all()
        
        if content in file_content or not content:
            return
        file_content.append(content)
        
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(file_content, file, ensure_ascii=False, indent=4)


    def delete(self, content) -> None:
        """удаляет закладку"""
        file_content = self.get_all()
        
        if content not in file_content or not content:
            return
        file_content.remove(content)
        
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(file_content, file, ensure_ascii=False, indent=4)