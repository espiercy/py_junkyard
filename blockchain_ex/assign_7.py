class Food:
    def __init__(self, name, kind):
        self.__name = name
        self.__kind = kind


    def describe(self):
        print("{} is a {}".format(self.__name, self.__kind))


    def get_name(self):
        return self.__name


    def get_kind(self):
        return self.__kind
    
    def __repr__(self):
        return("This {} is a kind of {}".format(self.get_name(), self.get_kind()))


class Meat(Food):
    def cook(self):
        print("I'm cooking the {}".format(self.get_name()))


class Fruit(Food):
    def clean(self):
        print("I'm cleaning the {}".format(self.get_name()))

food = Food("rice", "grain")
food.describe()
print(food)

meat = Meat("chicken", "poultry")
meat.describe()
print(meat)
meat.cook()

fruit = Fruit("tomato", "awful fruit")
fruit.describe()
print(fruit)
fruit.clean()