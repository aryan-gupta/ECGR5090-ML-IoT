

class person:
    def __init__(self):
        self.name = ""
        self.age = -1
        self.height = -1 # rounded to nearest cm
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self):
        return "{:} is {:} years old and {:} cm tall".format(self.name, self.age, self.height)