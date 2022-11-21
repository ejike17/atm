class Atm:
    #Constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.trials = 4


        if self.pin == '':
            print("Welcome, first time using this card, please create a pin")
            self.create_pin()

        self.menu()

    def menu(self):
        user_input = input("""
            How would you like to proceed?
            1. Enter 1 to change our pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit
        """)

        if user_input == '1':
            self.create_pin()
            self.more()
        elif user_input == '2':
            self.pin_use()
            self.deposit()
            self.more()
        elif user_input == '3':
            self.pin_use()
            self.withdraw()
            self.more()
        elif user_input == '4':
            self.pin_use()
            print(f"Your account balance is ${self.balance}")
            self.more()
        else:
            print("Exiting....Bye")

# For creating a new pin for new user
    def create_pin(self):
        pin = input("Enter your new pin\n")
        pin_confirmation = input("Enter pin again for confirmation\n")
        if pin == pin_confirmation:
            self.pin = pin
            print("Pin set ")
        else:
            print("Pin entered does not match, start again")
            quit()

    def pin_use(self):
        pins = input("Enter your pin\n")
        if pins != self.pin:
            self.trials -= 1
            print(f"Wrong pin. You have {self.trials} trials left")
            print("Your card and account will be blocked when you exhaust you trials.")
            if self.trials == 0:
                print("Your account and card has been blocked. Visit any nearest branch for revalidation.")
                quit()
            self.pin_use()

    def deposit(self):
        amount = input("Enter amount to be deposited\n")
        print(f"You deposited ${amount}\n")
        self.balance += int(amount)

    def withdraw(self):
        withdraw_amount = input("Enter amount to withdraw\n")
        if int(withdraw_amount) > self.balance:
            print("Insufficient Balance")
        else:
            print(f"You have withdrawn ${withdraw_amount}\n")
            self.balance -= int(withdraw_amount)

    def more(self):
        print("Would you like to do something else?")
        decision = input("Enter yes or no\n")
        if decision.lower() == 'yes':
            self.menu()
        else:
            print("Thank you for banking with us")
            quit()

Atm()