## 函数的理解
- 函数是用来实现单一，或相关联功能的代码段。
- 定义完函数以后，可以调用，不段复用。
## break/return/exit/quit的区别的认知
-  break 是用来终止循环语句的，只能用于for/while 循环语句。
-  return 用于函数返回运算的结果，一般在python中会自动给默认，但是在写函数的时候记得要写上。
-  exit/quit是结束进程
##  加入break的函数
```
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
    ```