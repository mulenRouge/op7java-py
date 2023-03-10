class User_DB:
    users = dict()
    id = 0

    @staticmethod
    def init():
        users = dict()
        id = 0
        return User_DB.users

    @staticmethod
    def add_user(user):
        User_DB.users[User_DB.id] = user
        User_DB.id += 1