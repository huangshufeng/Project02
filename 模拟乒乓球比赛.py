import random
#比赛主逻辑类
class MainGame():
    def __init__(self):
        pass
    def startGame(self):
        print("比赛开始")
        Score().times()
    def overGame(self):
        print("比赛结束")
#分数类
class Score():
    def __init__(self):
        self.sum_a=0
        self.sum_b=0
        self.m=0
        self.n=0
    #得分的方法
    def getScore(self):
        while True:
            a = random.randint(0,1)
            b = random.randint(0,1)
            if a>b:
                self.m=a
                self.n=b
                print("恭喜A成员获得一分")
                print(a,b)
            elif a<b:
                self.m=a
                self.n=b
                print("恭喜B成员获得一分")
                print(a,b)
            elif a==b:
                print("比赛激烈的进行中···")
                self.getScore()
            break
    #计算总分的方法
    def allScore(self):
        self.sum_a=self.m+self.sum_a
        self.sum_b=self.n+self.sum_b
        #比较分数选出优胜者
    def max(self):
        print("运动员A的总分为", self.sum_a)
        print("运动员B的总分为", self.sum_b)
        if self.sum_a>self.sum_b:
            print("恭喜A成员赢得比赛")
        elif self.sum_a<self.sum_b:
            print("恭喜B成员赢得比赛")
        elif self.sum_a==self.sum_b:
            print("恭喜你们，这是平局")
    #比赛的回合
    def times(self):
        x=int(input("请输入比赛场数："))
        for i in range(1,x+1):
            print("这是第{}场比赛".format(i))
            self.getScore()
            self.allScore()
        self.max()
MainGame() .startGame()
MainGame().overGame()