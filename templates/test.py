class Dog: 

    def __init__(self, name): 
        self.name = name

    def bark(self): 
        return 'woof'

    def get_name(self): 
        return self.name

    # def __str__(self): 
    #     return f"This dogs name is {self.name}"

    def __repr__(self): 
        return f"This dogs name is {self.name}"

    def __eq__(self, other): 
        return self.name == other.name

    def __hash__(self): 
        return hash(self.name)

    def __lt__(self, other): 
        return self.name < other.name

    def __le__(self, other): 
        return self.name <= other.name

    def __gt__(self, other): 
        return self.name > other.name

    def __ge__(self, other): 
        return self.name >= other.name

    def __ne__(self, other): 
        return self.name != other.name

    def __add__(self, other): 
        return self.name + other.name

    def __sub__(self, other): 
        return self.name - other.name

    def __mul__(self, other): 
        return self.name * other.name

    def __truediv__(self, other): 
        return self.name / other.name

    def __floordiv__(self, other): 
        return self.name // other.name

    def __mod__(self, other): 
        return self.name % other.name

    def __pow__(self, other): 
        return self.name ** other.name

    def __lshift__(self, other): 
        return self.name << other.name

    def __rshift__(self, other): 
        return self.name >> other.name

    def __and__(self, other): 
        return self.name & other.name

    def __xor__(self, other): 
        return self.name ^ other.name

    def __or__(self, other): 
        return self.name | other.name

    def __neg__(self): 
        return -self.name

    def __pos__(self): 
        return +self.name

    def __abs__(self): 
        return abs(self.name)

    def __invert__(self): 
        return ~self.name

    def __round__(self, n): 
        return round(self.name, n)

    def __floor__(self): 
        return math.floor(self.name)
    
# fluffy = Dog('fluffy')

# print(fluffy.bark())

woof = Dog('woof')

# woof > fluffy

# woof % fluffy

print(woof)