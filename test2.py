#just a joke
from os import read


money = 3000
nigga = True
hungry = False
poor = True
if money <=1000:
    print(money + 99)
elif money <0:
    print(money/100)
else:
    print("get a discount")
if nigga and hungry:
    print("eat")
elif nigga or hungry and poor:
    print("GO steal some kfc")
readin = input("Enter your name: ")
change_values = input("do u want to change the values? (yes/no): ")
if change_values == "yes":
    money = int(input("Enter your money: "))
    nigga = input("Are you a nigga? (yes/no): ") 
    hungry = input("Are you hungry? (yes/no): ") 
    poor = input("Are you poor? (yes/no): ")
if money < 0:
    print(f"go get a job nigga, {readin}!")
elif 100<money < 1000:
    print(f"you're doing okay, {readin}")
else:
    print(f"you're rich, {readin}!")    