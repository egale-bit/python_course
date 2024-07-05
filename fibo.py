#!/usr/bin/env python3

# fibnacci series

num = int(input("Enter the number: "))

counter = 0
n1, n2 = 0, 1

while counter < num:
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    counter += 1

