# MongoDB Secure Login Manager
This is a secure user account management template that is good for almost any project using MongoDB Atlas. This is built for Python.

## Description
MongoDB Secure Login Manager was created for use with Python programs that need to implement secure user authentication. You can store just the username and password or add your data and tie it to the user. Also uses ARGON 2 for password hashing. 

## Quick Start

```py
from secure_login import LoginGateway

    #First, you'll need your connection string:
    connection_str = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
    #It will need to know which database to connect to.
    database = "database"
    #Collection is optional; if it doesn't see one explicitly typed, it will create a collection called "login".
    collection = "login1"
    authPortal = LoginGateway(connection_str, database, collection)

    #Once you've intilized the LoginGateway, there are two functions you can use: "createuser" and "login".

    #Createuser will return two values: the first a bool telling if it could create user and the second is a string with a message for more details.
    success, message = authPortal.createuser("username", "password")
    print(success, message)
    #Likewise, login will return two values: the first being a bool telling if credentials match and the second is a string with more details. 
    success, message = authPortal.login("username", "password")
    print(success, message)
```

## FAQ
### When I look at my users, why can't I see their password?
You really shouldn't ever see your user's password. We send the password to be hashed by the ARGON 2 algorhythm, then when the user logs in, we check if the hashs are the same.
### How do I use this with a web framework like Flask?
You'd probably want to look into creating user authentication cookies and storing those inside the MongoDB document. 
