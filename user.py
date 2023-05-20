class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f'Name:{self.first_name} {self.last_name}')

    def greeting_user(self):
        print(f'Hello {self.first_name}! My sincere congratulations')

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


user1 = User("John", "Doe", 25, "New York")
user2 = User("Alice", "Smith", 30, "London")
user3 = User("Bob", "Johnson", 35, "San Francisco")

user1.describe_user()
user1.greeting_user()

user2.describe_user()
user2.greeting_user()

user3.describe_user()
user3.greeting_user()

user_4 = User("David", "Green", 40, "Kivy")
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()

print(f"{user_4.first_name} has {user_4.login_attempts} login attempts.")

user_4.reset_login_attempts()
print(f"{user_4.first_name} has {user_4.login_attempts} login attempts.")

class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]
        self.priv = Privileges()

    def show_privileges(self):
        print(f"{self.last_name} has such privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("Niki", "Sobo", 18, "Bremen")
admin.show_privileges()
admin.priv.show_privileges()