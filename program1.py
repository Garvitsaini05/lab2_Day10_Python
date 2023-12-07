# Menu Driven Program-------------------///////////////////

shoppingCart={}

print("")
print("!!.....WELCOME TO THE AMANDO SHOPPING SITE.....!!")
print("")
enter=input("FOR MENU Press ENTER.....!!")
if enter == "":
    print(" 1. Add a product to the cart.\n 2. Search for a product.\n 3. Delete a product from the cart.\n 4. Display the contents of the cart.\n 5. Display the contents of the cart.\n 6. Quit.\n ")

print("Type the MENU NUMBER you want to perform...")
WTD=int(input(":- "))

#FOR-1--------------------------************************
if WTD == 1:
    a=int(input("How many ITEMS to add :- "))
    i=1
    while i<=a:
        if a >=6:
            print("SORRY, You can only enter 5 ITEMS at a time...!")
            break
        else:
            x=input(f"Enter product{i}-name:- ")
            y=input(f"Enter product{i}-price :- ")
            z=input(f"Enter product{i}-brand :- ")
            shoppingCart.update({x:y})
            i=i+1
print(shoppingCart)
#FOR-2--------------------------************************
if WTD == 2:
    a=int(input("What to search :- "))