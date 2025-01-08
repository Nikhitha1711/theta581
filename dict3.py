products = [
    {"name":"laptop","price":1000},
    {"name":"Mobile","price":500},
    {"name":"Tablet","price":300}
]
affordable_products = [product for product in products if product["price"]<500]
print(affordable_products)