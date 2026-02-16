from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from models import ProductCreate
from database import session, engine
import db_models
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
import time

app = FastAPI(root_path="/api")

@app.on_event("startup")
def startup():
    for i in range(10):
        try:
            db_models.Base.metadata.create_all(bind=engine)
            print("Tables created successfully")
            break
        except OperationalError:
            print("Database not ready, retrying...")
            time.sleep(3)


# app.add_middleware(
#     CORSMiddleware,
#     allow_origin_regex=r"http://(localhost|192\.168\.\d+\.\d+:5173)",
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



db_models.Base.metadata.create_all(bind=engine)

products = [
 ProductCreate(id=1, name="phone", description="budget phone", price=99.5, quantity=10),
 ProductCreate(id=2, name="laptop", description="gaming laptop", price=999, quantity=6),
 ProductCreate(id=3, name="Pen", description="blue pen", price=1.99, quantity=902),
 ProductCreate(id=4, name="table", description="office table", price=199.9, quantity=65)
]


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return "Welcome to CRUD APP"

@app.post("/build")
def init_db():
    db=session()
    count = db.query(db_models.Product).count()
    if count ==0:
        for product in products:
            db.add(db_models.Product(**product.model_dump())) # ** is for unpacking, model_dump() to give dictionary
        db.commit()
        return "Build Completed!"
    raise HTTPException(status_code=409, detail="No need to build again!")


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(db_models.Product)\
                    .order_by(db_models.Product.id.asc())\
                    .all() 
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int,db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()

    if db_product != None:
        return db_product
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = db_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return "product added successfully"

@app.put("/products/{id}")
def update_product(id: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()

    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")       
    else:
        for key,value in product.model_dump().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return db_product

@app.delete("/products/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int,  db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()

    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")       
    else:
        db.delete(db_product)
        db.commit()


@app.delete("/reset")
def reset_table(db: Session = Depends(get_db)):
    db.execute(text("TRUNCATE TABLE product RESTART IDENTITY CASCADE"))
    db.commit()
    return {"message": "Table truncated and ID reset"}