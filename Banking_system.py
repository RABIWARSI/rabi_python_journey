class Bank_info:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amount):
        self.balance += amount
        print(f"Your amount deposited successfully. Your balance after deposit is: {self.balance}")

    def with_draw(self, amount, entered_password):
        if self.password == entered_password:
            if self.balance >= amount:
                self.balance -= amount
                print("Withdrawal is successful.")
            else:
                print("Sorry! Insufficient amount in your account.")
        else:
            print("Incorrect Password.")

# Object creation and method calling
b1 = Bank_info("Rabi", 5000, "abcd")
b1.deposit(1000)
b1.with_draw(500, "abcd")
