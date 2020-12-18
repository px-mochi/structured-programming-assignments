'''
Created on 7 Sep 2018

@author: User
'''

print("Enter two numbers. This algorithm will find the greatest common denominator.")
a = int(input())
b = int(input())
while not b == 0:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)
