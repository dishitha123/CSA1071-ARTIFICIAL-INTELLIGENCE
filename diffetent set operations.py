set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
set_C = {4, 5, 6, 7}

# Union of sets A and B
union = set_A.union(set_B)
print("Union of sets A and B:", union)

# Intersection of sets A and B
intersection = set_A.intersection(set_B)
print("Intersection of sets A and B:", intersection)

# Difference of sets A and B
difference = set_A.difference(set_B)
print("Difference of sets A and B:", difference)

# Symmetric difference of sets B and C
symmetric_difference = set_B.symmetric_difference(set_C)
print("Symmetric difference of sets B and C:", symmetric_difference)

# Check if set A is a subset of set B
is_subset = set_A.issubset(set_B)
print("Is set A a subset of set B:", is_subset)

# Check if set C is a superset of set B
is_superset = set_C.issuperset(set_B)
print("Is set C a superset of set B:", is_superset)
