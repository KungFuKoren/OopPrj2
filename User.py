from typing import List

class User():
    #use observer design for notifications maybe ?
    
    def __init__(self , userName , passWord):
        from Post import Post
        from PostFactory import PostFactory
        self.logged = True
        self.userName = userName
        self.passWord = passWord
        self.post_list: List[Post] = []
        self.friends_list: List[str] = []
        self.notif_list = []
        self.followsMe: List[User] = []
        self.post_factory = PostFactory()

    def __str__(self):
        return f'User name: {self.getName()}, Number of posts: {self.howManyPosts()} Number of followers: {self.numOfFollowers()} '

    def howManyPosts(self):
        return len(self.post_list)

    def numOfFollowers(self):
        return len(self.followsMe)    

    def getName(self):
        return self.userName
    
    def follow(self , user):        
        if not isinstance(user , User):
            raise Exception("Invalid input")
        elif  user.userName in self.friends_list:
            raise Exception("Already follows")
        else: 
            print(f"{user.userName} started following {self.userName}")
            self.friends_list.append(user.userName)
            user.followsMe.append(self)


    def unfollow(self , user):
        if not isinstance(user , User):
            raise Exception("Invalid input")
        elif user.userName not in self.friends_list:
            raise Exception("You do not follow this user")
        else:
            print("removed")
            self.friends_list.remove(user.userName)
            user.followsMe.remove(self) 

    #implement factory design pattern
    def publish_post(self , type , content, price = None, location = None):
        if not self.logged:
            raise Exception("user must be logged in")
        if not isinstance(type , str) or content == "" or type not in {"Text", "Image", "Sale"}:
            raise Exception("not a valid input")
        post = self.post_factory.createPost(self, type , content, price, location)
        self.post_list.append(post)
        return post
        

   
