import textwrap as tw

wallet = 100000


class Budget:
    categories = {
        "1": {
            "name": "Food",
            "balance": 0.00,
            "limit": 100
        },

        "2": {
            "name": "Clothing",
            "balance": 0.00,
            "limit": 100
        },

        "3": {
            "name": "Gas & Transportation",
            "balance": 0.00,
            "limit": 100
        },

        "4": {
            "name": "Data & Airtime",
            "balance": 0.00,
            "limit": 100
        },

        "5": {
            "name": "Groceries & Utilities",
            "balance": 0.00,
            "limit": 100
        },

        "6": {
            "name": "Insurance",
            "balance": 0.00,
            "limit": 100
        },

        "7": {
            "name": "Emergencies",
            "balance": 0.00,
            "limit": 100
        },

        "8": {
            "name": "Savings",
            "balance": 0.00,
            "limit": 100
        },

    }

    def __init__(self, category):
        self.category = category
        self.name = self.categories[category]['name']

        self.introduceCategory(category)

    def introduceCategory(self,category):
        print(f"\n{'*' * 8} {self.name} Budget {'*' * 8}")

        self.operation(category)

    def operation(self, category):

        budgetOperation = input(tw.dedent("""
                                What would you like to do?
                                1. Deposit
                                2. Withdraw
                                3. Check balance
                                4. Switch budget category
                                5. Go back to home page
                                ---> """))

        if budgetOperation == "1":
            self.deposit(category)

        elif budgetOperation == "2":
            self.withdraw()

        elif budgetOperation == "3":
            self.checkBalance()

        elif budgetOperation == "4":
            selectBudget()

        elif budgetOperation == "5":
            init()

        else:
            print("Invalid option")
            init()

    def deposit(self, category):
        print(self.categories[category]['balance'])
        depositAmount = input("How much would you like to deposit?\n---> $")

        try:
            if int(depositAmount) >= wallet:
                self.categories[category]['balance'] += float(depositAmount)
                print(tw.dedent(f"""
                            ${depositAmount} deposited successfully!
                            {self.name} budget balance: ${self.categories[category]['balance']}
                            """))
                self.operation(category)
            else:
                print("Insufficient funds available in wallet")
                self.operation(category)

        except ValueError:
            print("Invalid amount entered")
            self.deposit(category)

    def withdraw(self):
        pass

    def checkBalance(self):
        pass


def init():
    operation = input(tw.dedent("""
                        What would you like to do?
                        
                        1. Create a new budget
                        2. Access existing budgets
                        3. Add to wallet
                        4. logout
                        ---> """))

    if operation == "1":
        createBudget()
    elif operation == "2":
        selectBudget()
    elif operation == "3":
        addToWallet()
    elif operation == "4":
        exit()
    else:
        print("Invalid option")
        init()


def createBudget():
    pass


def selectBudget():
    print(f"\nWhat category would you like to access?\n")

    for key, value in Budget.categories.items():
        print(f"{key}. {value['name']}")

    category = input("Select an option\n---> ")

    try:
        if int(category) <= len(Budget.categories):
            category = str(category)

            Budget(category)

        else:
            print("Sorry category does not exist")
    except ValueError:
        print("Invalid input! Enter a number")


def addToWallet():
    pass


def endPage():
    pass


# App launch


print(tw.dedent("""
            Hi there! Welcome to BudgetApp
            """))
init()
