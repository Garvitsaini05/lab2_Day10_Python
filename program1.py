# Menu Driven Program-------------------///////////////////

shoppingCart={}
print("")
print("!!.....WELCOME TO THE AMANDO SHOPPING SITE.....!!")
print("")
enter=input("FOR MENU Press ENTER.....!!")

while (enter!=6):


    if enter == "":
            print("!!....MENU....!!\n 1. Add a product to the cart.\n 2. Search for a product.\n 3. Delete a product from the cart.\n 4. Display the contents of the cart.\n 5. Purchase items.\n 6. Quit.\n ")
    print("")
    print("Type the MENU NUMBER you want to perform...")
    WTD=int(input(":- "))
    print("")


#FOR-1--------------------------************************
if WTD == 1:
    a=int(input("How many ITEMS to add :- "))
    i=1
    while i<=a:
        if a >=6:
            print("SORRY, You can only enter 5 ITEMS at a time...!")
            break
        else:
            x=input(f"Enter product {i} & brand name :- ")
            y=input(f"Enter product {i}-price :- ")
            shoppingCart.update({x:y})
            i=i+1

            print("")

#FOR-2--------------------------************************
if WTD == 2:
    print("What to search..?\n 1. Whole Cart.\n 2. Specific Item.")
    b=int(input(":- "))
    i=1
    while i == 1:
        if b == 2:
            p=input("Product-name :- ")
            if p in shoppingCart:
                print(p," : ",shoppingCart[p])
            else:
                print("No product exists with this name.!!!!!")
        else:
            print(shoppingCart)
        i=i+1

        print("")


#FOR-3--------------------------************************
if WTD == 3:
    delete=input("DELETE SOMETHING.........??? (y/n):- ")
    if delete == "y":
        print("what to DELETE")
        c=input(":- ")
        if c in shoppingCart:
            shoppingCart.pop(c)
        else:
            print("Product not found in cart")

        print("Updated DATA")
        print(shoppingCart)
    else:
        print("Okay")
    print("")


#FOR-4--------------------------************************
if WTD == 4:
    print("")
    print(shoppingCart)

#FOR-5--------------------------************************
if WTD == 5:
    d = input("Complete Purchase.....? (y/n) :- ")
    if d == "y":
        
        print("Thank you for your business.")
        del shoppingCart
    elif d == "n":
        print("Please continue shopping")
    else:
        print("Please answer either Y or N.")

#FOR-6--------------------------************************
if WTD == 6:
    print("Terminating..........")




    if enter == "":
            print("!!....MENU....!!\n 1. Add a product to the cart.\n 2. Search for a product.\n 3. Delete a product from the cart.\n 4. Display the contents of the cart.\n 5. Purchase items.\n 6. Quit.\n ")
    print("")
    print("Type the MENU NUMBER you want to perform...")
    WTD=int(input(":- "))
    print("")