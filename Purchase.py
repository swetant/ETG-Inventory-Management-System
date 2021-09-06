import json
import add_Prod
fd=open("records.json","r")
txt=fd.read()
fd.close()
records=json.loads(txt)
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
def purchase_Prod():
    us=input("Do you want to buy any medicine(y for yes or n for no): ")
    if us=="y":
        no_prod=int(input("How many medicines you want to buy: "))
        Prod=[]
        price=[]
        Bill=0
        fd = open("sales.json", 'r')
        txt1 = fd.read()
        fd.close()
        sales=json.loads(txt1)
        keys=list(sales.keys())
        i=int(keys[-1])
        while no_prod>0:
            ui_prod = str(input("Enter the product_Id: "))
            ui_quant = int(input("Enter the quantity: "))
            Prod.append(records[ui_prod]['name'])
            price.append(records[ui_prod]['Price'])
            Bill +=(records[ui_prod]['Price'] * ui_quant)
            records[ui_prod]['quant'] = records[ui_prod]['quant'] - ui_quant
            no_prod-=1
            sales[i+1]={"name":records[ui_prod]["name"],'prod': ui_prod, 'quant': ui_quant, 'Billing Price': records[ui_prod]['Price'] * ui_quant}
            i+=1
        for i in range(len(Prod)):
            print("Product: ", Prod[i])
            print("Price: ", price[i])
        print("Billing Amount: ", Bill)
        print("******Thank You for shopping******")
        sale=json.dumps(sales)
        fd = open("sales.json", 'w')
        fd.write(sale)
        fd.close()
    else:
        print("Thanks for coming...")
if __name__=="__main__":
    print("*********Welcome to Pharmacy Shop*********")
    ans = input("Are you the Owner of this store Y for yes or N for no ")
    if ans=="n" or ans=="N":
        view_Prod()
        purchase_Prod()
        js = json.dumps(records)
        fd = open("records.json", 'w')
        fd.write(js)
        fd.close()
        verify_Prod=input("*****Type v to view available quantities---> ")
        if verify_Prod=="v":
            view_Prod()
        view_sale=input("*****Type v to view all sales---> ")
        if view_sale=="v":
            view_sales()
    else:
        add_Prod.add_Products()
        js = json.dumps(records)
        fd = open("records.json", 'w')
        fd.write(js)
        fd.close()
        check_prod = input("Want to view the products list(Y or N): ")
        if check_prod == "Y":
            for i in records:
                print(str(records[i]).split(","))
        else:
            print("Thanks for adding product!")
