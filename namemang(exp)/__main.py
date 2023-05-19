class Map:
    def __init__(self):
        self.__geek()

    def geek(self):
        print("In parent class")

        # private copy of original geek() method
    __geek = geek


class MapSubclass(Map):

    # provides new signature for geek() but
    # does not break __init__()
    def geek(self):
        print("In Child class")




# Driver's code
obj = MapSubclass()
obj.geek()

squares = tuple(x**2 for x in range(10))