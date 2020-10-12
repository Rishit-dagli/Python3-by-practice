## Task
Given a dict containing products from a store, where keys are products, and values are prices:
```
products = {
    "tshirt": 50,
    "jeans": 30
}
```
Write a program that takes an input where the first lines are products to be added until a zero(0) is read. Subsequent lines will be keys of products that will be removed (if present) until another zero(0) is read, when the program must print all the products.

### Sample input
```
hat 10
shoes 40
painting 100
socks 5
0
painting
0
```
### Sample output
```
hat: $50
shoes: $40
socks: $5
```