#Task 1: Write a function that lets the user add items to a list
def add_to_list(item):
    #add the item the user provided to the list, then sort the list
    user_list.append(item)
    user_list.sort()

#Task 2: Include a function to remove items from the list
def remove_from_list(item):
    #pass the item given by the user to remove from the list
    user_list.remove(item)

#Task 3: Add a function that prints out the entire list in a formatted way
def print_list():
    #iterate through the entire list manipulated by the user
    for i in range(len(user_list)):
        #print out each item numerically
        print(str(i + 1) + ". " + user_list[i])

#create an empty list for the user to change with the predefined functions
user_list = []
#create another variable that will be used as the loop condition and trigger to exit the loop
user_option = ""
#make another variable to pass items the user wants to add or remove from their list
user_item = ""

#as long as the user doesn't choose to quit, the loop will continue to prompt more options
while user_option.lower() != "quit":
    user_option = input("What action would you like to take? (add, remove, or quit) ")

    #when the user selects add, the user will provide an item to add to the list
    if user_option.lower() == "add":
        user_item = input("What item would you like to add to your list? ")
        user_item = user_item.lower()
        #pass the item from the user into the defined function to add
        add_to_list(user_item)

    #when remove is selected, the user enters an item to be removed from their list
    elif user_option.lower() == "remove":
        user_item = input("What item would you like to remove from your list? ")
        user_item = user_item.lower()

        #handle excpetion for user trying to remove an item that doesn't exist in the list
        if user_item not in user_list:
            print(user_item + " is not in your list.")
        #if item does exist, remove it
        else:
            remove_from_list(user_item)
    
    #if given the print option, print the list
    elif user_option.lower() == "print":
        print("Here is your current list:")
        print_list()

    #if the user wants to quit, break out of the loop
    elif user_option.lower() == "quit":
        break

    #handle the exception for if the user makes an invalid selection
    else:
        print("Please make a valid selection.")