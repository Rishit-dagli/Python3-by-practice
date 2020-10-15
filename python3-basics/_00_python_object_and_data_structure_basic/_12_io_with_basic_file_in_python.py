
myfile = open('myfile.txt')
# myfile = open('my_wrong_file.txt') # this line will error no such file

# file_contents = myfile.read()
file_contents = myfile.readlines()
print(file_contents)

# alternative file read
# mode
# r is read only
# w is write only (will overwrite files or create new)
# a is append only (will add on to file)
# r+ is read and write
# w+ is write and read(overwrite existing file or create a new file)
with open('myfile.txt', mode='r') as my_new_file:
    new_contents = my_new_file.read()
print(new_contents)

with open('myfile.txt', mode='a') as my_new_file:
    my_new_file.write('\nline four')

with open('myfile.txt', mode='r') as my_new_file_added:
    all_contents = my_new_file_added.read()
print(all_contents)