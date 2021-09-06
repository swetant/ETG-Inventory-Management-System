import json
fd=open("records.json","r")
txt=fd.read()
fd.close()
records=json.loads(txt)
def update_Prod():
    pro_id=input("Enter Product Id: ")
    quant=int(input("Enter the quantity to add: "))
    records[pro_id]["quant"]=records[pro_id]["quant"]+quant;
    if quant!=0:
        print("Product remove successfully")
def view_sales():
    a = ["Prod_ID","Name", "Quantity", "Billing Price"]
    fd = open("sales.json", 'r')
    txt1 = fd.read()
    fd.close()
    sales = json.loads(txt1)
    for i in a:
        print(i.ljust(20, " "), end=" ")
    print()
    print("-----------------------------------------------------------------------------")
    for i in sales:
        print(str(sales[i]["prod"]).ljust(20," "), str(sales[i]["name"]).ljust(22, " "), str(sales[i]["quant"]).ljust(20, " "),str(sales[i]["Billing Price"]).ljust(20, " "))
        print("-----------------------------------------------------------------------------")
def view_Prod():
    a=["Prod ID","Prod_Name","Quantity","Price"]
    for i in a:
        print(i.ljust(20," "),end=" ")
    print()
    print("---------------------------------------------------------------------")
    for i in records:
        print(i.ljust(20," "),str(records[i]["name"]).ljust(22," "),str(records[i]["quant"]).ljust(20," "),str(records[i]["Price"]).ljust(20," "))
        print("---------------------------------------------------------------------")
def add_Products():
    no_prod=int(input("How many products you want to add? "))
    while(no_prod>0):
        id=input("Enter the product ID: ")
        name=input("Enter the product name: ")
        quant=int(input("Enter the quantity: "))
        price=int(input("Enter the price: "))
        desc=input("Enter Product description: ")
        manf = input("Enter Mfg Date: ")
        power = input("Enter Power of medicine: ")
        records[id]={'name':name,'quant':quant,'Price':price,'desc':desc,'manf':manf,'power':power}
        no_prod-=1
    print("Product added successfully")
def del_Products():
    no_prod = int(input("How many products you want to remove? "))
    while (no_prod > 0):
        id = input("Enter the product ID: ")
        del records[id]
        no_prod -= 1
    print("Product removed successfully")

if __name__=="__main__":
    print("<--------------------------------------------------------WELCOME TO PHARMACY SHOP-------------------------------------------------------------->")
    ans = input("Are you the Owner of this store Y for yes or N for no ")
    if ans == "Y" or ans == "y":
        print("Type r to remove Products")
        print("Type a to add new Products")
        print(("Type n to add existing Products"))
        print("Type e to exit")
        view=input()
        if view=="r":
            view_Prod()
            del_Products()
            view_Prod()
        elif view=="a":
            view_Prod()
            add_Products()
            view_Prod()
        elif view=="n":
            view_Prod()
            update_Prod()
            view_Prod()
        else:
            exit(0)
        js = json.dumps(records)
        fd = open("records.json", 'w')
        fd.write(js)
        fd.close()
    elif ans == "N" or ans == "n":
        pass
    else:
        print("Please enter valid input")
    fd = open("sales.json", "r")
    txt1 = fd.read()
    fd.close()
    sales = json.loads(txt1)
    check_prod = input("Want to view all the sales list(Y or N): ")
    if check_prod == "Y":
        view_sales()

