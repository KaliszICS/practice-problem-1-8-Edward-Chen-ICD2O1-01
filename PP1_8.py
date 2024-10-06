
def q1():
  #Write Assignment code here
  bool1=True
  bool2=False
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  #Write Assignment code here
  num = int(input("Enter an integer: "))
  num2 = bool(num)  
  print(num2)


  

def q3():
  #Write Assignment code here
  num = int(input("Enter a number: "))
  result= num in range(0, 11)
  print(result)


def q4():
  #Write Assignment code here
  food = input("Input food: ")
  drink = input("Input drink: ")

  foodanddrink = not (food == "pizza" and drink == "pop")
  print(foodanddrink)
def q5():
  #Write Assignment code here
  num = int(input("Enter an integer: "))
  even = (num % 2)
  print(even)

#Do not edit code after this
#Comment out the followwing code when running tests

# q1()
# q2()
# q3()
# q4()
# q5()
