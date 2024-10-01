
def q1():
  #Write Assignment code here
  bool=True
  bool1=False
  print(bool and bool1)
  print(bool or bool1)

def q2():
  #Write Assignment code here
  num=input("Enter a integer: ")
  num=not(num=="0")
  print(num)


def q3():
  #Write Assignment code here
  num =int(input("Enter a number: "))
  result = (0 <= num <= 10)
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

q1()
q2()
q3()
q4()
q5()
