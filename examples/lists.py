# A list definition
age_list = [82, 42, 30, 67, 32]

# Get the first element
age_list[0]
# > 82

age_list.append(20) # age_list ow contains [82, 42, 30, 67, 32, 20]

# Slices
age_list[:2] # The first two elements
# > [82, 42]

age_list[-2:] # The last two elements
# > [32, 20]

age_list[:] # All elements
#> [82, 42, 30, 67, 32, 20]

age_list[1:3] # Second and third element (last value in the range is exclusive)
# > [42, 30]

# Sorting
sorted(age_list)
#> [20, 30, 32, 42, 67, 82]

# Alternative list syntax
list([82, 42, 30, 67, 32])