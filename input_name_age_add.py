# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

    #return name_func,age_func,add_func
def get_user_input(name_func,age_func,add_func) :
    name_func
    age_func 
    add_func 

    print(f"Hi, my name is {name_func}. I am {age_func} years old and I live in {add_func} . ")
    
# steps
# 1. ask name, age, and address
name = input("Name: ")
age = int(input("Age: "))
add = input("Address: ")
# 2. display name, age, and address
display = get_user_input(name,age,add)
