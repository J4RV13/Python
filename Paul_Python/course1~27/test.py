# *Use the Python Interpreter* *choose the lines and command the "shift+enter"*
#--------------------- 11 Variables ---------------------
# 變數可以隨便變更型態
print("Running test.py")
x = 5
type(x)
x = 3.14159
type(x)

#--------------------- 12 String ---------------------
a = "hello"
a[0]
print(a)
a.upper()
b = a.upper()
print(b)
c = b.lower()
print(c)
d = c.capitalize()
print(d)

b = " kitty"
a+b
C = a + b
print(C)
d = c * 5
print(d)


a = '''this is a test
this is a test2
this is a test3
'''
print(a)

a = "Hello kitty"
a = 'Hello Kitty'
print(a)

a = "Hello\nkitty"
print(a)
a = "Hello\tkitty"
print(a)

#--------------------- 13 List ---------------------
a = ['a', 'b', 'c', 'd', 'e']
print(a)
type(a)
a[0]
len(a)
a[0:3]
a.append('f')
print(a)
a.append('z')
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.count('f')
a.count('z')
a.count('oo')

#--------------------- 13 Dictionary ---------------------
dict = {'Paul':90, 'Alice':80, 'Bob':'zero', 'key':'value'}
dict['Paul']
dict['Alice']
dict['joni']
dict.get('Paul')
dict['John'] = 100
print(dict)
dict.keys()
dict.values()
'Paul' in dict.keys()

for key in dict.keys():
  print(key)

for key in dict.keys():
  print(dict[key])

for key in dict.keys():
  print(key, dict[key])

#--------------------- 15 Boolean ---------------------
True and True
True and False
(1>0) and (2>0)
True or False
False or True
False or False
(1<0) or (2>0)
(1<0) or (2<0)
(1<0)
not (1>0)

#--------------------- 16 Structure ---------------------
# code block 基本上空格都是4格，":(分號)"代表C語言的"{}"
for i in range(10):
  if i < 5:
    print("less than 5")
  else:
    print("more than 5")

#--------------------- 17 if ---------------------
x = 10
if x <= 0:
    print("x <= 0")
elif x <= 5:
    print("0 < x <= 5")
elif x <= 10:
    print("5 < x <= 10")
else:
    print("x > 10")

#--------------------- 18 for loop ---------------------
for b in [1, 3, 5, 7]:
  print(b, end=" ")

# range(10) = 0~9的數字, end是最後的字串是空白，沒有指定就會是換行
for a in range(10):
  print(a, end=" ")
for a in range(10):
  print(a, end="b ")

#--------------------- 19 while  loop ---------------------
i = 0
while i < 10:
  print(i, end=" ")
  i = i + 1

#--------------------- 20 break/continue ---------------------
for n in range(20):
  if n % 2 == 1:
    break
  print(n, end=" ")

for n in range(20):
  if n % 2 == 1:
    continue # 1 3 5 7 9 11 13 15 17 19
  print(n, end=" ")

#--------------------- 23 套件 ---------------------
import os
help(os)
print(os.name)
import os as abc # 可以把套件名稱另外取名
abc.name

from os import name
print(name)  # name 直接變成os.name

from os import *  # 內顯引用方式，把os內的值都引用出來，官方不建議這樣用
print(path)
path = "Jack Hung"
print(path)

#--------------------- 24 第三方套件 ---------------------
#使用pip安裝第三方套件
#pip3 install requests

#--------------------- 25 引用自製模組 ---------------------
import package.subpackage.sum_module as sum_module
help(sum_module)
sum_module.sum_bm(1, 2)
sum_module.multiply_bm(3, 2)

#--------------------- 25 安排自製模組目錄配置 ---------------------
# 只要資料夾地下有"__init__.py"，就是告訴python這個目錄是套件
