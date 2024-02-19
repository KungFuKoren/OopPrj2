from typing import List
from User import User

class SocialNetwork():
    

    def __init__(self , name):
        self.userList: List[User] = []
        self.userNames: List[str] = []
      #  self.userPasswords: List[str] = []
        self.activeUsers: List[str] = []
        if type(name) == str:
            self.name = name
        else:
            raise Exception("invalid name")

    def getName(self):
        return self.name        
    
    def sign_up(self , userName , userPass):
        if type(userName) == str and type(userPass) == str:
            if len(userPass) > 8 or len(userPass) < 4:
                raise Exception("invalid password")
            elif userName in self.userName:
                raise Exception("User already exists")
            else:
                self.userList.append(User(userName , userPass))
                self.userNames.append(userName)
                self.userPasswords.append(userPass)
                self.activeUsers.append(userName)
        else: raise Exception("Invaid type of input") 


    def log_in(self , userName , passWord):
        if type(userName) == str and userName in self.userNames and userName not in self.activeUsers:
            index = self.userNames.index(userName)
            if self.userList[index].passWord == passWord:
                self.activeUsers.append(userName)
        else: raise Exception("Unable to log in")        

    def log_out(self , userName):
        if userName in self.activeUsers:
            self.activeUsers.remove(userName)
        else: raise Exception("User already logged out or User do not exist")    