""""
Description: A script that contain simple data type, mathematic operations 
and collection types of python.
Author: Komaljit Kaur
Date: 2024-09-21
"""
import os
user_command = "echo"
os.system(user_command)

#SIMPLE DATA TYPES

first_name = "Komaljit"

admin_password = "Password123!"

# using f-string
print(f"value: {first_name}  type: {type(first_name)}")

# does Komaljit has a valid Manitoba Driver's License(bool)
komaljit_has_a_valid_manitoba_driver_license = False

# using f-string
print(f"value: {komaljit_has_a_valid_manitoba_driver_license}  type: {type(komaljit_has_a_valid_manitoba_driver_license)}")

current_year = 2024

# using f-string
print(f"this year: {current_year}  type: {type(current_year)}")

# increase the value to current year by 1
next_year = current_year + 1

# using f-string
print(f"next year: {next_year}  type: {type(next_year)}")

#CALCULATIONS

# GST and PST have constant values
GST = 0.05
PST = 0.07

# purchase price of a vehicle
vehicle_purchase_price = 80000.98

# tax calculation on vehicle
federal_tax =  vehicle_purchase_price * GST

provincial_tax = vehicle_purchase_price * PST

# total cost of vehicle including tax
final_cost = vehicle_purchase_price + federal_tax + provincial_tax

# using f-string
print(f"Pre-tax value: {vehicle_purchase_price}  Provincial Tax: {provincial_tax}  Federal Tax: {federal_tax}  Total: {final_cost}")

# using f-string to getting output upto two decimal places
print(f"Pre-tax value: ${vehicle_purchase_price:,.2f}  Provincial Tax: ${provincial_tax:,.2f}  Federal Tax: ${federal_tax:,.2f}  Total: ${final_cost:,.2f}")


#LISTS

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(type(numbers))
print(numbers)

# inserting first name between value of 5 and 6 in list
numbers.insert(5, "komaljit")
print(numbers)

# removing number 9 from list
numbers.remove(9)
print(numbers)

# second list
alphabets = ['A', 'B', 'C']

# third list
third_list = [numbers, alphabets]
print(third_list)


#TUPLES

# tuple contsin 4 Canadian Provinces
canadian_provinces = ('Manitoba', 'Ontario', 'Alberta', 'British Columbia')

print(type(canadian_provinces))
print(canadian_provinces)


#DICTIONARIES

# declearing variable that contain 3 different keys and their corresponding values. 
variables = {'nickle': 0.05,
             'dime': 0.1,
             'quarter': 0.15
             }

print(type(variables))
print(variables)

# modifying values of each key 
variables = { 'nickle': 5,
             'dime': 10,
             'quarter': 15
}

print(variables)

# adding two items in  existing dictionary
variables["Loonie"] = "100"
variables["Toonie"] = "200"

print(variables)


variables["Loonie"] = input("Enter Loonie value: ")
variables["Toonie"] = "200"

#SETS

# declaring a set containing all even numbers between 2 to 20
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

print(type(even_numbers))
print(even_numbers) 

# second set containing multiples of 5 between 5 to 20
multiples_of_five = {5, 10, 15, 20}

print(multiples_of_five)

# third set that contain unique values of previous both sets
third_set = even_numbers.union(multiples_of_five)

print(third_set)

# fourth set that contain common values from initial two sets
fourth_set = even_numbers.intersection(multiples_of_five)

print(fourth_set)

# fifth set that contain all values of even_numbers set but not those in multiples_of_five set
fifth_set = even_numbers.difference(multiples_of_five)

print(fifth_set)

# sixth set that contain all values of multiple_of_five set but not in even_numbers set
sixth_set = multiples_of_five.difference(even_numbers)

print(sixth_set)