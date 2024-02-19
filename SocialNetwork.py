from typing import List
from User import User

class SocialNetwork():
    #singleton implementation
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
        return cls._instance

    def __init__(self , name):
        if not hasattr(self, 'initialized'):
            if type(name) == str:  
                self.userList: List[User] = []
                self.userNames: List[str] = []
                self.activeUsers: List[str] = []
                self.name = name
                self.initialized = True
            else:
                raise Exception("invalid name")
        else: raise Exception("Cant create another network")    

    def getName(self):
        return self.name        
    
    def sign_up(self , userName , userPass):
        if type(userName) == str and type(userPass) == str:
            if len(userPass) > 8 or len(userPass) < 4:
                raise Exception("invalid password")
            elif userName in self.userNames:
                raise Exception("User already exists")
            else:
                _User = User(userName , userPass)
                self.userList.append(_User)
                self.userNames.append(userName)
                self.activeUsers.append(userName)
                return _User
        else: raise Exception("Invaid type of input") 


    def log_in(self , userName , passWord):
        if type(userName) == str and userName in self.userNames and userName not in self.activeUsers:
            index = self.userNames.index(userName)
            if self.userList[index].passWord == passWord:
                for i in self.userList:
                    if self.userList[i].name == userName:
                        self.userList[i].logged = True
                self.activeUsers.append(userName)
        else: raise Exception("Unable to log in")        

    def log_out(self , userName):
        if userName in self.activeUsers:
            for i in self.userList:
                if self.userList[i].name == userName:
                    self.userList[i].logged = False

            self.activeUsers.remove(userName)

        else: raise Exception("User already logged out or User do not exist")    