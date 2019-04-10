# -*- coding: utf-8 -*- 
 


import random
i = random.randrange(1, 100)
print(i)
while True:
    x = input("请输入一个1-100之间的整数： ")
    if x.isnumeric() == True:
        x = int(x)
        if x<100:
            if guess_number(x):
                break
            else:
                continue
        else:
            print("格式错误，请重新输入")
    else:
        print("格式错误，请重新输入")


def guess_number(x):
    if x < i:
        print("猜小了，再试试")
    elif x > i:
        print("猜大了，再试试")
    else:
        print("恭喜你，猜对了")
        return  True

