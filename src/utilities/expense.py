# Expense class to represent an individual expense entry

class Expense:

    def __init__(self, category, amount, date, description):
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
            "description": self.description
        }
