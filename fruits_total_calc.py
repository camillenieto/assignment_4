# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.


def get_apples_and_oranges(apples, oranges) :
    apple_price = apples * 20
    orange_price = oranges * 25
    sum_of_apples_and_oranges = apple_price+orange_price
    total_price = sum_of_apples_and_oranges

    print('The total amount is', total_price)

#def get_total_price(get_apples,) :
#apples = int(input("Enter apples: ")) 
#oranges = int(input("Enter oranges: "))
#total_apples_oranges = get_apples_and_oranges(apples, oranges)

# steps 
# 1. ask how many apples and oranges you want and the total amount you need to pay if apple is 20 pesos and orange is 25 pesos
apples = int(input("Enter apples: ")) 
oranges = int(input("Enter oranges: "))
# 2. display output
total_apples_oranges = get_apples_and_oranges(apples, oranges)