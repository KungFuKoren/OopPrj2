from abc import ABC #, abstractmethod  # if needed
from typing import List


class Post(ABC):
    # Use Factory design for choosing type of post
    def __init__(self ,user, type , content):
        
        self.type = type
        self.content = content
        self.user = user
        self.likes = {}
        self.comments: List[str] = []

def getUser(self):
    return self.user

def getLikes(self):
    return len(self.likes)

def addLike(self , user):
    from User import User
    
    if isinstance(user , User) and user.getName() not in self.likes:
        self.likes.add(user.getName)
# sends notification
        
def addComment(self , user , text ):
    self.comments.append({
        "user": user,
        "text" : text
    })
    #send notification

