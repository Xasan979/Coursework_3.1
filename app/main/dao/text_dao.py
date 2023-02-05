class TextDAO:
    
    def find_all_tags(self, text:str):
        return sorted(list({tag.strip("#") for tag in text.split() if tag.startswith("#") and len(tag)>1}), reverse=True)
    
    
    def replace_tags_to_links(self, text:str, tags:list|set|tuple):
        result_text = text
        for tag in tags:
            result_text = result_text.replace(f"#{tag}", f'<a class="item__tag" href="/tag/{tag}"><[heshteg]>{tag}</a>')
        return result_text.replace("<[heshteg]>", "#")
    
    
    def make_nice_text(self, text):
        tags = self.find_all_tags(text)
        result_text = self.replace_tags_to_links(text, tags)
        return result_text
    
    
    # def make_nice_text_for_posts(self, posts:list):
    #     for post in posts:
    #         tags = self.find_all_tags(post["content"])
    #         post["content"] = self.replace_tags_to_links(post["content"], tags)
    #     return posts