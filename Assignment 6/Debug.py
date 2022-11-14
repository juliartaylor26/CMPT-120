class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee:
    def __init__(self, name, id_number, department):
        self.name = name
        self.id_number = id_number
        self.department = department


class Cake:
    def __init__(self, cake_flavor, frosting_flavor):
        self.name = name
        self.cake_flavor = cake_flavor
        self.frosting_flavor = frosting_flavor

    #   can you fill out the rest of this for me? im dumb
    #   the cake needs to have the cake flavor and cake frosting stored


def main():
    #   fill this one out with a dog's name and age... can be your dog, friend's dog, etc
    dog1 = Dog("Parker", 8)
    print(dog1.name, dog1.age)

    #   and what about a new employee
    new_employee = Employee("Johnson", 54321, "Elevator Music")
    #   how would we print out each of the variables from new_employee?
    print(new_employee.name, new_employee.id_number, new_employee.department)

    #   now create and print out a cake you make

    # and now create another cake and print it out


main()
