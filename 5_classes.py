
class User:

    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.id = id

    def print_details(self):
        print(f"User with name {self.name} has the id {self.id} and the email {self.email}")

    def __str__(self):
        return f"User {self.name}, id {self.id}, email {self.email}"


if __name__ == '__main__':
    user1 = User(id=1, name="Adrian", email="adrian@email.com")
    user2 = User(id=2, name="Jhon", email="jhon@email.com")

    user1.print_details()
    print(user1)

    #open classes principle
    user1.location = "Cluj"

    print(isinstance(user1, User))
    print(isinstance(user2, User))

    print(f"User {user1} is located in {user1.location}")
    print(f"User {user2} is located in {user2.location}")