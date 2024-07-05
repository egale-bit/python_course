#!/usr/bin/env python3

num = int(input("Enter the number: "))

for i in range(1, 11):
    print("{0} x {1} = {2}".format( num, i, num*i))
