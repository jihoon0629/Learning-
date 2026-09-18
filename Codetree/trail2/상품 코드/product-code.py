product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class product():
    def __init__(self, name = 'codetree', code = 50):
        self.name = name
        self.code = code

product1 = product()
product2 = product(product_name, product_code)

print("""product {0} is {1}
product {2} is {3}""".format(product1.code, product1.name, product2.code, product2.name))