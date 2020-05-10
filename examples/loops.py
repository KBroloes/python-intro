# Prints all the numbers from 0 to (excluding) 5
for i in range(5):
    print(i)


# Prints all the ages
age_list = [82, 42, 30, 67, 32]
for age in age_list:
    print(age)

# Prints keys and values of our list
for index, age in enumerate(age_list):
    print(index, age)

# List comprehension, returns all ages +1 in a new list
older_age_list = [age+1 for age in age_list]
print(older_age_list)


# Print all the names and ages in our name:age dictionary
ages = { "Bob": 82, "Alice": 42, "Eve": 30}
for name, age in ages.items():
    print(f"{name}: {age}")