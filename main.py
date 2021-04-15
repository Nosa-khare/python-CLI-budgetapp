

class BudgetApp:

    accountBalance = 13300000

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

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def checkBalance(self):
        pass
