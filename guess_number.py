# -*- coding: encoding -*-
 
import random
i=random.randrange(1,101)
print(i)
x = input("请输入一个1-100之间的整数： ")
def check_num(x):
    if  x<1:
        print("小于1了，请输入一个1-100之间的整数：")
    elif x>100:
        print("大于100了，请输入一个1-100之间的整数：")
    elif isinstance(x,int)==False:
        print("格式错误，请输入一个1-100之间的整数：")
    else:
        pass    
if x<i:
    print("猜小了，再试试")
elif x>i:
    print("猜大了，再试试")
else :
    print("恭喜你，猜对了")  