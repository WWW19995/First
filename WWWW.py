import random
secret = random.randint(1,20)
print('-------wcwcwc--------')
temp = input("猜猜答案吧：")
guess = int(temp)
while guess != secret:
    temp = input("哎呀，猜错啦，请重新猜吧：")
    guess = int(temp)
    if guess == secret:
        print("恭喜猜对了哦！")
        print("不过没有奖励哦！")
    else:
        if guess > secret:
            print("猜错啦，大了哦！")
        else:
            print("猜错啦，小了哦！")
print("游戏结束了！")
