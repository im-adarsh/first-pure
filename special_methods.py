class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return self.pages

myb = Book("Clean code", "Uncle Bob", 400)
print(len(myb))