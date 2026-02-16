# FastAPI testing -- Simple Product Management App

A full-stack CRUD application for managing products — now upgraded to a production-style Docker and reverse proxy architecture.

------------------------------------------------------------------------

## 🚀 Tech Stack

-   Backend: FastAPI
-   Database: PostgreSQL
-   ORM: SQLAlchemy
-   Frontend: React (Vite)
-   HTTP Client: Axios
-   Reverse Proxy: Nginx
-   Containerization: Docker & Docker Compose

------------------------------------------------------------------------

## 🏗 Architecture (Production-Style)

Browser
↓
Nginx (Port 80)
├── / → Frontend (React)
└── /api → FastAPI Backend
↓
PostgreSQL

-   Single public entry point
-   Same-origin architecture
-   No CORS required
-   Clean `/api` routing
-   Persistent database storage

------------------------------------------------------------------------

## ✨ Features

-   Create products
-   View all products
-   Update existing products
-   Delete products
-   Reset database
-   Seed sample data
-   RESTful API design
-   Proper HTTP status handling
-   Reverse proxy routing
-   Dockerized deployment

------------------------------------------------------------------------

## 📡 API Endpoints

  Method   Endpoint                Description
  -------- ----------------------- ---------------------------------------
  - GET      `/api/products`         Get all products
  - POST     `/api/product`          Create a product
  - PUT      `/api/products/{id}`    Update a product
  - DELETE   `/api/products/{id}`    Delete a product
  - DELETE   `/api/reset`            Delete all products and reset DB
  - POST     `/api/build`            Create sample products if DB is empty

------------------------------------------------------------------------

## 🐳 Docker Setup (Recommended)

#### Run the entire application stack:

```bash
docker compose up -d --build
```
- Application runs at: http://localhost
- Only Nginx (port 80) is publicly exposed.
- Backend and database run inside Docker network.

## 🖥 Backend Setup (Without Docker)
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
uvicorn main:app --reload
```

- Runs at: http://localhost:8000
- Docs : http://localhost/docs

## 🎨 Frontend Setup (Without Docker)
```bash
npm install
npm run dev
```
- runs at: http://localhost:5173

## 🛠 Production Improvements Implemented
- Dockerized frontend
- Dockerized FastAPI backend
- Persistent PostgreSQL volume
- Fixed Vite build-time environment variable issue
- Debugged and resolved CORS properly
- Implemented reverse proxy with Nginx
- Removed CORS completely using same-origin routing
- Clean /api path-based routing
- Single-entry production-style architecture

## 📌 Future Improvement Scope
- Search functionality
- Pagination
- JWT Authentication
- HTTPS support
- Rate limiting
- CI/CD pipeline
- VPS deployment

⭐ If you like this project, give it a star!