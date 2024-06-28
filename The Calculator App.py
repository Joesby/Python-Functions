#Task 1: Create functions for each arithmetic operation
#Make a function that takes two numbers as parameters to add
def add(num1, num2):
    #Make a variable that adds the two numbers and assigns them to a sum variable and return the sum
    sum = num1 + num2
    
    return sum
    
#Make a function that takes two numbers as parameters to subtract
def subtract(num1, num2):
    #Make a variable that subtracts the second number from the first and return the difference
    difference = num1 - num2

    return difference

#Make a function that takes two numbers as parameters to multiply
def multiply(num1, num2):
    #Make a variable that multiplies the two numbers and return the product
    product = num1 * num2
    
    return product

#Make a function that takes two numbers as parameters to divide
def divide(num1, num2):
    #Make a variable that divides the first number by the second number and return the quotient
    quotient = num1 / num2

    return quotient

#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use
#promt the user with options to determine what mathmatical operation they want to perform
print("Which mathmatical operation would you like to perform?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
#request the user answer the prompt with a numer and convert it to an integer
user_selection = int(input("Please select a number: "))

#make sure the users answer is within the bounds of the selections, if not, request they input a number from the list of options
while user_selection <= 0 or user_selection >= 5:
    user_selection = int(input("I'm sorry, please select a number from 1 to 4: "))

#identify the numbers the user wants to use in their mathmatical operation
user_number_1 = int(input("What is the first number you want to use? "))
user_number_2 = int(input("What is the second number you want to use? "))

#Task 3: Ensure your code can handle division by zero and other potential errors
#If the user wants to divide, but their secondary number is 0, request they choose a different number to avoid a zero division error
while user_selection == 4 and user_number_2 == 0:
    user_number_2 = int(input("I'm sorry, you cannot divide by zero, please select another secondary number: "))
else:
    pass

#check each possible option and perform the corresponding mathmatical operation using the numbers previously given
if user_selection == 1:
    print(add(user_number_1, user_number_2))

elif user_selection == 2:
    print(subtract(user_number_1, user_number_2))

elif user_selection == 3:
    print(multiply(user_number_1, user_number_2))

elif user_selection == 4:
    print(divide(user_number_1, user_number_2))

else:
    print("Error, please try again.")
