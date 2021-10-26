# Python program to illustrate the use of
# @property decorator

# Defining class
class Portal:

    # Defining __init__ method
    def __init__(self):
        self.__name = ''

    # Using @property decorator
    @property
    # Getter method
    def name(self):
        return self.__name

    # Setter method
    @name.setter
    def name(self, val: str):
        self.__name = val.capitalize() + ' alto turro el dani'

    # Deleter method
    @name.deleter
    def name(self):
        del self.__name


# Creating obj
p = Portal();

# Setting name
p.name = 'GeeksforGeeks'

# Prints name
print(p.name)

# Deletes name
del p.name

p.name = 'tricky'
print(p.name)