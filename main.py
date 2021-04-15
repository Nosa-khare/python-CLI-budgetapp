import textwrap as tw

wallet = 100000


class BudgetApp:
    categories = {
        "1": {
            "name": "Food",
            "balance": 1122334,
            "limit": 100
        },

        "2": {
            "name": "Clothing",
            "balance": 1122334,
            "limit": 100
        },

        "3": {
            "name": "Gas & Transportation",
            "balance": 1122334,
            "limit": 100
        },

        "4": {
            "name": "Data & Airtime",
            "balance": 1122334,
            "limit": 100
        },

        "5": {
            "name": "Groceries & Utilities",
            "balance": 1122334,
            "limit": 100
        },

        "6": {
            "name": "Insurance",
            "balance": 1122334,
            "limit": 100
        },

        "7": {
            "name": "Emergencies",
            "balance": 1122334,
            "limit": 100
        },

        "8": {
            "name": "Savings",
            "balance": 1122334,
            "limit": 100
        },

    }

    def __init__(self, category):
        self.category = category
        self.name = self.categories[category]['name']

        self.introduceCategory()

    def introduceCategory(self):
        print(f"\n{'*' * 8} {self.name} Budget {'*' * 8}")
        self.action()

    def action(self):
        pass

    def deposit(self, ):
        pass

    def withdraw(self, amount):
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

    for key, value in BudgetApp.categories.items():
        print(f"{key}. {value['name']}")

    category = input("Select an option\n---> ")

    try:
        if int(category) <= len(BudgetApp.categories):
            category = str(category)

            BudgetApp(category)

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
