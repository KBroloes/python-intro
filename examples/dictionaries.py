ages = { "Bob": 82, "Alice": 42, "Eve": 30}

# Get key
ages["Bob"]
# > 82

# Check key
"Kevin" in ages
# > False
"Alice" in ages
# > True

# Set key
ages["Kevin"] = 32

# Get values (and convert to list)
list(ages.values())
# > [82, 42, 30, 32]

# Get keys and convert to liste
list(ages.keys())
# > [‘Bob’, ‘Alice’, ‘Eve’, ‘Kevin’]