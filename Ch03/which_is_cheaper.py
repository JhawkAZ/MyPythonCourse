product1_price = input("What is the price of product 1?")
print('the type is ', type(product1_price))
price1=float(product1_price)
print('Product 1 is an integer:',price1.is_integer())
weight1 = float(input("How many ounces is product 1?"))
price2 = float(input("what is the price of product 2 ?"))
weight2=float(input("How many ounces is product 2?"))
price_per_ounce1 = price1/weight1
price_per_ounce2= price2/weight2
print("Price per ounce of product 1: ")
print(price_per_ounce1)
print("Prince per ounce of product 2: ")
print(price_per_ounce2)
print("Is Product 1 Less than Product 2 " + str(price1<price2))

