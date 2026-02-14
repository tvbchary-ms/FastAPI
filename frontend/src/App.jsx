import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";


const API = "http://localhost:8000";

function App() {
  const [deleteId, setDeleteId] = useState(null);
  const [products, setProducts] = useState([]);
  const [form, setForm] = useState({
    id: "",
    name: "",
    description: "",
    price: "",
    quantity: "",
  });
  const [editingId, setEditingId] = useState(null);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    const res = await axios.get(`${API}/products`);
    setProducts(res.data);
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleAdd = async () => {
    if (editingId) {
      await axios.put(`${API}/products/${editingId}`, form);
      setEditingId(null);
    } else {
      await axios.post(`${API}/products`, form);
    }

    setForm({
      id: "",
      name: "",
      description: "",
      price: "",
      quantity: "",
    });

    fetchProducts();
  };

  const handleEdit = (product) => {
    setForm(product);
    setEditingId(product.id);
  };

  const confirmDelete = async () => {
  await axios.delete(`${API}/products/${deleteId}`);
  setDeleteId(null);
  fetchProducts();
};


 const handleDelete = async (id) => {
 
  await axios.delete(`${API}/products/${id}`);
  fetchProducts();
};


  return (
    <div className="container">
      <h1>Simple React 18 CRUD App</h1>

      <div className="card">
        <h2>Add Product</h2>
        <div className="form-row">
          <input name="id" placeholder="ID" value={form.id} onChange={handleChange} />
          <input name="name" placeholder="Name" value={form.name} onChange={handleChange} />
          <input name="description" placeholder="Description" value={form.description} onChange={handleChange} />
          <input name="price" placeholder="Price" value={form.price} onChange={handleChange} />
          <input name="quantity" placeholder="Quantity" value={form.quantity} onChange={handleChange} />
          <button onClick={handleAdd}>
            {editingId ? "Update" : "Add"}
          </button>
        </div>
      </div>

      <div className="card">
        <h2>Products</h2>
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Description</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {products.map((p) => (
              <tr key={p.id}>
                <td>{p.id}</td>
                <td>{p.name}</td>
                <td>{p.description}</td>
                <td>${p.price}</td>
                <td>{p.quantity}</td>
                <td>
                  <button className="edit" onClick={() => handleEdit(p)}>
                    Edit
                  </button>
                  <button
                    onClick={() => setDeleteId(p.id)}
                    className="bg-red-500 text-white px-3 py-1 rounded delete"
                  >
                      Delete
                  </button>

                </td>
              </tr>
            ))}
          </tbody>
        </table>

        <h2>by TVB Chary For testing Fast API</h2>
        <h4>*** React - FastAPI - PostgreSQL ***</h4>
      </div>
      
      {deleteId && (
  <div className="modal-overlay">
    <div className="modal-box">
      <h2>Confirm Delete?</h2>
      <p>Are you sure you want to delete this product?</p>
      <div className="modal-actions">
        <button onClick={() => setDeleteId(null)}>Cancel</button>
        <button onClick={confirmDelete} className="delete">
          Delete
        </button>
      </div>
    </div>
  </div>
)}




    </div>
  );
}

export default App;
