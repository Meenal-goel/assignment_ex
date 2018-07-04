#1. WAP to iterate over a list and store the cube into another list using lambda.

ini_list = []
upd_list = []
s = int(input("enter the list size:"))
print("enter the numbers:")
for i in range(s):
    var = int(input())
    ini_list.append(var)
print(ini_list)

for ele in ini_list:
    cube = (lambda x:x**3)
    upd_list.append(cube(ele))
print(upd_list)
print("*"*20)
print("\n")

#2.WAP to iterate over a list and store the cube  into another list using map

ini_list1 = []
upd_list1 = []
s1 = int(input("enter the list size:"))
print("enter the numbers:")
for i in range(s):
    var = int(input())
    ini_list1.append(var)
print(ini_list1)
upd_list1 = list(map(lambda x:x**3,ini_list1))
print(upd_list1)
print("*"*20)
print("\n")

#3.WAP to iterate over a list,add its element using reduce

import functools
ini_list2 = []
upd_list2 = []
s2 = int(input("enter the list size:"))
print("enter the numbers:")
for i in range(s2):
    var = int(input())
    ini_list2.append(var)
print(ini_list2)
upd_list2 =(functools.reduce(lambda x,y:x+y,ini_list2))
print(upd_list2)



    

    
