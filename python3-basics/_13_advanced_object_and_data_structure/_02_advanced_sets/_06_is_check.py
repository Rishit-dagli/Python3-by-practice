s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

# isdisjoin
# This method will return True if two sets
# have a null intersection.
print(f's1.isdisjoint(s2):{s1.isdisjoint(s2)}')  # False
print(f's1.isdisjoint(s3):{s1.isdisjoint(s3)}')  # True
# issubset
# This method reports whether another set contains this set.
print(f's1.issubset(s2):{s1.issubset(s2)}')  # True
# issuperset
# This method will report whether this set contains another set.
print(f's2.issuperset(s1):{s2.issuperset(s1)}')  # True
