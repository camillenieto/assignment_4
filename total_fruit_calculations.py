# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def get_apples_and_oranges() :
    apples = int(input("Enter apples: ")) *20
    oranges = int(input("Enter oranges: ")) *25
    return apples, oranges

def total_amount(apples_sum, orange_sum) :
    return apples_sum + orange_sum


# steps 
# 1. ask how many apples and oranges you want and the total amount of it
apples_f, oranges_f = get_apples_and_oranges()
# 2. display output
print(f"The total amount is {total_amount(apples_f, oranges_f)}.")