s = 'hello'
# isalnum() will return True if all characters
# in S are alphanumeric
print(f'isalnum:{s.isalnum()}')  # True
# isalpha() wil return True if all characters
# in S are alphabetic
print(f'isalpha:{s.isalpha()}')  # True
# islower() will return True if all cased characters
# in S are lowercase and there is at least one cased
# character in S, False otherwise.
print(f'islower:{s.islower()}')  # True
# isspace() will return True if all characters
# in S are whitespace.
print(f'isspace:{s.isspace()}')  # False
# istitle() will return True if S is
# a title cased string and there is at least one
# character in S, i.e. uppercase characters may only
# follow uncased characters and lowercase characters
# only cased ones. Return False otherwise.
print(f'istitle:{s.istitle()}')  # False
# isupper() will return True if all cased characters
# in S are uppercase and there is at least one cased
# character in S, False otherwise.
print(f'isupper:{s.isupper()}')  # False
# method is endswith() which is essentially
# the same as a boolean check on s[-1]
print(f'endswith o:{s.endswith("o")}')  # False