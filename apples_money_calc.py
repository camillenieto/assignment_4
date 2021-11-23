#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.
def maximum_apples() :
    amount_of_money = float((input("Enter money: ")))
    price_of_apples = float(input("Enter price of apple: "))
    maximum_of_apples = float(amount_of_money//price_of_apples)
    remaining_money = price_of_apples % maximum_of_apples
    return amount_of_money, price_of_apples, maximum_of_apples, remaining_money
  
def display_output(maximum_of_apples_f,remaining_money_f) :
    print(f"You can buy {maximum_of_apples_f} apples and your change is {remaining_money_f} pesos.")


amount_of_money_f, price_of_apples_f, maximum_of_apples_f, remaining_money_f = maximum_apples()
display_output(maximum_of_apples_f,remaining_money_f)


# steps 
#1. enter how much money do you have, how much is the apple and calculate the maximum number of apples that you can buy and calculate the remaining money that you will have
#money_f,apples_func = amount_money_and_price_apples ()
#2. display the output
#print(f"You can buy {amount_money_and_price_apples(money_f,apples_func)} apples and your change is {maximum_apple_and_remaining_money(apples_func,money_f)} pesos.")
