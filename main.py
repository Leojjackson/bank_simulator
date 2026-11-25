# Bank simulator
from time import sleep
class Bank:
    def __init__(self,saved_money = 0, owner = 'Jackson', locked_money = 0):
        self.saved_money = saved_money
        self.owner = owner
        self.locked_money = 1000

    def options(self):
         print("-" * 40)
         self.option = input('1) check current balance\n'
              '2) Add Money\n'
              '3) Withdraw Money\n'
              '4) Apply for a loan\n'
              '5) Exit\n'
              'Type an option: '
              )

    def process(self):
        while True:
            self.options()
            if self.option == '1':
                print("Checking your Sistem data...")
                sleep(2)
                print(f'This is Your Current Bank Balance: R${self.saved_money:.2f}')
                sleep(2)

            elif self.option == '2':
                add_money = int(input('Money to add to your account:R$ '))
                self.saved_money += add_money
                print('This Value is in progress to be Add to your bank account...')
                sleep(1.5)
                print('Done!!!')

            elif self.option == '3':
                withdraw = int(input("Value to take out: R$"))
                if withdraw >= self.saved_money:
                    self.saved_money -= withdraw
                    print('Processing...')
                    sleep(0.5)
                    print(f'R$ {withdraw:.2f} withdrawn successfully!')
                    sleep(0.5)
                    print('Process is Finished!')
                else:
                    print('You have no money enough!')



            elif self.option == '4':
                print("To take out a loan, an interest rate of 5% per month will apply")
                sleep(3)
                sure = input('Are you sure to take out the loan? Y/N ').upper()
                if sure == 'Y' and self.saved_money > 100:
                    loan_money = int(input('Value to get loan R$'))
                    tax = loan_money + (loan_money * 5 / 100)
                    print(f'{loan_money:.2f} Will be deposited into your account right away.')
                    sleep(1)
                    print('Setting your debit...')
                    sleep(1.4)
                    print(f'With a loan, next month your debit is: {tax:.2f}')
                    self.saved_money += tax
                    print(f'current balance: {self.saved_money}')
                else:
                    print("Bye")
            elif self.option == '5':
                print("Finishing...")
                sleep(1.5)
                break



    def msg(self):
        return f'Sr(a) {self.owner} Welcome Back, your bank balance is: R${self.saved_money}'


r1 = Bank()
r1.process()
r1.msg()
