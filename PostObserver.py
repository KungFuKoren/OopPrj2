from User import User
from Post import Post


class PostObserver():
    def __init__(self, post):
        if isinstance(post, Post):
            self.myself = post.getUser()
        else:
            raise Exception("Unavailable input")

    def liked(self, user):
        if not isinstance(user, User):
            raise Exception("invalid input")
        if user != self.myself:
            self.myself.add_notification(f"{user.getName()} liked your post")

    def commented(self, user):
        if (isinstance(user, User)) and user != self.myself:
            self.myself.add_notification(
                f"{user.getName()} commented on your post")
        else:
            raise Exception("invalid input")
