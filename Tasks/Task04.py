#Area of a circle
# Write a Python program to calculate the area of a circle given its radius using the
# formula ``` area=π×r^2``` ( Take pie as 3.14)
"""
import math

r=float(input("Enter the radius"))

#Area = 3.14 * (r**2) #OR
Area= math.pi * pow(r,2)

print(Area)
print(f"Area:{Area:.2f}")"""


#Oneline
import math
print("Area=", math.pi*(float(input("Enter radius")))**2)