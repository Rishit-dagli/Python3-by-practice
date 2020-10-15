from io import StringIO

# Arbitrary String
message = 'This is just a normal string.'

# Use StringIO method to set as file object
f = StringIO(message)

f.read()

f.write(' Second line written to file like object')

# Reset cursor just like you would a file
f.seek(0)

# Read again


print(f.read())