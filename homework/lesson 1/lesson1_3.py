#converting radius to circumference and area
#variable declaration
radius = int()
pi = 3.14

#input
radius = int(input("Please insert your radius: "))

#conversion rule
circumference = 2*pi*radius
"radius 1 = 6.28 circumference"
area = pi*radius*radius

#printing result
print("The circumference of the circle is: %0.2f units." %(circumference))
print("The area of the circle is: %0.2f units squared." %(area))

