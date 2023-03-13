import csv
import datetime
import time


# Pizza Class (SuperClass)
class Pizza:
    # Initialize default name and cost of pizzas
    def __init__(self):
        self.name = ""
        self.cost = 0.0

    def get_description(self):
        return self.name

    def get_cost(self):
        return self.cost


# Create subclasses of Pizza Class
class Classical(Pizza):
    def __init__(self):
        self.name = "Classical Pizza"
        self.cost = 10.0

class Margarita(Pizza):
    def __init__(self):
        self.name = "Margarita"
        self.cost = 120

class TurkishPizza(Pizza):
    # Initialize cost and name of pizza using Pizza Class
    def __init__(self):
        self.name = "Turkish Pizza"
        self.cost = 170

class PlainPizza(Pizza):
    def __init__(self):
        self.name = "Plain Pizza"
        self.cost = int(90)

# Decorator Class (SuperClass)
class Decorator(Pizza):
    def __init__(self, topping):
        self.topping = topping

    def get_description(self):
        return self.topping.get_description() + "\n" + Pizza.get_description(self)

    def get_cost(self):
        return self.topping.get_cost() + Pizza.get_cost(self)


# Create subclasses of Decorator Class
class Olive(Decorator):
    def __init__(self, topping):
        self.topping = topping
        self.name = "Olive"
        self.cost = 3

class Mushroom(Decorator):
    # Initialize name and cost of toppings
    def __init__(self, topping):
        self.topping = topping
        self.name = "Mushroom"
        self.cost = 5

class GoatCheese(Decorator):
    # Initialize name and cost of toppings
    def __init__(self, topping):
        self.topping = topping
        self.name = "Goat Cheese"
        self.cost = 4

class Meat(Decorator):
    def __init__(self, topping):
        self.topping = topping
        self.name = "Meat"
        self.cost = 10

class Onion(Decorator):
    def __init__(self, topping):
        self.topping = topping
        self.name = "Onion"
        self.cost = 3

class Corn(Decorator):
    def __init__(self, topping):
        self.topping = topping
        self.name = "Corn"
        self.cost = 2

# Create the User function to retrieve information from the user
def user():
    name = input("Enter your name : ")
    surname = input("Enter your surname : ")

    id_number = ""
    while True:
        id_number = input("Enter your ID number : ")
        if len(id_number) == 11:
            break
        print("Enter id number correctly, ID number must be 11 digits!")
    
    credit_card_number = ""
    while True:
        credit_card_number = input("Enter your credit card number : ")
        if len(credit_card_number) == 16:
            break
        print("Please enter credit card number correctly, credit card number must be 16 digits!")

    credit_card_date = input("Enter your credit card expiration date (**/**) : ")
    
    credit_card_security = ""
    while True:
        credit_card_security = input("Enter your credit card security code : ")
        if len(credit_card_security) == 3:
            break
        print("Please enter credit card security code correctly, credit card security code must be 3 digits!")
    
    credit_card_password = ""
    while True:
        credit_card_password = input("Enter your credit card password : ")
        if len(credit_card_password) == 4:
            break
    print("Please enter credit card password correctly, credit card password must be 4 digits!")

    print("Your information is being received.")
    time.sleep(2)
    print("Process completed!")
    
    return name, surname, id_number, credit_card_number, credit_card_date, credit_card_security, credit_card_password

# Create the Update function to add informations of users ("orders_database.csv" is created earlier.)
def update(name, surname, id_number, credit_card_number, credit_card_date, credit_card_security, credit_card_password):
    with open("orders_database.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, surname, id_number, credit_card_number, credit_card_date, credit_card_security, credit_card_password, datetime.datetime.now().strftime("%d-%m-%Y %H:%M")])
        
def main():
    # Print the contents of menu
    file = open("menu.txt", "r")
    contents = file.read()
    print(contents)

    # Choose the pizza
    prepared_pizza = ""
    while prepared_pizza == "":
        pizza = input("Choose your pizza (1 - 4) : ")
        if pizza == "1":
            prepared_pizza = Classical()
        elif pizza == "2":
            prepared_pizza = Margarita()
        elif pizza == "3":
            prepared_pizza = TurkishPizza()
        elif pizza == "4":
            prepared_pizza = PlainPizza()
        else:
            print("Please enter valid value!")
    
    # Choose the toppings
    selected_topping = ""
    while selected_topping == "":
        topping = input("Choose your topping (5 - 10) : ")
        if topping == "5":
            selected_topping = Olive(prepared_pizza)
        elif topping == "6":
            selected_topping = Mushroom(prepared_pizza)
        elif topping == "7":
            selected_topping = GoatCheese(prepared_pizza)
        elif topping == "8":
            selected_topping = Meat(prepared_pizza)
        elif topping == "9":
            selected_topping = Onion(prepared_pizza)
        elif topping == "10":
            selected_topping = Corn(prepared_pizza)
        else:
            print("Please enter valid value!")
    
    # Print description and total cost of prepared pizza
    totalCost = selected_topping.get_cost()
    descriptionOfPizza = selected_topping.get_description()

    print("Your pizza is prepared. Please wait!")
    time.sleep(5)
    print("Your pizza is ready!\nPizza's description is " + descriptionOfPizza + "\nPizza's total cost is " + str(totalCost) + " $\n")

    # Get information from users
    print("Complete the payment by entering your information\n")
    name, surname, id_number, credit_card_number, credit_card_date, credit_card_security, credit_card_password = user()

    # Update database with information from users
    update(name, surname, id_number, credit_card_number, credit_card_date, credit_card_security, credit_card_password)

    print("Payment is successful. Thanks for your order. We are waiting for you again.")


main()