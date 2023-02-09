class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    # instance methods
    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password


# BankUser subclass
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    # instance methods
    def show_balance(self):
        print(f"{self.name} has an account balance of: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, receiver, amount, pin):
        print("you are transferring", amount, "to", receiver)
        print("Authentication required")
        check_pin = input(("Enter your pin"))
        if self.pin == pin:
            print("Transfer authorized")
            print(f"Transferring ${amount} to {receiver}")
            receiver.balance += amount
            self.balance -= amount
            return True
        else:
            return False



    def request_money(self, sender, amount, pin, receiver, password):
        print("you are transferring", amount, "to", sender)
        print("Authentication required")
        check_pin = input(("Enter your pin"))
        if self.pin == pin and sender.password == password:
            sender.balance -= amount
            self.balance += amount
            return True
        else:
            return False
bankuser2 = BankUser("Alic", 5678, "verynew")
bank_user1 = BankUser("Bob", 1234, "password")
bank_user1.show_balance()
bank_user1.deposit(float(5000))
bank_user1.transfer_money(500, bankuser2, 5678)
bank_user1.show_balance()
bankuser2.show_balance()
bank_user1.withdraw(float(500))
bankuser2.request_money(2000, bank_user1, 200, 5678, "password")
bankuser2.show_balance()
bank_user1.show_balance()





