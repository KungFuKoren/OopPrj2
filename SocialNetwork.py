from typing import List
from User import User

class SocialNetwork():
    

    def __init__(self , name):
        self.userList: List[User] = []
        self.userNames: List[str] = []
        if type(name) == str:
            self.name = name
        else:
            raise Exception("invalid name")

    def getName(self):
        return self.name        
    
    def sign_up(self , userName , userPass):
        if len(userPass) > 8 or len(userPass) < 4:
            raise Exception("invalid password")
        elif userName in self.userName:
            raise Exception("User already exists")
        else:
            self.userList.append(User(userName , userPass))
            self.userNames.append(userName)
