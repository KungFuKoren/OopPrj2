from abc import ABC
from typing import List, Dict, Union

class Post(ABC):
    def __init__(self, user, post_type, content):
        from User import User
        self.post_type = post_type
        self.content = content
        self.user = user
        self.likes = set()
        self.comments: List[Dict[Union[User, str], str]] = []
        


    def getUser(self):
        return self.user

    def getLikes(self):
        return len(self.likes)

    def comment(self, user, text):
        from User import User
        if not isinstance(user, User) and user.getName() not in self.likes:
            raise Exception("Unable to add comment")
        self.comments.append({
            "user": user,
            "text": text
        })
        # send notification

    def like(self, user):
        from User import User
        if isinstance(user, User) and user.getName() not in self.likes:
            self.likes.add(user)
            # print("Liked")
        else:
            raise Exception("Unable to like")