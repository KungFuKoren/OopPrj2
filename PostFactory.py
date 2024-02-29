from ImagePost import ImagePost
from TextPost import TextPost
from SalePost import SalePost

class PostFactory():
    def createPost(self, user, type, content, price = None, location = None):
        post = None

        if type == "Text":
            post = TextPost(user, type, content)
        elif type == "Image":
            post = ImagePost(user, type, content)
        elif type == "Sale":
            if price is None or location is None:
                raise ValueError("Price and location are required for Sale post")
            post = SalePost(user, type, content, price, location)
        else:
            return None
        
        print(post)
        return post
