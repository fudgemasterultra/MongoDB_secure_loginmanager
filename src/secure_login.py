from pymongo import MongoClient
from argon2 import PasswordHasher



class LoginGateway():
    #This will intilize the connection to your MongoDB atlast
    def __init__(self, connection_str:str, database:str ,collection:str = "login"):
        self.client = MongoClient(connection_str)
        self.client = self.client[database]
        self.client = self.client[collection]

    #This handles encrypting password, duplicate checking, and sending to database.
    def createuser(self, username:str, password:str, data:dict = None):
        dupcheck = self.client.find_one({"username": username})
        if dupcheck == None:
            payload = {}
            encrpytpassword = PasswordHasher().hash(password)
            if data:
                payload = {
                    "username" : username,
                    "password": encrpytpassword,
                    "data": data, 
                }
            else:
                payload = {
                    "username": username,
                    "password": encrpytpassword
                }
            self.client.insert_one(payload)
            return True, "Inserted"
        else:
            return False, "Duplicate"
    
    #This checks if user exsists then checks the input password against hash. 
    def login(self, username, password):
        finduser = self.client.find_one({"username": username})
        if finduser:
            encryptedpassword = finduser["password"]
            try:
                PasswordHasher().verify(encryptedpassword, password)
                return True, "Login"
            except:
                return False, "Incorect Password"