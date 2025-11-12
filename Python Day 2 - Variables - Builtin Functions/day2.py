# Exercises: Level 1
"""
1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py(skip it!)
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line
"""

#2 Write a python comment saying 'Day 2: 30 Days of python programming'
# 'Day 2: 30 Days of python programming'

#3 Declare a first name variable and assign a value to it
first_name = 'Francis Leo'
print(first_name)

#4 Declare a last name variable and assign a value to it
last_name = 'Marcos'
print(last_name)

#5 Declare a full name variable and assign a value to it
full_name = f"{first_name} {last_name}"
print(full_name)

#6. Declare a country variable and assign a value to it
my_country = 'Atlantis'
print(my_country)

#7. Declare a city variable and assign a value to it
my_city = 'Biringan'
print(my_city)

#8. Declare an age variable and assign a value to it
my_age = 69
print(my_age)

#9. Declare an year variable and assign a value to it
my_age = 6969
print(my_age)

#10. Declare a variable is_married and assign a value to it
is_married = 'Ohoo!'
print(is_married)

#11. Declare a variable is_true and assign a value to it
is_true = True
print(is_true)

#12. Declare a variable is_light_on and assign a value to it
is_light_on = 'Yes'

#13. Declare multiple variable on one line
"""
Hindot ka! King ina mo!! ohhooo!!!
"""
# Exercises: Level 2

"""
1. Check the data type of all your variables using type() built-in function(skip)
2. Using the len() built-in function, find the length of your first name(skip)
3. Compare the length of your first name and your last name(skip)
4. Declare 5 as num_one and 4 as num_two
5. Add num_one and num_two and assign the value to a variable total
6. Subtract num_two from num_one and assign the value to a variable diff(skip)
7. Multiply num_two and num_one and assign the value to a variable product(skip)
8. Divide num_one by num_two and assign the value to a variable division(skip)
9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10. Calculate num_one to the power of num_two and assign the value to a variable exp(skip)
11. Find floor division of num_one by num_two and assign the value to a variable floor_division
12. The radius of a circle is 30 meters.-->@ the bottom #13-#15
13. Calculate the area of a circle and assign the value to a variable name of area_of_circle
14. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
15. Take radius as user input and calculate the area.
16. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
17. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""

#4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#5. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

#9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)

#11. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

#13 Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math
radius = 30 
pi = math.pi
area_of_circle = pi*(radius)**2 
print(f'{round(area_of_circle,2)} sq meter')


#14. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*pi*radius
print(f'{round(circum_of_circle,2)} meter')

#15. Take radius as user input and calculate the area.
radius = input("Enter radius value:")
area_of_circle = pi*(float(radius))**2 
print(f'{area_of_circle:.2f} sq meter')







