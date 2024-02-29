from Post import Post

class TextPost(Post):
    def __init__(self, user, type, content):
        super().__init__(user, type, content)

    def __str__ (self):
        return f"{self.user.userName} published a post:\n\"{self.content}\""