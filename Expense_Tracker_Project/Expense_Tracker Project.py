#Expense Tracker Project

expenselist=[] # list of all expenses

print("Wel Come to Expense Tracker: ")
while True:
    print("====Menu====")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Cost")
    print("4. Exit")

    choice=int(input("Please Enter Your Choice: "))

#1. Add Expense
    if(choice==1):
        date=input("When you incur an expense: ")
        category=input("Which type of Expense: ")
        discription=input("Enter the more details of this expense: ")
        amount=float(input("Enter the Amount: "))

        expense={
            "date" : date,
            "category" : category,
            "discription" : discription,
            "amount" : amount,
        }

        expenselist.append(expense)
        print("\nExpense is add successfully ")

#2. View All Expense
    
    elif(choice==2):
        if(len(expenselist)==0):
            print("No Expense Add. so you can add expense")
        else:
            print("====This all is Your Expense====")
            count=1
            for eachexpense in expenselist:
                print(f"Expense Number {count} -> {eachexpense["date"]}, {eachexpense["category"]}, {eachexpense["discription"]}, {eachexpense["amount"]} ")
                count= count+1
            
#3. view Total Costing

    elif(choice==3):
        total=0
        for eachexpense in expenselist:
            total=total+eachexpense["amount"]

        print("\n Total Cost = ",total)

#4. Exit
    elif(choice == 4):
        print("Thank You for Visit")
        break

    else:
        print("Invalid Choice. Try Again")










