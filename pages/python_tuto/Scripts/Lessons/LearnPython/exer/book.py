
class Book:
    def __init__(self, title, author, pages):
        self.title = title;
        self.author = author;
        self.pages = pages
    
    @property
    def set_title(self, title):
        self.title = title
    
    def title(self):
        return self.title;
