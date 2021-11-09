#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.

def amount_money_and_price_apples (amount_of_money,price_of_apples) :
    amount_of_money
    price_of_apples
    maximum_apples = amount_of_money//price_of_apples
    apple_price = price_of_apples*maximum_apples
    remaining_money = amount_of_money-apple_price

    print('You can buy', (int(maximum_apples)), 'apples and your change is', (float(remaining_money)))

# steps 
#1. enter how much money do you have, ask how much is the apple and calculate the maximum number of apples that you can buy and calculate the remaining money that you will have
amount_of_money = float(input("Enter money: ")) 
price_of_apples = float(input("Enter price of apple: "))
#2. display the output
apples_and_excess_money = amount_money_and_price_apples (amount_of_money,price_of_apples)
