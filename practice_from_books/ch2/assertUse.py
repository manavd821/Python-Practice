def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'] , ("price can't be lower than 0 or higher than price of product")
    return price

product = {
    'price' : 14900
}
# print(apply_discount(product, 5))

# string literal concatenation (#2.2 chapter) 
s = ('manav '
     'desai'
     ' bhai')
print(s)