
Name = str #variable of the name item
price = float #variable of the price the product
quantity = int #variable product quantity
validate = True #variable to control the while loop for input validation
Total_cost = float # variable of the total purchase amount 


validate = True  # Variable used to control the loop

print("Welcome to the Inventory System")
print("--------------------------------")

while validate:
    try:
        # Ask the user for the product information
        name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the product quantity: "))

        # PROCESSING PHASE
        total_cost = price * quantity

        # If everything is correct, stop the loop
        validate = False

    except ValueError:
        # This message appears if the user enters invalid data
        print("Error: Please enter a valid number for price and quantity.")

# OUTPUT PHASE
print("\nInventory Summary")
print("------------------")
print(f"Product: {name}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total Cost: ${total_cost:.2f}")


