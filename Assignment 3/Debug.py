def main():
    # Can you print out "Hello" 8 times? I gave you a tiny hint to start...
    for x in range(8):
        print("Hello")

    print("________")

    # What about as a while loop?
    loops = 1
    while loops < 9:
        print("Hello")
        loops = loops + 1

    # The loop iterations are one behind in a non-programming counting way... how can we fix this?
    count = 1
    while count < 4:
        print("While loop iteration", count)
        count = count + 1

    # Same deal here!
    y = 1
    for y in range(1, 4):
        print("For loop iteration:", y)

    # Uh oh I messed up and made an infinite loop... so silly of me!
    endless = 4
    while endless < 5:
        print("I'm no longer stuck in this loop!!!!")
        endless = endless + 1

    # print out your last name one letter at a time
    for x in "Taylor":
        print(x)

    # aw i suck i made another infinite loop.. use that thing I taught you about to get out once it prints once...
    # starts with a b... br....
    found = False
    while not found:
        print("i only printed once")
        break

    # can you fill this out so that it prints found when it hits the letter r?
    for z in "Marist":
        if z == "r":
            print("found")
            break

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # you could print out the list using print(numbers) OR you could go the long way and use a for loop to print out
    # the value of each index :)
    for h in range(len(numbers)):
        print(numbers[h])

    # what if I wanted you to print out only the even numbers in this range I made?
    for p in range(20, 501):
        # i feeeeel like modulooooooo is neededddd
        if p % 2 == 0:
            print(p)


main()
