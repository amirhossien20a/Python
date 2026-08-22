products = {
    "laptop": 5,
    "phone": 10,
    "mouse": 20,
    "keyboard": 8
}

print("Products are : ")
for i in products:
    print(i)

productName = input("Enter the product name : ")

if productName in products:
    print (f"we have {products.get(productName)} {productName}s")
else:
    print("Product not found")

