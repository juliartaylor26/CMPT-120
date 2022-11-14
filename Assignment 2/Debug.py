# instructions: Something about these if statements aren't giving the desired effect. Look at them and see how to fix
# them. (Run them yourself and see what the output is!) also, we have some input practice!

def main():
    # this is a nice solid working one!
    name = input("your name is? ")
    print("Hello, ", name)

    # this isn't printing anything :( so sad. what's wrong with her? Why she not printing out?
    color = input("what's your favorite color? ")
    print(color)

    # I thought i did this right :( can you fix it for me?
    age = input("how old are you? ")
    print("You are ", age, " years old")

    # Start with this one! We have a compilation error :(
    # Side note: you can put these statements in parentheses or not. it's up to you.
    if 5 > 3:
        print("5 is greater than 3")

    # There are multiple correct answers and adjustments to this one
    is_not_five = 6
    if is_not_five > 5:
        print(is_not_five, "is greater than 5")
    else:
        print(is_not_five, "is less than 5")

    # more multiple correct answers. Similar to the first. Adjust as perceived
    to_check = 4
    if to_check > 5:
        print(to_check, "is greater than 5.")
    elif to_check < 3:
        print(to_check)
    else:
        print(to_check, "is greater than 3")

    # Is it really printing the BEST option though? Rearrange these as you see fit
    to_check = 5
    if to_check < 6 and to_check < 7 and to_check == 5:
        print("5 is less than 6 and 7, and 5 is equal to 5.")
    else:
        print("to_check is invalid")


main()
