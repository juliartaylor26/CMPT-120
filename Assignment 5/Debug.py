def main():
    #good working example!
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")
        
    #can you google and find what function you should use to check if it's numeric (an int?)?
    intInput = input("enter an int")
    if intInput.isdigit():
        print("int!")
    else:
        print("not int :(")
    
    #what about if it's both letters and numbers?
    alphIntInput = input("Enter letters and numbers")
    if alphIntInput.isalnum():
        print("Letters and numbers!")
    else:
        print("weird characters :(")
       
    #good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")


    amperisk = input("Enter an asterisk [*] or an ampersand [&]")
    if amperisk == "*" or amperisk == "&":
        print("thanks!")
    else:
        print("darn")


   #now write code to check if the input was either an asterisk OR an ampersand (&)
    
        
    #do the live example we did in class: ask user to input an integer, but before you cast it to an int,
    #check that it's an integer before doing your variable = int(variable) command
    wantInt = input("Enter an integer")
    if wantInt.isdigit():
        wantInt = int(wantInt)
        print(wantInt)
    else:
        print("not an integer :(")


    # last challenge: find out how to check if the string input has the substring "marist"
    #google this one ;) substring is the key google term
    schoolName = input("Where do you go to school?")
    substring = "marist"
    if substring in schoolName:
        print("me too!")
    else:
        print("lame")


main()
