from source.User_DB import User_DB


class User_Service:
    @staticmethod
    def save_user(user, users):
        User_DB.add_user(user)