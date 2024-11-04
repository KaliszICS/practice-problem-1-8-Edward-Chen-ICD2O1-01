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
  input = input("Enter a number: ")
  num = float(input)
  is_between = 0 <= num <= 10
  print(is_between)



def q4():
  #Write Assignment code here
  food = input("Input food: ")
  drink = input("Input drink: ")

  foodanddrink = not (food == "pizza" and drink == "pop")
  print(foodanddrink)
def q5():
  #Write Assignment code here
  input = input("Enter an integer: ")
  num = int(input)
  num2 = (num % 2 == 0)
  print(f"The integer {num} is {num2}.")


#Do not edit code after this
#Comment out the followwing code when running tests

# q1()
# q2()
# q3()
# q4()
# q5()
