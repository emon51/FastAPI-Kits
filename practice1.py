from fastapi import FastAPI
from models import Product

'''
# models.py: 
from pydantic import BaseModel 

class Product(BaseModel):
    id: int 
    name: str
    price: float 
    quantity: int 
'''

app = FastAPI()

@app.get("/")
def home():
    return  'Hello FastAPI' #{"message": "Hello FastAPI"} -> return something as a dictionary is the best practice.

@app.get("/address/")
def adresses():
    return  'Dhaka, Bangladesh' 


products = [
    Product(id=101, name='laptop', price=40000, quantity=1), 
    Product(id=102, name='PC', price=60000, quantity=1),
] 

# Fetch all products
@app.get('/products/')
def get_products():
    return products 

# Insert product
@app.post('/add-product/')
def add_product(product: Product):
    products.append(product)
    return 'Added product successfully to the Database'


# Update product 
@app.put("/update-product/")
def update_product(product: Product):
    for p in products:
        if p.id == product.id:
            p.name = product.name
            p.price = product.price
            p.quantity = product.quantity
            return 'Product updated successfully'
    return 'Product not found' 

# Update product by id 
@app.put("/update-product/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for p in products:
        if p.id == product_id:
            p.name = updated_product.name
            p.price = updated_product.price
            p.quantity = updated_product.quantity
            return 'Updated product successfully'
    return "Product not found"


# DELETE product by id
@app.delete("/delete-product/{product_id}")
def delete_product(product_id: int):
    for i, p in enumerate(products):
        if p.id == product_id:
            products.pop(i)
            return 'Deleted product successfully'
    return "Product not found"







