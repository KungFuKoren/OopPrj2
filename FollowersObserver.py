from Post import Post


class FollowersObserver():
    def __init__(self, user):
        self.user = user
        self.subscribers = set()

    def subscribe(self, user):
        from User import User
        if not isinstance(user, User):
            raise Exception("Must send user of type User")
        if (user in self.subscribers):
            return
        self.subscribers.add(user)

    def unsubscribe(self, user):
        from User import User
        if not isinstance(user, User):
            raise Exception("Must send user of type User")
        if (user not in self.subscribers):
            raise Exception(f"User is not following {self.user.userName}")
        self.subscribers.remove(user)

    def notifyToFollowers(self, post):
        if not isinstance(post, Post):
            raise Exception("Post to notify must be type of Post")
        for user in self.subscribers:
            user.add_notification(f"{self.user.userName} has a new post")

    def is_a_follower(self, user):
        from User import User
        if not isinstance(user, User):
            raise Exception("Must send user of type User")
        return user in self.subscribers

    def followers_amount(self):
        return len(self.subscribers)
