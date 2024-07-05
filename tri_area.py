#!/usr/bin/env python3

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

s = ( a + b + c ) / 2
area = ( s * (s - a) * ( s - b ) * ( s - c ) ) ** 0.5

print("The area of the triangle: %0.2f"%area)
