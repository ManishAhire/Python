class Animal:

    name = ""

    def eat(self):
        print("I can eat")


class Dog(Animal):

    # override eat() method
    def eat(self):
        super().eat()
        print("I like to eat bones")

    def display_name(self):
        # access name attribute of superclass using self
        print("\nMy Name is: ", self.name)


# create an object of the subclass
labrabor = Dog()

# access superclass attribute and method
labrabor.name = "Sonu"
labrabor.eat()

# call subclass method
labrabor.display_name()
