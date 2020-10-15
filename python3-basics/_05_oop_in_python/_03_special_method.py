class Book:

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __del__(self):
        print('the object is gone')


b = Book('Python tutorials', 'Pan', 200)
print(b)
s = set()
del s
print(s)
del b  # delete variable from your computer memory
print(b)

