# -*- coding: utf-8 -*- 
 
import random
i=random.randrange(1,101)
print(i)
while True:
    x = input("请输入一个1-100之间的整数： ")
    if x.isnumeric()==True:
        x = int(x)
        guess_number(x)      
    else:
        print("格式错误，请重新输入")
    
        
def guess_number(x):
    if x<101:
        if x<i:
            print("猜小了，再试试")
        elif x > i:
            print("猜大了，再试试")
        else:
            print("恭喜你，猜对了")
            exit()           
    else:
        print("格式错误，请重新输入")
        

                                                   
