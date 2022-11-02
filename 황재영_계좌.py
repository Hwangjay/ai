import os
import random


class Account:
    balance = 0
    name = ""
    accountCount = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.depositCount = 0

        num1 = str(random.randint(100, 999))
        num2 = str(random.randint(10, 99))
        num3 = str(random.randint(100000, 999999))
        Account.accountNumber = str(num1) + "-" + str(num2) + "-" + str(num3)

        f = open(f"C:/sample/{self.name}.txt", "w")
        f.write(f"{self.name} {Account.accountNumber} {self.balance}\n")
        f = open(f"C:/sample/{self.name}.txt", "r")
        f.close()


    def getaccountNum(self):
        print(f"-은행에 개설된 계좌계수 : {Account.accountCount}")

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            f = open(f"C:/sample/{self.name}.txt", "a")
            f.write(f"{self.name} {Account.accountNumber} {self.balance}\n")
            f.close()

            if self.depositCount % 3 == 0:  #3회 될때마다
                self.balance= self.balance*1.01
                f = open(f"C:/sample/{self.name}.txt", "a")
                f.write(f"{self.name} {Account.accountNumber} {self.balance}\n")
                f.close()



    def withdraw(self, amount):
        # print("출금하다")
        if self.balance > amount:
            self.balance -= amount
            f = open(f"C:/sample/{self.name}.txt", "a")
            f.write(f"{self.name} {Account.accountNumber} {self.balance}\n")
            f.close()

    def display_info(self):
        print(f"- 이름 :{self.name}")
        print(f"- 잔고 :{self.balance}")
        print(f"- 계좌번호 :{Account.accountNumber}")
        f = open(f"C:/sample/{self.name}.txt", "a")
        f.write(f"{self.name} {Account.accountNumber} {self.balance}\n")
        f = open(f"C:/sample/{self.name}.txt", "r")
        f.close()

    def __del__(self):
        os.remove(f"C:/sample/{self.name}.txt")
        print(f"{self.name} 계좌 통장이 폐기 되었습니다.")


h = Account("황재영",50000)
h.deposit(10000)
h.deposit(10000)
h.deposit(10000)
h.display_info()
l = Account("이순신",350000)
l.deposit(10000)
l.withdraw(10000)
l.display_info()
p = Account("박효신",480000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.withdraw(10000)
p.display_info()

print()
print("------------")
print(" 50만원 이상 고객 정보 :")

list = []
list.append(h)
list.append(l)
list.append(p)

for anyone in list:
    if anyone.balance >= 500000:
        anyone.display_info()