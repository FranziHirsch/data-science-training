class User:
    pass

# create an instance/ object of the class

user1=User()

print(user1) #<__main__.User object at 0x0000014381C771D0>

print(type(user1)) #<class '__main__.User'>

# Define what attributes a user should have
class User:

    def __init__(self, name, age, email):
        self.name=name
        self.age=age
        self.email=email

    #Instance methods

    # Define some user methods (why methods - not functions? Because when I call them, they will be attached to an object, see below)

    # The below are instance methods, not class methods. I.e. every instance of "User" has its own methods

    # Note: I always need to include "self" as the 1st argument. Python assumes that this will always be the 1st
    # argument, so if I don't include it, it throws an error

    # This method returns the user's name
    def say_name(self):
        return f"{self.name}"

    # This method says whether the user is 18 or older
    def user_age(self):
        if self.age >= 18:
            return "The user is old enough"
        else:
            return "The user is too young"

    # I can also include an attribute in the method
    def user_score(self, score):
        return f"{self.name}'s score is {score}"

    # Can also change the attributes

    def birthday(self):
        self.age+=1
        return f"Happy {self.age}'th birthday, {self.name}"

# Initiate an instance of user
u1=User("Joe", 25, "joe@gmail.com")

# print(u1.age) #25
#
# print(u1.say_name()) #Joe
#
# print(u1.user_age()) #The user is old enough
#
# print((u1.user_score(100))) #Joe's score is 100
#
# print(u1.birthday()) #Happy 26'th birthday, Joe

# Exercise

class BankAccount:

    def __init__(self, owner, balance=0.0):
        self.owner=owner
        self.balance=balance

    def deposit(self, d):
        self.balance+=d
        return f"The new balance is {self.balance}."

    def withdraw(self, w):
        self.balance-=w
        return f"The new balance is {self.balance}."

a1=BankAccount("Franzi")

# print(a1.deposit(10))
# print(a1.withdraw(5))
# print(a1.balance)





# Class attributes

# Back to class User. Say we have a chat & want to monitor the no of active users
# Enter class attribute at the top of the class

class User:

    # This is the class method
    active_users=0

    def __init__(self, name, age, email):
        self.name=name
        self.age=age
        self.email=email

# The class method is called like this:
# print(User.active_users) #0


# Say each time a user is initialised, 1 should be added to active_users

class User:

    # This is the class method
    active_users=0

    def __init__(self, name, age, email):
        self.name=name
        self.age=age
        self.email=email
        User.active_users+=1

    def logout(self):
        User.active_users-=1
        # return print(f"{self.name} has logged out.")

u1=User("Harry", 18, "abc@abc.com")

# The class method is called like this:
# print(User.active_users) #1

# User.logout(u1)

# The class method is called like this:
# print(User.active_users)
#Harry has logged out.
#0


# Another common use case for class methods is for validation

# Say we have a class "Pets" - to prevent us from creating a 3-headed dog or an elephant

class Pets:

    # Enter list of allowed pets
    allowed=["dog", "cat", "fish", "rabbit"]

    def __init__(self, name, species):
        # Don't allow an instance to be created if the species is not in allowed
        if species not in Pets.allowed:
            raise ValueError(f"You can't have a {species}!")
        self.name=name
        self.species=species

# p1=Pets("Minka", "cat")
# p2=Pets("Tony", "tiger") #ValueError: You can't have a tiger!



# Since we only need the attribute in __innit__ we could just move the list to __innit__

class Pets:



    def __init__(self, name, species):
        # Enter list of allowed pets
        allowed = ["dog", "cat", "fish", "rabbit"]
        # Don't allow an instance to be created if the species is not in allowed
        if species not in allowed:
            raise ValueError(f"You can't have a {species}!")
        self.name=name
        self.species=species


# p2=Pets("Tony", "tiger") #ValueError: You can't have a tiger!

# However, if I want to use the allowed list in another method, I would have to copy the list again
# So it's better to have as a class attribute



class Pets:

    # Enter list of allowed pets
    allowed=["dog", "cat", "fish", "rabbit"]

    def __init__(self, name, species):
        # Don't allow an instance to be created if the species is not in allowed
        if species not in Pets.allowed:
            raise ValueError(f"You can't have a {species}!")
        self.name=name
        self.species=species

    def set_species(self, species):
        if species not in Pets.allowed:
            raise ValueError(f"You can't have a {species}!")
        self.species=species

# Add a pet to the list of allowed
Pets.allowed.append("hamster")

p3=Pets("Paul", "cat")
p3.set_species("hamster")
print(p3.species) #hamster



# Exercise - Chicken Coop

class Chicken:

    total_eggs=0

    def __init__(self, name, species, eggs_laid=0):
        self.name=name
        self.species=species
        self.eggs_laid=eggs_laid

    def add_eggs(self, n):
        self.eggs_laid+=n
        Chicken.total_eggs+=n

    def count_eggs(self): #This returns the no of eggs each chicken laid
        return print(f"{self.name} laid a total of {self.eggs_laid} eggs")

    def count_total(self):#This returns the total no of eggs
        return print(f"The total no of eggs is {Chicken.total_eggs}")

c1=Chicken("Betty", "normal")
c2=Chicken("Susi", "blue")

# print(Chicken.count_eggs(c1))
# print(Chicken.count_eggs(c2))
#
# Chicken.add_eggs(c1, 3)
# Chicken.add_eggs(c2, 2)

# print(Chicken.count_eggs(c1))
# print(Chicken.count_eggs(c2))
# print(Chicken.total_eggs)



# Class methods

class User:

    active_users=0

    # Create a class method to return the no of active users
    # Note: don't have to put add to the top

    # Use decorator
    @classmethod
    def display_active(cls): #cls = class - to signify that we're not working with an instance but a class
        return print(f"There are {User.active_users} active users")

    # Another example...
    # Say we want to create a user from a string, e.g. "Tom, 80, t@hotmail.com"
    # We can't pass this string into User
    # But we can create a user from a class method
    @classmethod
    def from_string(cls, string):
        # Split string from commas
        name, age, email=string.split(",")
        return cls(name, age, email) #What's happening here?
        # cls refers to the class itself, so User. And we define attributes of each instance of User below
        # So this method allows us to create an instance of User

    def __init__(self, name, age, email):
        self.name=name
        self.age=age
        self.email=email
        User.active_users+=1

    # This method returns the user's name
    def say_name(self):
        return f"{self.name}"

    # This method says whether the user is 18 or older
    def user_age(self):
        if self.age >= 18:
            return "The user is old enough"
        else:
            return "The user is too young"

    # I can also include an attribute in the method
    def user_score(self, score):
        return f"{self.name}'s score is {score}"

    def logout(self):
        User.active_users-=1
        # return print(f"{self.name} has logged out.")

u1=User.from_string("Tom, 80, t@hotmail.com")
print(u1.name) #Tom



#