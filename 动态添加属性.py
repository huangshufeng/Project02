class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1=Person('小明',18)
p1.address = '北京'
setattr(p1,'gender','男')
print('姓名：%s 年龄：%d 地址：%s 性别:%s'%(p1.name,p1.age,p1.address,p1.gender))
print('姓名：%s 年龄：%d 地址：%s 性别:%s'%(p1.name,p1.age,p1.address,getattr(p1,'gender')))
#添加类属性
p2 = Person('小红',17)
Person.Classroom = 101
print(p1.Classroom)
print(p2.Classroom)




