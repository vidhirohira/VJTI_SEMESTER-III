# Violation of SRP
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_db(self):
        # Code to save user data to the database
        pass

# Following SRP
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save_to_db(self, user):
        # Code to save user data to the database
        pass
