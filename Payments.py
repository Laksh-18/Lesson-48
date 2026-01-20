class Cash:
    def pay(self, amount):
        print("Paid", amount, "using Cash.")


class Card:
    def pay(self, amount):
        print("Paid", amount, "using Card.")


class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI App")


payments = [Cash(), Card(), UPI()]

for mode in payments:
    mode.pay(500)