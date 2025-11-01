expense = []
def printmenu():
    print("\n--- Expense Tracker ---")
    print("1) Add expense")
    print("2) View all expenses")
    print("3) Summary (total by category)")
    print("4) Set/Check budget")
    print("5) Exit")
def addexpense(expense):
    date = input("enter date (YYYY-MM-DD): ")
    category = input("enter category (e.g., Food, Transport): ")
    amtstr = input("Enter amount: ")
    amount = float(amtstr)
    expense.append({'date': date, 'category': category, 'amount': amount})
    print("Expense added successfully.")
def viewexpenses(expense):
    if not expense:
        print("no expenses recorded.")
        return
    print("\nAll Expenses:")
    for i in expense:
        print(i['date'], i["category"], i['amount'])
def reportsummary(expense):
    if not expense:
        print("No expenses recorded.")
        return
    total=sum(i['amount'] for i in expense)
    print("\nTotal Expnses: {total}")
    bycategory = {}
    for i in expense:
        cat = i['category']
        amt = i['amount']
        if cat in bycategory:
            bycategory[cat] += amt
        else:
            bycategory[cat] = amt
    print("Expenses by Category:")
    for category, amount in bycategory.items():
        print(f"{category}: {amount}")
def main():
    budget= None
    while True:
        printmenu()
        choice = input("Choose an option: ")
        if choice == '1':
            addexpense(expense)
        elif choice == '2':
            viewexpenses(expense)
        elif choice == '3':
            reportsummary(expense)
        elif choice == '4':
            if budget == None:
                amt = input("Set your budget amount: ")
                budget = float(amt)
            print(f"Budget set to {budget}")
        elif choice == '5':
            totalexpenses = sum(i['amount'] for i in expense)
            print(f"Current budget: {budget}. Total expenses: {totalexpenses}")
            if totalexpenses > budget:
                    print("You have exceeded your budget!")
            else:
                print("You are within your budget.")
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()