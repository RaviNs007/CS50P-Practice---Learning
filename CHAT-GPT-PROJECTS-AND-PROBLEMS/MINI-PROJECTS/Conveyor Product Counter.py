products = []
product_list = []
product_id = ''
unique_products = []
duplicat_produts = []
while True:
    product_id = input("Enter Product ID: ")
    
    if product_id == "done":
        break
    
    if product_id not in products:
       product_list.append(product_id)
    
    products.append(product_id)
    
for product in product_list:
    count = 0
    for product_old in products:
        if product_old == product:
            count += 1
    if count > 1:
        duplicat_produts.append(product)
        
    elif count == 1:
        unique_products.append(product)
        
print(f""" 
Total Products = {len(products)})

duplicat Products = {duplicat_produts})

Unique Products = {unique_products})
""")


    