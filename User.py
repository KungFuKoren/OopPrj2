from typing import List

class User():
    #use observer design for notifications maybe ?
    
    def __init__(self , userName , passWord):
        from Post import Post
        from PostFactory import PostFactory
        logged = True
        self.userName = userName
        self.passWord = passWord
        self.post_list: List[Post] = []
        self.friends_list: List[str] = []
        self.notif_list = []
        self.followsMe: List[User] = []
        self.post_factory = PostFactory()

    def getName(self):
        return self.userName


    def follow(self , user):        
        if not isinstance(user , User):
            raise Exception("Invalid input")
        elif  user.userName in self.friends_list:
            raise Exception("Already follows")
        else: 
            print("followed")
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
        if not isinstance(type , str) or type not in {"Text", "Image", "Sale"}:
            raise Exception("not a valid input")
        post = self.post_factory.createPost(self, type , content, price, location)
        self.post_list.append(post)
        return post
        

    
    # def like(self , post):
    #      from Post import Post  
    #     if isinstance(post , Post):
    #         post.addLike(self)
    #     else: raise Exception("Invalid input")    


    # def comment(self , post , text):
    #     if isinstance(post , Post) and type(text) == str:
    #         post.addComment(self , text)
    #     else: raise Exception("Invalid input")


    # def notifIfUpload(self , user):
    #     #gets notification if followed posted
    #     random = 1


    # def notIfCom(self , user):
    #     #gets notification if someone liked or commented ur post (do not include self likes)        
    #     random = 1


    # def getUserInfo(self):
    #     #user indo
    #     random = 11     


    # def getAllNotif(self):
    #     #gets all notifications from oldest to new
    #     random = 1
