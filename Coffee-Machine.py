# Coffee-Machine
import time

# Creating variables for the 5 products and their respective prices. 
product_1, product_1_price, product1Origin = "Cappacino", 500, "Italy"
product_2, product_2_price, product2Origin = "Espresso", 400, "Italy"
product_3, product_3_price, product3Origin = "Americano", 450, "Italy"
product_4, product_4_price, product4Origin = "Flat White", 500, "New Zealand"
product_5, product_5_price, product5Origin = "Long Black", 600,"Australia"

print ("Welcome to the Python Coffee Machine. Here is the Our List Of Coffee Available Rightnow")
time.sleep(2)

print ("Item: {}, Price {},Origin {} ".format(product_1, product_1_price, product1Origin))
print ("Item: {}, Price {},Origin {} ".format(product_2, product_2_price, product2Origin))
print ("Item: {}, Price {},Origin {} ".format(product_3, product_3_price, product3Origin))
print ("Item: {}, Price {},Origin {} ".format(product_4, product_4_price, product4Origin))
print ("Item: {}, Price {},Origin {} ".format(product_5, product_5_price, product5Origin))
print ("")
# Asking the user how much money they wish to enter.
num_of_10 = int(input("How many 10 Rupee Coins would you like to insert? "))
while num_of_10 < 0:
    num_of_10 = int(input("Please enter a positive number."))
num_of_20 = int(input("How many 20 Rupee Notes would you like to insert? "))
while num_of_20 < 0:
    num_of_20 = int(input("Please enter a positive number."))
num_of_50 = int(input("How many 50 Rupee Notes would you like to insert? "))
while num_of_50 < 0:
    num_of_50 = int(input("Please enter a positive number."))
num_of_100 = int(input("How many 100 Rupee Notes would you like to insert? "))
while num_of_100 < 0:
    num_of_100 = int(input("Please enter a positive number."))
# Creating a variable to store the total amount of money inserted into the vending machine.
change = round(((num_of_10 * 10) + (num_of_20 * 20) + (num_of_50 * 50) + (num_of_100 * 100)),2)
# Informing the user how much they have entered in total.
print ("\nIn total you have entered Rs", change)
time.sleep(2)

# Creating variables to track the number of each items bought,
Cappuccino_bought = 0
Espresso_bought = 0
Americano_bought = 0
Flat_White_bought = 0
Long_Black_bought = 0
# Informing the user of the choices available and the prices that of each item.
print ("There are 5 products available to pick from;\n")
time.sleep(2)
print ("Item_1: {}, Price {}".format(product_1, product_1_price))
print ("Item_2: {}, Price {}".format(product_2, product_2_price))
print ("Item_3: {}, Price {}".format(product_3, product_3_price))
print ("Item_4: {}, Price {}".format(product_4, product_4_price))
print ("Item_5: {}, Price {}".format(product_5, product_5_price))
print ("")
# Asking the user to make a selection.
while change > 0:
    customer_choice = input("What would you like to buy? Enter Item Number. Type N when you are finished \n")
    if customer_choice == "1" and change >= product_1_price:
        print ("You have chosen a", product_1, "these cost", product_1_price, "each,")
        change = round((change - product_1_price),2)
        Cappuccino_bought = (Cappuccino_bought + 1)
        print ("You have this much money remaining: Rs", change)
    elif customer_choice == "2" and change >= product_2_price:
        print ("You have chosen a", product_2, "these cost", product_2_price, "each,")
        change = round((change - product_2_price),2)
        Espresso_bought = (Espresso_bought + 1)
        print ("You have this much money remaining: Rs", change)
    elif customer_choice == "3" and change >= product_3_price:
        print ("You have chosen a", product_3, "these cost", product_3_price, "each,")
        change = round((change - product_3_price),2)
        Americano_bought = (Americano_bought + 1)
        print ("You have this much money remaining: Rs", change)
    elif customer_choice == "4" and change >= product_4_price:
        print ("You have chosen a", product_4, "these cost", product_4_price, "each,")
        change = round((change - product_4_price),2)
        Flat_White_bought = (Flat_White_bought + 1)
        print ("You have this much money remaining: Rs", change)
    elif customer_choice == "5" and change >= product_5_price:
        print ("You have chosen a", product_5, "these cost", product_5_price, "each,")
        change = round((change - product_5_price),2)
        Long_Black_bought = (Long_Black_bought + 1)
        print ("You have this much money remaining: Rs", change)
    elif customer_choice == "N" or customer_choice == "n":
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (product_1, "x", Cappuccino_bought)
        print (product_2, "x", Espresso_bought)
        print (product_3, "x", Americano_bought)
        print (product_4, "x", Flat_White_bought)
        print (product_5, "x", Long_Black_bought)
        print ("You have Rs", change, "remaining.")
        break
    elif change <= 0:
        print ("You have run out of money.")
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (product_1, "x", Cappuccino_bought)
        print (product_2, "x", Espresso_bought)
        print (product_3, "x", Americano_bought)
        print (product_4, "x", Flat_White_bought)
        print (product_5, "x", Long_Black_bought)
        break
    else:
        print ("There has been an error or you may not have enough credit.")
