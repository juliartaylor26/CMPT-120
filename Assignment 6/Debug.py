class Dog:
    def __init__(self, dog_name, age):
        self.dog_name = dog_name
        self.age = age


class Employee:
    def __init__(self, employee_name, id_number, department):
        self.employee_name = employee_name
        self.id_number = id_number
        self.department = department


class Cake:
    def __init__(self, cake_flavor, frosting_flavor):
        self.cake_flavor = cake_flavor
        self.frosting_flavor = frosting_flavor

    #   can you fill out the rest of this for me? im dumb
    #   the cake needs to have the cake flavor and cake frosting stored


def main():
    #   fill this one out with a dog's employee_name and age... can be your dog, friend's dog, etc
    dog1 = Dog("Parker", 8)
    print(dog1.dog_name, dog1.age)

    #   and what about a new employee
    new_employee = Employee("Johnson", 54321, "Elevator Music")
    #   how would we print out each of the variables from new_employee?
    print(new_employee.employee_name, new_employee.id_number, new_employee.department)

    #   now create and print out a cake you make
    bd_cake = Cake("Chocolate", "Chocolate")
    print(bd_cake.cake_flavor, bd_cake.frosting_flavor)
    # and now create another cake and print it out
    rando_cake = Cake("White", "Lemon")
    print(rando_cake.cake_flavor, rando_cake.frosting_flavor)


main()
