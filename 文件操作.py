# -*- coding:utf-8 -*-
f = open("班级数据.txt",'r',encoding='utf-8')
for i in f:
    i=i.split()

    age=int(i[1])
    heigh=int(i[3])
    #选出符合条件的成员
    if age>17 and heigh>170:
        print(i)
