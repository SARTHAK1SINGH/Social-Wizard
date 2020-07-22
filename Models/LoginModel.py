import pymongo
import bcrypt
from pymongo import MongoClient


class LoginModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.socialwizard
        self.Users = self.db.users

    def check_user(self, data):
        user = self.Users.find_one({"username": data.username})

        if user:
            if bcrypt.checkpw(data.password.encode(), user["password"]):
                return user
            else:
                return False
        else:
            return False

    def update_info(self, data):
        update = self.Users.update_one({
            "username": data["username"]
        }, {"$set": data})

        return True