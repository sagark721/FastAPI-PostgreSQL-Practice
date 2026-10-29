
from models import Products
from fastapi import FastAPI
from database_config import session, engine
import database_models
app=FastAPI()


database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Ganapati Bappa Moraya !!!"


productList=[
    Products(id=1,name= "Product 1",description="Description 100", price= 100.0, quantity=100),
    Products(id=2,name= "Product 2",description="Description 200", price= 200.0, quantity=200),
    Products(id=3,name= "Product 3",description="Description 300", price= 300.0, quantity=300),
    Products(id=4,name= "Product 4",description="Description 400", price= 400.0, quantity=400),
    Products(id=5,name= "Product 5",description="Description 500", price= 500.0, quantity=500), 
    Products(id=6,name= "Product 6",description="Description 600", price= 600.0, quantity=600),
    Products(id=7,name= "Product 7",description="Description 700", price= 700.0, quantity=700)
]


def init_db():
    db=session()

    count=db.query(database_models.Products).count()

    if count==0:
        for product in productList:
            db.add(database_models.Products(**product.model_dump()))
        db.commit()
init_db()


@app.get("/item")
def get_item():
    db=session()
    db.query()
    return productList


@app.get("/item/{id}")
def getProductById(id:int):
    for product in productList:
        if product.id == id:
            return product
    return {"error": "Product not found"} 


@app.post("/item")
def addProduct(product:Products):
    productList.append(product)
    return product


@app.put("/item")
def updateTheProduct(id:int, product:Products):
    for i in range(len(productList)):
        if productList[i].id==id:
            productList[i]=product
            return f"{product} \nAdded Successfully"

    return "Product Not Found!"



@app.delete("/item")
def deleteProduct(id:int):
    for i in range(len(productList)):
        if productList[i].id==id:
            del productList[i]
            return "Product Deleted Sucessfully"

    return "Product Not Found!" 