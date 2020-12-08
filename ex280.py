import random
class Account:
    # class variable
    account_count = 0
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
		
        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1
		
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count
    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)
    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)
    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)
    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)
k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()
k.withdraw(100)
k.withdraw(200)
k.withdraw_history()

# 먼저 withdraw_history, deposit_history 를 정의한다.
# 이때 비어있는 withdraw, deposit 리스트를 만든다.
# 예금을 할때마다 self.deposit_log.append(amount)로 리스트로 얼마 저장했는지 알 수 있게 하고
# 출금을 할때마다 self.withdraw_log.append(amount)로 얼마 출금했는지 리스트로 알 수 있게 한다.
# 입금내역은 for문을 이용하여 변수 amount를 사용한다.
# 출금내역도 입금내역과 똑같이 만든다.
# 그리고 나서 Account함수를 이용하여 Kim이라는 사람이 1000원을 넣고 deposit(100),deposit(200),deposit(300)하여 각각 100,200,300원을 넣은 것을 history함수로 알 수 있다.
# 똑같이 history함수로 출금내역도 알 수 있다.
# 최정적으로 Kim 이라는 사람은 1000+100+200+300-100-200으로 총 1300원이 있을 것이다.