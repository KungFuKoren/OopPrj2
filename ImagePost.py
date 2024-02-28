from Post import Post

class ImagePost(Post):
    def __init__(self, user, type, image):
        super().__init__(user, type, image)

    def print(self):
        print("Image Post")