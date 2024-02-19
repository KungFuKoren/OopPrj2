from typing import List
from User import User


class Post():
    # Use Factory design for choosing type of post
    def __init__(self ,user , text):
        self.text = text
        self.user = user
        self.likes: List[User] = []
        self.comments = []
        self.numLikes = len(self.likes)

