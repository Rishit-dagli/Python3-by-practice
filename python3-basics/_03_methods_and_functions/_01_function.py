# systex with return
def hello(name):
    '''
    Document of function (optional)
    '''
    s = 'Hello,' + name
    return s

say = hello(' Jonh')
print(say)

help(hello)

# Find our if the word "dog" is in a string?
def dog_check(s):
    if 'dog' in s:
        return True
    else:
        return False

print(dog_check('My dog ran away.'))

def pig_latin(word):
    first_letter = word[0]
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:]+first_letter+'ay'
    return pig_word

print(pig_latin('apple'))

