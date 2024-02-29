from Post import Post
# import matplotlib.pyplot as plt

class ImagePost(Post):
    def __init__(self, user, post_type, image):
        super().__init__(user, post_type, content=image)

    def __str__ (self):
        return f"{self.user.userName} posted a picture"

    # def display(self):
    #     print(self.content)
    #     img_to_arr = plt.imread(self.content)
    #     plt.imshow(img_to_arr)
    #     plt.show()