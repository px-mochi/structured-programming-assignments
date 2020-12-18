print("Enter two positive integer numbers. This algorithm will find the greatest common denominator.")
a = int(input())
b = int(input())
while a <= 0 or b <= 0:
    print("Please input a valid positive integer.")
    a = int(input())
    b = int(input())
counter = 0
while not b == 0 and not a == 0:
    if a > b:
        a = a % b
    else:
        b = b % a
    counter = counter + 1
print("Number of iterations: ", end='', flush=True)
print(counter)
if a > b:
    c = a
else:
    c = b
print(c)
