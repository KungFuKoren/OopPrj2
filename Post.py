from abc import ABC
from typing import List, Dict, Union


class Post(ABC):
    def __init__(self, user, post_type, content):
        from PostObserver import PostObserver
        from User import User
        self.post_type = post_type
        self.content = content
        self.user = user
        self.likes = set()
        self.comments: List[Dict[Union[User, str], str]] = []
        self.post_observer = PostObserver(self)

    def getUser(self):
        return self.user

    def getLikes(self):
        return len(self.likes)

    def comment(self, user, text):
        from User import User
        if not isinstance(user, User) and user.getName() not in self.likes and not user.logged:
            raise Exception("Unable to add comment")
        self.comments.append({
            "user": user,
            "text": text
        })
        self.post_observer.commented(user)
        # send notification

    def like(self, user):
        from User import User
        if isinstance(user, User) and user.getName() not in self.likes and user.logged:
            self.likes.add(user)
            self.post_observer.liked(user)
        else:
            raise Exception("Unable to like")
