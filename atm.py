class Atm:
    #Constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0


        if self.pin == '':
            self.create_pin()

        self.menu()

    def menu(self):
        user_input = input("""
            How would you like to proceed?
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit
        """)

        if user_input == '1':
            self.create_pin()
            self.more()
        elif user_input == '2':
            self.deposit()
            self.more()
        elif user_input == '3':
            self.withdraw()
            self.more()
        elif user_input == '4':
            print(f"Your account balance is ${self.balance}")
            self.more()
        else:
            print("Exiting....Bye")

    def create_pin(self):
        pin = input("Create your pin\n")
        pin_confirmation = input("Enter pin again for confirmation\n")
        if pin == pin_confirmation:
            self.pin = pin
            print("Pin set ")
        else:
            print("Pin entered does not match, start again")
            quit()

    def deposit(self):
        amount = input("Enter amount to be deposited\n")
        print(f"You deposited ${amount}\n")
        self.balance += int(amount)

    def withdraw(self):
        withdraw_amount = input("Enter amount to withdraw\n")
        print(f"You have deposited ${withdraw_amount}\n")
        self.balance -= int(withdraw_amount)

    def more(self):
        print("Would you like to do something else?")
        decision = input("Enter yes or no\n")
        if decision.lower() == 'yes':
            self.menu()
        else:
            quit()

Atm()