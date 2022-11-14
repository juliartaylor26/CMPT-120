def main():
    # a variable with the value of a double
    double_value = 18.5

    # a variable with the value of an integer
    int_value = 17

    # prints out addition, subtraction, multiplication, and division of these two values
    print(double_value + int_value)
    print(double_value - int_value)
    print(double_value * int_value)
    print(int_value / double_value)

    # list of friends
    my_friends = ["Grace M", "Grace H", "Hannah G", "Hannah P", "Jasmine E", "Jasmine Z", "Josh S", "Jackson S",
                  "Ryan K"]

    # prints out friends at index 2 and index 3
    print(my_friends[2], "and", my_friends[3])

    # list of five numbers
    five_numbers = [1, 28, 8, 4, 21]

    # prints four equations that use numbers from five_numbers
    print(five_numbers[0] + five_numbers[3])
    print(five_numbers[1] - five_numbers[4])
    print(five_numbers[2] * five_numbers[3])
    print(five_numbers[1] / five_numbers[3])

    # replaces two of the numbers in the list with a different number
    five_numbers.insert(4, 0)
    five_numbers.remove(21)

    # prints out the list
    print(five_numbers)


main()
