class User:
    # initialise attributes
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "Karol")
user_2 = User("001", "Jack")


user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)

# user_1 = User("001")
# # adding attributes:
# # user_1.id = "001"
# user_1.username = "Karol"
# user_1.email = "Karol@python.eu"
# print(user_1.username)
#
# # construct defines what attributes should be passed to the object \
# # (to avoid manually adding) by object initialization by __init__
#
# user3 = User("003")
# print(user3.id)