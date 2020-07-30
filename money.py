class Account:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.phone_number = phone_number
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
    from datetime import datetime
    

    def __init__(self, first_name, last_name, bank, phone_number,service_provider):
        self.first_name = first_name
        self.last_name = last_name
        self.bank = bank
        self.phone_number = phone_number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.pay_loan = 0
    
    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name)
        return name
    
    def deposit(self, amount):
               date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("The date and time is {}".format(date_time))
    time = now.strftime("%H:%M:%S")
    print("The time is {}".format(time)) month = now.strftime("%m")
    print("The month is {}".format(month))year = now.strftime("%Y")
    print("The year is {}".format(year))
     
          

        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")
        else:
            self.balance += amount
            self.deposits.append(amount)
            print("You have deposited {} to {}".format(amount, self.account_name()))
        
        
        
        
            
            
    def withdraw(self, amount):date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            print("The date and time is {}".format(date_time)) time = now.strftime("%H:%M:%S")
            print("The time is {}".format(time)) month = now.strftime("%m")
            print("The month is {}".format(month))year = now.strftime("%Y")
      print("The year is {}".format(year))


        withdraw = self.withdrawals.append(amount)
        if amount <= 0:
            print("You cannot withdraw zero or negative")
        elif amount > self.balance:
            print("You don't have enough balance to make the transition")
        else:
            self.balance -= amount
            print("You have withdrawn {} from {}".format(amount, self.account_name()))
        
    
    def get_balance(self):
          

        return "The balance for {} is {}".format(self.account_name(), self.balance)

    def deposit_statements(self):
        for deposit in self.deposits:
            print(deposit)

        
        

    def withdrawal_statements(self):
        for withdraw in self.withdrawals:
            print(withdraw)
        

    def pay_loan(self,amount):
        if amount <= 0:
            print("you cannot withdraw a negative value")
        else:
            self.loan = amount
            print("you have been given a loan of shillings {}".format(amount))   
    def repay_loan(self,amount):
        try:
            amount + 10:
        except TypeError:
            print("Enter amount in figures")
            return
        if amount<=0
        print("You can not repay with that amount")    
        elif self.loan == 0:
            print("you do not have an existing loan")
        elif amount > self.loan:
            print("your loan is {}, please enter a amount that is less or equal to your loan".format(self.loan))
        else:
            self.loan -= amount
            self.repay = self.loan - amount
            print("you have repaid your loan with this {}, your existing balance is {}".format(amount,self.loan))
    def deposit(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")
        else:
            self.balance += amount
            self.deposits.append(amount)
            print("You have deposited {} to {}".format(amount, self.account_name()))

   def request_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")
        else:
            self.loan = amount
            print("You have been given a loan of {}".format((amount))
    def loan_repayment_statement(self):
         for repayment in self.loan_repayments:
        time = repayment["time"]
        amount = repayment['amount']
        formatted_time= self.get_formatted_time(time)
        statement="You repaid {} on {}".format,formatted_time(time)
        print(statement)

class BankAccount(Account):
    def __init__(self, first_name, last_name, phone_number, bank):
        self.bank = bank
        super().__init__(first_name, last_name, phone_number)


class MobileMoneyAccount(Account):
    def __init__(self, first_name, last_name, phone_number, service_provider):
        self.service_provider = service_provider
        super().__init__(self, first_name, last_name, phone_number)
    def buy_airtime(self,amount):
        try:
            amount=1
        except TypeError:
            print("PLease enter the amount in figures")
            return
        if amount=self.balance
        print("You do not have enough balance.Your balance is {}".format(self.balance))
        else:
            self.balance-=amounttime= date.now()
            airtime={
                "time"=time,
                "airtime"=amount
                
            } 
            self.airtime.append(airtime)
            print("You have bought airtime worth {} on {}".format(amount,self.get_formatted_time(time)))
    def pay_bill(self,amount):
        try:
            amount+=1
            except TypeError:
            print("Please enter the amount in figures")
            return
        if amount=self.balance
        print("You do not have enough balance.Your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time= date.now()
            pay_bill={
                "time"=time,
                "paybill"=amount
                
            } 
            self.pay_bill.append(airtimepaybill)
            print("You have paid  {} on {}".format(amount,self.get_formatted_time(time)))
    def receive_money(self,amount):
        try:
            amount+=1
            except TypeError:
            print("Please enter the amount in figures")
            return
        if amount=self.balance
        print("You do not have enough balance.Your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time= date.now()
            receive_money={
                "time"=time,
                "receive_money"=amount
                
            }  
            self.receive_money.append(receive_money)
            print("You have received ksh {} from  on {}".format(amount,self.account_name,self.get_formatted_time(time)))     
        
    def send_money(self,amount):
        try:
            amount+=1
            except TypeError:
            print("Please enter the amount in figures")
            return
        if amount-=self.balance
        print("Your account balance has insufficient money to complete this transaction.Your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time= date.now()
            send_money={
                "time"=time,
                "send_money"=amount
                
            }  
            self.send_money.append(send_money)
            print("You have sent ksh {}  to {} on {}".format(amount,self.account_name,self.get_formatted_time(time))) 