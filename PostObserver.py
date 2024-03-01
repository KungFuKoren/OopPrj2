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
            notification = f"{user.getName()} liked your post"
            self.myself.add_notification(notification)
            print(f"notification to {self.myself.userName}: {notification}")


    def commented(self, user, text):
        if (isinstance(user, User)) and user != self.myself:
            notification = f"{user.getName()} commented on your post"
            self.myself.add_notification(notification)
            print(f"notification to {self.myself.userName}: {notification}: {text}")
        else:
            raise Exception("invalid input")
