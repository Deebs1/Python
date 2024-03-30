class Deeapp:
    def __init__(self):
        self.users = {}
    def create_user(self, username, pword):
        print(self.users)
        if username in self.users:
            print("User already present")
        else:
            self.users[username] = pword
            print("User registered successfully")
            print(self.users)

    def login_user(self, username, pword):
        print(self.users[username])
        if self.users[username]==pword:
            print("user logged in successfully")
        else:
            print("user doesnot exist")

app = Deeapp()
username = "dee"
pword = 123
app.create_user(username, pword)
app.login_user(username, pword)

