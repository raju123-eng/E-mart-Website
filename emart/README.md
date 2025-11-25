# EMART -- Multivendor E‑Commerce Website (Django)

## 📌 Project Overview

EMART is a dynamic **multivendor e‑commerce web application** built
using Django.\
It includes **Buyer, Seller, and Admin** modules and supports complete
e‑commerce workflows including product listing, shopping cart, checkout,
order management, reviews, and secure authentication.

------------------------------------------------------------------------

## ✨ Features

### 👤 Buyer Module

-   User registration & login\
-   Browse products by category\
-   Add to cart, update quantity, remove items\
-   Secure checkout\
-   Place orders & make payments\
-   Track order status\
-   Write reviews & ratings\
-   View past orders

### 🛒 Seller Module

-   Seller registration & login\
-   Add, update, delete products\
-   Manage stock\
-   View orders received\
-   Track sales and history\
-   Manage product reviews

### 🛠 Admin Module

-   Manage categories, buyers, sellers\
-   Approve/Reject seller accounts\
-   Monitor orders\
-   Generate reports\
-   Full dashboard

------------------------------------------------------------------------

## 🏗 Tech Stack

### Backend:

-   Python 3.x\
-   Django Framework\
-   SQLite / MySQL

### Frontend:

-   HTML5, CSS3\
-   Bootstrap / Tailwind\
-   JavaScript

### Additional:

-   Django ORM\
-   Django Templates\
-   Django Authentication System\
-   Media & Static file handling

------------------------------------------------------------------------

## 📂 Project Folder Structure

    EMART/
    │
    ├── emart/                  # Main Django project settings
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    │
    ├── buyer/                  # Buyer app
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── templates/
    │       └── buyer/
    │
    ├── seller/                 # Seller app
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── templates/
    │       └── seller/
    │
    ├── admin_panel/            # Admin app
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── templates/
    │       └── admin_panel/
    │
    ├── media/                  # Uploaded product images
    ├── static/                 # Static CSS/JS files
    └── README.md               # Project documentation

------------------------------------------------------------------------

## ⚙️ Installation Guide

### **1️⃣ Clone the Project**

    git clone https://github.com/yourusername/emart.git
    cd emart

### **2️⃣ Create a Virtual Environment**

    python -m venv venv
    venv/Scripts/activate   (Windows)

### **3️⃣ Install Dependencies**

    pip install -r requirements.txt

### **4️⃣ Run Migrations**

    python manage.py makemigrations
    python manage.py migrate

### **5️⃣ Create Superuser**

    python manage.py createsuperuser

### **6️⃣ Run Server**

    python manage.py runserver

------------------------------------------------------------------------

## 🔗 Important URLs

  Module            URL
  ----------------- ------------------
  Buyer Homepage    `/`
  Buyer Login       `/buyer/login/`
  Seller Login      `/seller/login/`
  Admin Login       `/admin/`
  Product Listing   `/products/`
  Cart              `/cart/`
  Checkout          `/checkout/`

------------------------------------------------------------------------

## 📸 Screenshots (Add your own)

-   Homepage\
-   Seller Dashboard\
-   Buyer Product View\
-   Cart Page\
-   Admin Dashboard

You can place screenshots inside:

    /static/screenshots/

------------------------------------------------------------------------

## 🧪 Testing

Run Django tests:

    python manage.py test

------------------------------------------------------------------------

## 📜 License

This project is licensed under **MIT License**.

------------------------------------------------------------------------

## 🤝 Contribution Guidelines

1.  Fork the repository\
2.  Create a new feature branch\
3.  Commit changes with proper messages\
4.  Submit a pull request

------------------------------------------------------------------------

## ✉️ Contact

If you need help integrating backend APIs, improving UI, or adding
payment gateway support---feel free to ask!

------------------------------------------------------------------------
# this project is uploaded to git youcan verify it by using github link given below

https://github.com/raju123-eng/EMART-Website
"# EMART-Website" 
