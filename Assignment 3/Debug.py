def main():
    
    #Can you print out "Hello" 8 times? I gave you a tiny hint to start...
    for x in range(8):
        print("Hello")

    print("________")

    #What about as a while loop?
    loops = 1
    while (loops < 9):
        print("Hello")
        loops = loops + 1
        
    
    #The loop iterations are one behind in a non-programming counting way... how can we fix this?
    count = 1
    while (count < 4):
        print("While loop iteration", count)
        count = count + 1
        
    #Same deal here!
    y = 1
    for y in range(1, 4):
        print("For loop iteration:", y)
     
    #Uh oh I messed up and made an infinite loop... so silly of me!   
    endless = 4    
    while (endless < 5):
        print("I'm no longer stuck in this loop!!!!")
        endless = endless + 1
    
    
    
main()
