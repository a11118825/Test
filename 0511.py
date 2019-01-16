# class Bank():
#     count=0
#     def __init__(self,name): 
#         self.name=name
#         self.balance=100  
#         Bank.count+=1
#         #print(self.name,self.b)
#     def withdraw(self,flow):
#         self.balance-=flow
#         if flow<self.balance:
#             print("您提了",flow,"元,","餘額NT$",self.balance,"元")
#             return ""
#         else:
#             print("您的存款不足")                                                                                                     
#             return ""
#     def deposit(self,flow):
#         self.balance+=flow
#         print("您存了NT$",flow,"總額為NT$",self.balance)
#         return ""

    
# account1=Bank("Jack")
# account2=Bank("Carol")
# print("Hello",account1.name,",您的開戶金額是NT$",account1.balance)

# print(account1.withdraw(40))
# print(account1.deposit(1000))

# print(Bank.count)


# class Circle():
#     def __init__(self):    
#         pass 
    
#     def long(self,r):
#         return r*2*3.14 

# a=Circle()
# print(a.long(3))

# import numpy as np
# a=np.array([2,4,8,9])
# b=np.array([1,3,5,7])
# print(a)
# print(a+b)
# print(b>2)


def x(array):
    return sorted(array)[0]

a=x([8,5,9,6,3])
print(a)