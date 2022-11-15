#!/usr/bin/python
# -*- coding: utf-8 -*-

def isNotFloat(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return True
    try:
        float(element)
        return False
    except ValueError:
        return True
 
def multi(index, lists):
    product = 1
    i = 0
    for item in lists:
        if i != index:
            product *= float(item)
        i += 1
    return product

nums = []
res = []

print("Please input three or more float number. Press 'Enter' to end input")
while True:
    str = input()
    if str == "" and len(nums) >= 3:
        break
    elif str == "":
        print ("Please input more float number.  We need three or more float number")
    elif isNotFloat(str):
        print("It is not a float number.  Please input float number")
    else:
        nums.append(str)

n = len(nums)
print(nums)
# initial res to 1
for i in range(n):
    res.append(multi(i,nums))

print(res)