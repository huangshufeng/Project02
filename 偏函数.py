from functools import partial
str1 = '1010'
fun1 = partial(int,base=2)
print(fun1(str1))