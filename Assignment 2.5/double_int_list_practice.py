def main():
  
  #set this to any double
  doubleValue = 18.5
  
  #set this to any int
  intValue = 17
  
  #print out addition, subtraction, multiplication, and division of these two values

  print(doubleValue + intValue)
  print(doubleValue - intValue)
  print(doubleValue * intValue)
  print(intValue / doubleValue)

  
  #populate this list
  myFriends = ["Grace M", "Grace H", "Hannah G", "Hannah P", "Jasmine E", "Jasmine Z", "Josh S", "Jackson S", "Ryan K"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2], "and", myFriends[3])
  
  #populate this list with five numbers
  fiveNumbers = [1, 28, 8, 4, 21]
  
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[0] + fiveNumbers[3])
  print(fiveNumbers[0] - fiveNumbers[3])
  print(fiveNumbers[0] * fiveNumbers[3])
  print(fiveNumbers[0] / fiveNumbers[3])

  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)

  fiveNumbers.insert(4, 0)
  fiveNumbers.remove(21)


  #print out the list
  print(fiveNumbers)
  
main()
