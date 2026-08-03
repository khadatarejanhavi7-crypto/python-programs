import random
import string

class PasswordGenerator:

    def __init__(self, username, length):
        self.username = username
        self.length = length

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""

        for i in range(self.length):
            password = password + random.choice(characters)

        return password

    def password_strength(self):
        if self.length >= 12:
            return "Strong Password"
        elif self.length >= 8:
            return "Medium Password"
        else:
            return "Weak Password"

    def display(self):
        print("------------------------------")
        print("Username :", self.username)
        print("Password Length :", self.length)
        print("Generated Password :", self.generate_password())
        print("Password Strength :", self.password_strength())
        print("------------------------------")


P1 = PasswordGenerator("Janhavi", 8)
P2 = PasswordGenerator("CodeVerse", 14)

P1.display()
P2.display()