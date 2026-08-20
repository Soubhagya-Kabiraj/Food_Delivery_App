<<<<<<< HEAD
# Food_Delivery_App
This is my second Django project of food delivery webapp.
=======
# CraveX - Premium Food Delivery Web Application

**CraveX** is a minimal, high-end food ordering platform inspired by luxury quick-service brands like KFC. Instead of overwhelming users with hundreds of options, CraveX offers a curated collection of costly, top-tier food items such as crispy chicken buckets, gourmet chicken burgers, artisanal chicken pizzas, glazed wings, loaded fries, molten lava cakes, and premium cold beverages.

---

## 🚀 Key Features

### 1. Authentication & Profile
- User Registration & Login / Logout
- Profile management with phone number and default delivery address
- View recent order history

### 2. Landing / Home Page
- High-impact hero section with dark luxury aesthetics
- Tagline: *"Premium Taste, Delivered Fast"*
- Hand-picked featured food collection
- Category quick links (Chicken Specials, Burgers, Pizza, Sides, Drinks, Desserts)

### 3. Menu & Food Details
- Exclusive 13+ signature items
- Category filter pills, search bar, and sorting (price low/high, rating)
- Food details page with key ingredients breakdown, rating badges, price, and quantity control

### 4. Cart & Checkout
- Add/remove items with quantity +/- adjustment
- Dynamic cart summary (subtotal, delivery fee, grand total)
- Real-time cart badge count in the navigation bar
- Express Checkout pre-filled with customer details

### 5. Live Order Tracking
- Order confirmation & order history tracking
- Interactive status progression bar (`Pending` → `Preparing` → `Out for Delivery` → `Delivered`)

### 6. Admin Panel
- Access Django Admin at `/admin/`
- Full control over Categories, FoodItems (images, ratings, availability, featured), Carts, Orders, and Order Items

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, Vanilla Custom CSS, Bootstrap 5, FontAwesome 6
- **Backend**: Python 3.x, Django 4.2 (MVT Architecture)
- **Database**: SQLite3
- **Image Processing**: Pillow

---

## 📂 Project Directory Structure

```text
Food Deliver App/
│
├── cravex/               # Django Core Settings & URLs
│   ├── settings.py
│   └── urls.py
│
├── accounts/             # Authentication & User Profiles
├── menu/                 # Categories & Food Catalog
├── cart/                 # Cart Management & Context Processors
├── orders/               # Orders & Live Tracking
│
├── templates/            # Django HTML Templates
│   ├── base.html
│   ├── accounts/
│   ├── menu/
│   ├── cart/
│   └── orders/
│
├── static/               # Custom CSS & JS Assets
│   ├── css/style.css
│   └── js/main.js
│
├── media/                # Uploaded/Seeded Food Images
│   └── food_images/
│
├── seed_data.py          # Data Seeding Script
├── manage.py
└── db.sqlite3
```

---

## ⚡ Quick Setup & Running Locally

### 1. Prerequisites
Ensure Python 3.9+ is installed.

### 2. Install Dependencies
```bash
pip install django pillow
```

### 3. Run Migrations & Seed Sample Data
```bash
python manage.py makemigrations
python manage.py migrate
python seed_data.py
```

### 4. Start Development Server
```bash
python manage.py runserver 8080
```

Open your browser and navigate to:
👉 **[http://127.0.0.1:8080/](http://127.0.0.1:8080/)**

---

## 🔑 Pre-Configured Accounts

- **Admin Account**:
  - Username: `admin`
  - Password: `admin123`
  - Admin Panel URL: `http://127.0.0.1:8080/admin/`

- **Demo Customer Account**:
  - Username: `crave_lover`
  - Password: `password123`
>>>>>>> 3c95a08 (Initial commit)
