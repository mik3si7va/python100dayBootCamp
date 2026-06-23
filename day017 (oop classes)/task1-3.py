class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# Example usage:
user1 = User("Alice", 30)
print(user1.greet())  # Output: Hello, my name is Alice and I am 30 years old.

user1.id = 12345  # Adding a new attribute 'id' to the user1 instance
user1.username = "alice123"  # Adding a new attribute 'username' to the user1 instance
print(user1.id)  # Output: 12345
print(user1.username)  # Output: alice123