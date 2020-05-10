from .lists import age_list
from .dictionaries import ages

#Filter

# Get all values that are odd
is_odd = lambda age: age % 2 != 0

# Use lambda in filter function
new_list = list(filter(is_odd, age_list))
print(new_list)
# > [67]

# inline lambda
less_than_40 = list(filter(lambda age: age < 40, age_list))
print(less_than_40)
# > [30, 32, 20]

# Map

# Just return the ages (lambda receives a Tuple oject)
age_values = list(map(lambda item: item[1], ages.items()))
print(age_values)
# > [82, 42, 30, 32]

# Above is the same as
print(list(ages.values()))
# > [82, 42, 30, 32]

# or
age_values = [item[1] for item in ages.items()]
print(age_values)
# > [82, 42, 30, 32]


# Convert to string representation
pretty = list(map(lambda item: item[0] + str(item[1]), ages.items()))
print(pretty)
# > ['Bob82', 'Alice42', 'Eve30', 'Kevin32']

# above is equivalent to
pretty = [item[0] + str(item[1]) for item in ages.items()]
print(pretty)
# > ['Bob82', 'Alice42', 'Eve30', 'Kevin32']