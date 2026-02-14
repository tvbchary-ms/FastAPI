# FastAPI testing -- Simple Product Management App

A simple full-stack CRUD application for managing products.

## 🚀 Tech Stack

-   Backend: FastAPI
-   Database: PostgreSQL
-   ORM: SQLAlchemy
-   Frontend: React (Vite)
-   HTTP Client: Axios

------------------------------------------------------------------------

## ✨ Features

-   Create products
-   View all products
-   Update existing products
-   Delete products
-   RESTful API design
-   Proper HTTP status handling

------------------------------------------------------------------------

## 📡 API Endpoints

  Method   Endpoint           Description
  -------- ------------------ ---------------------------------------
  - GET      `/products`        Get all products
  - POST     `/product`         Create a product
  - PUT      `/products/{id}`   Update a product
  - DELETE   `/products/{id}`   Delete a product
  - DELETE   `/reset`           Delete all products and reset DB
  - POST     `/build`           Create sample products if DB is empty

------------------------------------------------------------------------

## 🖥 Backend Setup

``` bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
uvicorn main:app --reload
```

Runs at: http://localhost:8000\
Docs: http://localhost:8000/docs

------------------------------------------------------------------------

## 🎨 Frontend Setup

``` bash
npm install
npm run dev
```

Runs at: http://localhost:5173

------------------------------------------------------------------------

## 📌 Future Improvement Scope

-   Search functionality
-   Pagination
-   Authentication
-   Docker support

------------------------------------------------------------------------

⭐ If you like this project, give it a star!
