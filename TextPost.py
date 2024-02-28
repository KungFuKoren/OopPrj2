from Post import Post

class TextPost(Post):
    def __init__(self, user, type, content):
        super().__init__(user, type, content)

    def print(self):
        print("Text Post")