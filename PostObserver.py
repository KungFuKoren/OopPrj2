from User import User
from Post import Post

class PostObserver():
    def __init__(self , post):
        if isinstance(post , Post):
            self.myself = post.getUser()
        else: raise Exception("Unavailable input")    

    def liked(self , user):
        if(isinstance(user,User)) and user != self.myeslf:       
            self.myself.add_notification(f"{user.getName()} liked your post")
        else: raise Exception("invalid input")  

    def commented(self , user):
        if(isinstance(user,User)) and user != self.myeslf:
            self.myself.add_notification(f"{user.getName()} commented on your post")
        else: raise Exception("invalid input")   