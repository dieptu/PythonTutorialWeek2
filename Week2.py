import math

first_day = "Monday"
second_day = "Tuesday"
third_day = "Wednesday"
fourth_day = "Thursday"
fifth_day = "Friday"
sixth_day = "Saturday"
seventh_day = "Sunday"

#implicit continuation 
#first way with ,
first_string = "first day:", first_day, "second day:", second_day, "third day:", third_day
print(first_string)
print("first day:", first_day, "second day:", second_day, "third day:", third_day)

#second way with +
second_string = "first day: " + first_day + " second day: "+ second_day + " third day: " + third_day
print(second_string)
print("first day: " + first_day + 
        " second day: "+ second_day + 
        " third day: " + third_day)

#explicit continuation
third_string = "first day: " + first_day + \
                " second day: "+ second_day + " third day: " + third_day
print(third_string)

print("\n")
print("-"*15)
print("index in string")
print(first_day[0])
print(first_day[1])
print(first_day[-1])

print("\n")
print("-"*15)

user_input_name = input("Enter your name: ")
print(type(user_input_name))
user_input_age = input("Enter your age: ")
print(type(user_input_age))
user_age = int(user_input_age)
print(type(user_age))

print("\n")
print("-"*15)

print("Python", "is", "fun", sep="-")
print("first day:", first_day, "second day:", second_day, "third day:", third_day, sep="**")

print("\n")
print("-"*15)
print("arthmetic operation")
steps = 0
print("Steps: ",steps)
steps += 10 # steps = steps + 10
print("Steps: ",steps)
steps *= 2  # steps = steps * 2
print("Steps: ",steps)

print("\n")
print("-"*15)
print("common math functions")
some_value = 5
power_value = math.pow(some_value, 3)
print(some_value, "power of 3 = ", power_value)


some_value1 = 25
sqrt_value = math.sqrt(some_value1)
print(some_value1, "squart is = ", sqrt_value)

some_value2 = 23.33
ceil_value = math.ceil(some_value2)
print(some_value2, "ceil is = ", ceil_value)

some_value3 = 23.33
floor_value = math.floor(some_value3)
print(some_value3, "floor is = ", floor_value)


print("\n")
print("-"*15)
print("Addtion +")
number_1 = 9 + 6
print("Addtion of 9 and 6 is", number_1)

print("\n")
print("Subtraction -")
number_2 = 9 - 6
print("Subtraction of 9 and 6 is", number_2)

print("\n")
print("Multiplication *")
number_3 = 9 * 6
print("Multiplication of 9 and 6 is", number_3)

print("\n")
print("Exponentiation **")
number_4 = 9 ** 6
print("Exponentiation of 9 and 6 is", number_4)

print("\n")
print("Division /")
number_5 = 9 / 6
print("Division of 9 and 6 is", number_5)

print("\n")
print("Integer division //")
number_6 = 9 // 6
print("Integer division of 9 and 6 is", number_6)

print("\n")
print("Modulo %")
number_7 = 9 % 6
print("Modulo of 9 and 6 is", number_7)





