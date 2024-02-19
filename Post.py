from typing import List
from User import User


class Post():
    # Use Factory design for choosing type of post
    def __init__(self ,user , text):
        self.text = text
        self.user = user
        self.likes: List[str] = []
        self.comments: List[str] = []

def getUser(self):
    return self.user

def getLikes(self):
    return len(self.likes)

def addLike(self , user):
    if isinstance(user , User) and user.getName not in self.likes:
        self.likes.append(user.getName)
# sends notification
        
def addComment(self , user , text ):
    self.comments.append(text)
    #send notification

