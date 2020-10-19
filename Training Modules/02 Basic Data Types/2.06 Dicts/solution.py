products = {}

while True:
    add = input()
    if add == '0':
        break
    new_product = add.split(' ')
    products[new_product[0]] = int(new_product[1])

while True:
    remove = input()
    if remove == '0':
        break
    if remove in products:
        del products[remove]

for key in products:
    print("{}: ${}".format(key, products[key]))
