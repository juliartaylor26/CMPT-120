def print_hello():
    print("Hello")


def print_name(x):
    print(x)


def addition(x, y):
    return x + y


def smaller(i, j):
    if i < j:
        return i
    elif j < i:
        return j
    elif i == j:
        return 0


def main():
    print_hello()
    print_name("Julia")

    var1 = 10
    var2 = 20
    print(addition(var1, var2))

    num1 = int(input("Enter number 1"))
    num2 = int(input("Enter number 2"))
    print(smaller(num1, num2))


main()
