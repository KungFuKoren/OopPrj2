from typing import List


class User():
    # use observer design for notifications maybe ?

    def __init__(self, userName, passWord):
        from FollowersObserver import FollowersObserver
        from Post import Post
        from PostFactory import PostFactory
        self.logged = True
        self.userName = userName
        self.passWord = passWord
        self.post_list: List[Post] = []
        self.friends_list: List[str] = []
        self.notif_list: List[str] = []
        self.post_factory = PostFactory()
        self.followers_observer = FollowersObserver(self)

    def __str__(self):
        return f'User name: {self.getName()}, Number of posts: {self.howManyPosts()}, Number of followers: {self.numOfFollowers()} '

    def howManyPosts(self):
        return len(self.post_list)

    def numOfFollowers(self):
        return self.followers_observer.followers_amount()

    def getName(self):
        return self.userName

    def follow(self, user):
        if not isinstance(user, User):
            raise Exception("Invalid input")
        elif user.userName in self.friends_list:
            raise Exception("Already follows")
        else:
            print(f"{self.userName} started following {user.userName}")
            self.friends_list.append(user.userName)
            user.followers_observer.subscribe(self)

    def unfollow(self, user):
        if not isinstance(user, User):
            raise Exception("Invalid input")
        elif user.userName not in self.friends_list:
            raise Exception("You do not follow this user")
        else:
            print(f"{user.userName} unfollowed {self.userName}")
            self.friends_list.remove(user.userName)
            user.followers_observer.unsubscribe(self)

    # implement factory design pattern
    def publish_post(self, type, content, price=None, location=None):
        if not self.logged:
            raise Exception("user must be logged in")
        if not isinstance(type, str) or content == "" or type not in {"Text", "Image", "Sale"}:
            raise Exception("not a valid input")
        post = self.post_factory.createPost(
            self, type, content, price, location)
        self.post_list.append(post)
        self.followers_observer.notifyToFollowers(post)
        return post

    def add_notification(self, notification):
        if not isinstance(notification, str):
            raise Exception("Must send a string to notifications")
        self.notif_list.append(notification)

    def print_notifications(self):
        print(f"{self.userName} notifications:")
        for notification in self.notif_list:
            print(f"{notification}")
