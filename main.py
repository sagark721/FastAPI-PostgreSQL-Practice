
from models import Products
from fastapi import FastAPI,Depends
from database_config import session, engine
import database_models
from sqlalchemy.orm import Session


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


def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()



def init_db():
    db=session()

    count=db.query(database_models.Products).count()

    if count==0:
        for product in productList:
            db.add(database_models.Products(**product.model_dump()))
        db.commit()
init_db()


@app.get("/item")
def get_item(db: Session = Depends(get_db)):
    db_productList=db.query(database_models.Products).all()
    return db_productList


@app.get("/item/{id}")
def getProductById(id:int, db:Session = Depends(get_db)):
    db_product=db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if db_product:
        return db_product
    return "error: Product not found" 


@app.post("/item")
def addProduct(product:Products, db:Session = Depends(get_db)):
    db.add(database_models.Products(**product.model_dump()))
    db.commit()
    return product


@app.put("/item")
def updateTheProduct(id:int, product:Products, db:Session=Depends(get_db)):
    db_product=db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity

        db.commit()
        return "Product Updated Successfully"
    else:
        return "Product Not Found!"



@app.delete("/item")
def deleteProduct(id:int,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Products).filter(database_models.Products.id==id).first()

    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted Successfully!"
    else:
        return "Product Not Found!" 