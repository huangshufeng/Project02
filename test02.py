#开始总人数
person = ["Alien","Luce","Jack","Bob","House"]
print("开始人数：",person)
del person[2]
print("走了Jack:",person)
a = person.pop(3)
print("删除了：",a)
person.remove("Alien")
print("又走了Alien:",person)
person.insert(0,"Min")
person.append("Jim")
print("新来了Min和Jim:",person)
for i in range(len(person)):
    print(person[i],end=" ")



