# Administrator accounts list
adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]

# Build your login functions below
def getCreds():
    username = input("What is your username?: " )
    password = input("What is your password?: " )
    user_data = {}
    user_data["username"] = username
    user_data["password"] = password
    return(user_data)

def checkLogin(userInfo, adminList):
    for admin_credentials in adminList:
        if userInfo == admin_credentials:
            loggedIn = True
            break
        else:
            loggedIn = False
    return(loggedIn)

while True:
    userInfo = getCreds()
    userCheck = checkLogin(userInfo, adminList)
    print("---------")
    if checkLogin(userInfo, adminList) == True:
        print("YOU HAVE LOGGED IN!")
        break