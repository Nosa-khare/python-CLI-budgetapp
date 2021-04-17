import textwrap as tw


class Budget:
    wallet = 100000  # mutable, can undergo changes on deposits and withdrawals

    categories = {
        "1": {
            "name": "Food Budget",
            "balance": 1000,
            "warning": 100
        },

        "2": {
            "name": "Clothing Budget",
            "balance": 1000,
            "warning": 100
        },

        "3": {
            "name": "Gas & Transportation Budget",
            "balance": 1000,
            "warning": 100
        },

        "4": {
            "name": "Data & Airtime Budget",
            "balance": 1000,
            "warning": 100
        },

        "5": {
            "name": "Groceries & Utilities Budget",
            "balance": 1000,
            "warning": 100
        },

        "6": {
            "name": "Insurance Budget",
            "balance": 1000,
            "warning": 100
        },

        "7": {
            "name": "Emergencies Budget",
            "balance": 1000,
            "warning": 100
        },

        "8": {
            "name": "Savings Budget",
            "balance": 1000,
            "warning": 100
        },

    }

    def __init__(self, category):
        self.category = category
        self.name = self.categories[category]['name']

        self.introduceCategory(category)

    def introduceCategory(self, category):
        print(f"\n{'*' * 8} {self.name} {'*' * 8}")
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
            self.withdraw(category)

        elif budgetOperation == "3":
            print("Balance:", self.checkBalance(category))
            self.operation(category)

        elif budgetOperation == "4":
            selectBudget()

        elif budgetOperation == "5":
            init()

        elif " " in budgetOperation or budgetOperation == "":
            print("Clear whitespaces and an enter option")
            self.operation(category)

        else:
            print("Invalid option")
            init()

    def fetchWalletBalance(self):
        return Budget.wallet

    def updateWallet(self, value):
        Budget.wallet += value

    def newBalance(self, budget_name, balance):
        display = f"{budget_name} balance: ${balance}"
        return display

    def deposit(self, category):

        depositAmount = int(input("\nHow much would you like to deposit?\n---> $"))

        try:
            if depositAmount <= self.fetchWalletBalance():
                self.categories[category]['balance'] += depositAmount
                updateValue = -depositAmount
                self.updateWallet(updateValue)

                print("\nSuccess!!\n"
                      f"{self.newBalance(self.name, self.checkBalance(category))}\n"
                      f"{self.newBalance('Wallet', self.fetchWalletBalance())}"
                      )
                self.operation(category)
            else:
                print("\nFail!!\nInsufficient funds available in wallet")
                self.operation(category)

        except ValueError:
            print("\nFail!!\nInvalid amount entered")
            self.deposit(category)

    def withdraw(self, category):
        pass

        withdrawalType = input("\n1. Withdraw from budget balance into wallet\n"
                               "2. Transfer funds into another budget category\n--->")

        withdrawalAmount = int(input("\nHow much would you like to withdraw?\n---> "))

        try:
            if withdrawalAmount <= self.categories[category]["balance"]:  # check if account balance is sufficient to
                # dispense withdrawal amount

                if withdrawalType == "1":
                    self.updateWallet(withdrawalAmount)
                    self.categories[category]['balance'] -= withdrawalAmount

                    print("\nsuccess!!\n"
                          f"{self.newBalance('Wallet Balance', self.fetchWalletBalance())}\n"
                          f"{self.newBalance(self.name, self.checkBalance(category))}"
                          )
                    self.operation(category)

                elif withdrawalType == "2":
                    print("\nWhat budget category would you like to transfer into?")

                    for key, value in Budget.categories.items():
                        print(f"{key}. {value['name']}")

                    transferCategory = input("Select an option\n---> ")
                    self.categories[transferCategory]['balance'] += withdrawalAmount
                    self.categories[category]['balance'] -= withdrawalAmount

                    print("\nsuccess!!\n"
                          f"{self.newBalance(self.categories[transferCategory]['name'], self.checkBalance(transferCategory))}\n"
                          f"{self.newBalance(self.name, self.checkBalance(category))}"
                          )
                    self.operation(category)

                else:
                    print("Fail!!\nInvalid option selected")
                    self.withdraw(category)

            else:
                print("Fail!!\nInsufficient funds")

        except ValueError:
            print("Invalid input")
            self.withdraw(category)

    def checkBalance(self, category):
        balance = f"${self.categories[category]['balance']}"
        return balance


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

        if int(category) <= len(Budget.categories) and int(category) != 0:
            category = str(category)
            Budget(category)

        else:
            print("Sorry category does not exist")
            selectBudget()

    except ValueError:
        print("Invalid input! Enter a number")
        selectBudget()


def addToWallet():
    pass


def endPage():
    pass


# App launch


print(tw.dedent("""
            Hi there! Welcome to BudgetApp
            """))
init()
