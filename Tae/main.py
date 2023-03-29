## JAVA Study TIL 2월 


#2023.02.20
#print("Hello world!")

#Variables
#a = 2
#b = 3
#c = a + b
#print(c)

#my_age = 88
#my age 띄워쓰기 X
#숫자로 시작 X

#Booleans and Strings
#my_name = "tae_yong"
#my_name = "1212" <- 숫자가 아닌 문자
#my_name = True , False
#print(my_name)

#Recap
#my_name = "tae_yong"
#age = 21
#dead = False
#print("Hello my name is ",my_name)
#print("and I'm ",age," years old")

#Functions
#def say_hello():
#  print("hello how r u?")

#def say_bye():
#  print("bye bye")

#say_hello()

#Parameters
#def say_hello(name):
#  print("hello",name,"how r u?")

#say_hello("tae_yong")

#Multiple Parameters
#def say_hello(name,age):
#  print("hello",name)
#  print("you are",age,"years old")
#say_hello("tae_yong",21)

#Recap
#def tax_calculator(money):
#  print(money * 0.35)

#tax_calculator(8456213)

#Default Parameters
#def say_hello(name="anonymous"):
#  print("hello",name)

#say_hello("tae_yong")
#say_hello()

#Retrun Values
#def tax_calculator(money):
#  return money * 0.35

#def pay_tax(tax):
#  print("thank you for paying",tax)

#to_pay = tax_calculator(12345135)
#pay_tax(to_pay)

#Retrun Recap
#my_name = "tae_yong"
#my_age = 21
#my_color_eyes = "black"

#print(f"Hello I'm {my_name}, I have {my_age} years in the earth,{my_color_eyes} is my eye color")

#def make_juice(fruit):
#  return f"{fruit}+🍹"

#def add_ice(juice):
#  return f"{juice}+🧊"

#def add_sugar(iced_juice):
#  return f"{iced_juice}+🍬"

#juice = make_juice("🍎")
#cold_juice = add_ice(juice)
#perfect_juice = add_sugar(cold_juice)

#print(perfect_juice)



#2023.02.22
#If
#if 10 > 5:
#  print("Correct!")

#if 10 == 10:
#  print("True!")

#password_correct = False
#if password_correct:
#  print("Here is your money")
#else:
#  print("Wrong password")

# winner = 10
# if winner > 10:
#  print("winner is greater than 10")
# elif winner < 10:
#  print("Winner is less than 10")
# else:
#  print("winner is 10")

# And & Or
# age = int(input("How old are you?"))

# if age < 18:
#   print("You can't drink")
# elif age > 18 and age < 35:
#   print("You drink beer!")
# elif age == 60 or age == 70:
#   print("Birthday party!")
# else:
#   print("Go aghead!")

# Python Standard Library
