#!/usr/bin/env python3
import math
#1
name = "Sivert Log"
age = 39
height = 5.11
favorite_color = "Red"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"My name is {name}, I'm {age:d} years old. My height is {height:.2f} and my favorite color is {favorite_color}")

print(f"""
Name: {name}
 Age: {age}
Height: {height}
Favorite Color: {favorite_color}
""")

r = 5
pi = math.pi
circle_area = pi*r**2
print(f"The area of a circle with a radius of 5 is {circle_area:.1f}")

#2
print("The square root of my age is", math.sqrt(age))

print(f"The sine of my height is {math.sin(height)}")
print(f"The cosine of my height {math.cos(height)}")

#3
print(f"""
The sum of age and 5 is {age+5}
The difference between height and 4 is {height-4:.2f}
The product of age and height is {age*height:.2f}
The quotient of height and 2 is {height/2}
The remainder of age divided by 3 is {age%3}
age raised to the power of 2 is {age**2}
""")

#4
fahr = float(input("Enter a temperature in fahrenheit:"))
celsius = (fahr - 32) * 5 / 9
print(f"That is {celsius:.1f}° celsius.")