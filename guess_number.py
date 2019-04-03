# -*- coding: utf-8 -*- 
 
import random
i=random.randrange(1,101)
while True:
    x = int(input("请输入一个1-100之间的整数： "))
    if x<i:
        print("猜小了，再试试")
    elif x>i:
        print("猜大了，再试试")
    else :
        print("恭喜你，猜对了") 
        break
    

def check_type(x):
    if x.isnumeric():
        return True
    else:
        return False

def check_num():
        if x < 1:
            print("小于1了，请输入一个1-100之间的整数：")
        elif x > 100:
                print("大于100了，请输入一个1-100之间的整数：")
        else:
            pass




    
