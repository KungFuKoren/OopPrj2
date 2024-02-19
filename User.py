from typing import List
from Post import Post

class User():
    #use observer design for notifications maybe ?
    
    def __init__(self , userName , passWord):
        self.userName = userName
        self.passWord = passWord
        self.post_list: List[Post] = []
        self.friends_list: List[str] = []
        self.notif_list = []




    def follow(self , user):        
        if not isinstance(user , User):
            raise Exception("Invalid input")
        
        elif  user.getName() in self.friends_list:
            raise Exception("Already follows")
        
        else: self.friends_list.append(user.getName())

    def unfollow(self , user):
        if not isinstance(user , User):
            raise Exception("Invalid input")
         
        elif user.getName() not in self.friends_list:
            raise Exception("You do not follow this user")
         
        else: self.friends_list.remove(user.getName)
         
    def getName(self):
        return self.userName

    def publish_post(self , type , text , price , location ):
        if isinstance(type , str):
            x = 1
        else: raise Exception("not a valid input")
        #publishes post , sends notification for followed users
        #         

    
    def like(self , post):
        #likes a post
        random = 11

    def comment(self , post):
        #comments on a post
        random =1

    def notifIfUpload(self , user):
        #gets notification if followed posted
        random = 1

    def notIfCom(self , user):
        #gets notification if someone liked or commented ur post (do not include self likes)        
        random = 1

    def getUserInfo(self):
        #user indo
        random = 11     

    def getAllNotif(self):
        #gets all notifications from oldest to new
        random = 1
