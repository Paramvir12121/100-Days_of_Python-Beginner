class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 =User("Param", 1)
user2 =User("Anjali", 2)

print(user1.name)

print(user1.followers)
user1.follow(user2)
print(user1.followers)