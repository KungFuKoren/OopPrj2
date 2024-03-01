from typing import List
from User import User


class SocialNetwork():
    # singleton implementation
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, 'initialized'):
            if type(name) == str:
                self.userList = {}
                self.userNames: List[str] = []
                # self.activeUsers: List[str] = []
                self.name = name
                self.initialized = True
                print(f"The social network {self.name} was created!")
            else:
                raise Exception("invalid name")
        else:
            raise Exception("Cant create another network")

    def __str__(self):
        ans = f"{self.name} social network:\n"
        for user in self.userList:
            ans += self.userList[user].__str__() + '\n'
        return ans

    def getName(self):
        return self.name

    def sign_up(self, userName, userPass):
        if type(userName) == str and type(userPass) == str:
            if len(userPass) > 8 or len(userPass) < 4:
                raise Exception("invalid password")
            elif userName in self.userNames:
                raise Exception("User already exists")
            else:
                _User = User(userName, userPass)
                self.userList[_User.userName] = _User
                self.userNames.append(userName)
                return _User
        else:
            raise Exception("Invaid type of input")

    def log_in(self, userName, passWord):
        if type(userName) == str and userName in self.userNames and not self.userList[userName].logged:
            if self.userList[userName].passWord == passWord:
                self.userList[userName].logged = True
                print(f"{userName} connected")

        else:
            raise Exception("Unable to log in")

    def log_out(self, userName):
        if not self.userList[userName].logged:
            raise Exception("User already logged out or User do not exist")

        self.userList[userName].logged = False
        print(f"{userName} disconnected")
