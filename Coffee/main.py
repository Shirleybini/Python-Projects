from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


My_Menu = Menu()
MakeCoffee = CoffeeMaker()
Money = MoneyMachine()

Machine_working = True
while Machine_working:
  choice = input("What do you want? espresso, latte, cappuccino: ").lower()
  if choice == 'off':
    Machine_working = False
  
  elif choice == 'report':
    MakeCoffee.report()
    Money.report()
    
  else:
    drink = My_Menu.find_drink(choice)
    if MakeCoffee.is_resource_sufficient(drink) and Money.make_payment(drink.cost):
      MakeCoffee.make_coffee(drink)





