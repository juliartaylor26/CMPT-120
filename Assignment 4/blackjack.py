import random


def bust(first, second, third):
    total = first + second + third
    if total <= 21:
        return total
    elif total > 21:
        return 0
    elif total > 21 and (first == 11 or second == 11 or third == 11):
        return total - 10


def main():
    first_number = random.randint(1, 11)
    print(first_number)
    second_number = random.randint(1, 11)
    print(second_number)
    third_number = random.randint(1, 11)
    print(third_number)
    print(bust(first_number, second_number, third_number))


main()
