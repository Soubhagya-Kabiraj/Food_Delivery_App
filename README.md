<img width="1676" height="912" alt="Screenshot 2026-08-03 121430" src="https://github.com/user-attachments/assets/4dc7825d-b558-44d7-9374-5840acf89ef0" />

---

# 🍔 CraveX — Premium Food Delivery Web Application

[![Django Version](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap Version](https://img.shields.io/badge/Bootstrap-5.3-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**CraveX** is a minimalist, luxury-themed food ordering platform inspired by high-end, premium quick-service dining. Unlike generic platforms cluttered with hundreds of average choices, CraveX focuses on a curated, exclusive selection of gourmet chicken buckets, artisanal pizzas, handcrafted burgers, premium mocktails, and decadent desserts.

Built with **Django (MVT Architecture)** and a modern **Dark-Luxury UI Design System**, CraveX delivers a premium, fast, and highly interactive user experience..

---

## 📸 User Interface Preview
*(To showcase your application, insert screenshots of your pages below)*

| 🏠 Home Dashboard | 🍕 Food Menu |
| --- | --- |
| <img width="1676" height="912" alt="Screenshot 2026-08-03 121430" src="https://github.com/user-attachments/assets/4dc7825d-b558-44d7-9374-5840acf89ef0" /> | <img width="1356" height="911" alt="Screenshot 2026-08-03 121542" src="https://github.com/user-attachments/assets/e67e158c-5692-4899-941f-8d30ab63fdba" /> |

| ⭐ Premium Featured Collection | 🍔 Food/Product Details |
| --- | --- |
| <img width="1350" height="912" alt="Screenshot 2026-08-03 121512" src="https://github.com/user-attachments/assets/ea8ae553-bbea-4beb-8cd5-c3c21813e3d8" /> | <img width="1850" height="907" alt="Screenshot 2026-08-03 121751" src="https://github.com/user-attachments/assets/9e244a2e-3701-4c42-9cc8-201885560335" /> |

| 🛒 Shopping Cart | 💳 Checkout Page |
| --- | --- |
| <img width="1837" height="916" alt="Screenshot 2026-08-03 121831" src="https://github.com/user-attachments/assets/b93ccc59-b379-47b6-8fae-4b634ffb58a3" /> | <img width="1577" height="907" alt="Screenshot 2026-08-03 121900" src="https://github.com/user-attachments/assets/857931e6-f09e-4749-af9e-63895813be87" /> |

| 📍 Live Order Tracking | 📝 Registration Page |
| --- | --- |
| <img width="1531" height="912" alt="Screenshot 2026-08-03 121936" src="https://github.com/user-attachments/assets/6d939c0e-9dc1-42cb-8fbb-f97fc2059ed1" /> | <img width="1902" height="912" alt="Screenshot 2026-08-03 120331" src="https://github.com/user-attachments/assets/c9326c5f-ad77-49e8-bd81-b80c0fe64ec2" /> |
---

## 🗺️ System Architecture & User Journey

The diagram below illustrates the customer lifecycle and application flow from login to real-time delivery status:

```mermaid
graph TD
    A[Unauthenticated Visitor] -->|Register/Login| B[CraveX Dashboard]
    B -->|Explore Categories| C[Curated Menu Catalog]
    C -->|Search/Filter/Sort| D[Food Details Page]
    D -->|Add Item & Quantity| E[Dynamic Shopping Cart]
    E -->|Express Checkout| F[Review Address & Confirm Order]
    F -->|Place Order| G[Live Tracking Dashboard]
    G -->|Order Lifecycle Status| H[Pending ➔ Preparing ➔ Out for Delivery ➔ Delivered]
```

---

## ✨ Core Features

### 🔒 1. Authentication & Custom User Profiles
* **Secure Auth:** Fully integrated Django registration, login, and session-based logout flows.
* **Smart User Profiles:** Automatic profile generation (`UserProfile`) on registration to store phone numbers and delivery addresses, minimizing steps during future checkouts.

### 🍽️ 2. High-Impact Curated Menu & Food Catalog
* **Premium Theme Aesthetics:** Rich dark UI featuring high-impact crimson red accents and elegant gold elements designed for Indian fine-dining context.
* **Advanced Catalog Tools:** Real-time search query matching, categories filtering (Chicken Specials, Pizza, Burgers, Sides, Drinks, Desserts), and sorting (by rating or price low-to-high/high-to-low).
* **Detailed Food Cards:** Complete view of premium ingredients, ratings, availability badges, and interactive quantity controllers.

### 🛒 3. Dynamic Cart & Shopping Ledger
* **Immediate Adjustments:** Real-time item additions and quantity management.
* **Auto-calculations:** Live subtotal, delivery charges, and final grand totals automatically calculated in the template.
* **Persisted Sessions:** Cart states are linked dynamically to user instances and remain active across sessions.

### 💳 4. Express One-Click Checkout
* **Pre-Filled Shipping Details:** Checkout inputs are auto-populated from the user's `UserProfile` for a seamless ordering process.
* **Consolidated Invoice:** Detailed list of all ordered items, individual item subtotals, and total billing before checking out.

### 📍 5. Live Order Tracking & Lifecycle Progression
* **Visual Status Tracker:** Interactive status indicator bar that updates dynamically (`Pending` ➔ `Preparing` ➔ `Out for Delivery` ➔ `Delivered`).
* **Order History Archive:** Customers can access past invoices, address files, phone logs, and order receipts in one central screen.

### ⚙️ 6. Admin Control Center
* **Superuser Panel:** Full database management at `/admin/` for Category creation, custom FoodItem creation (with ratings, image uploads, featured toggles), and real-time order status tracking updates.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
|---|---|---|
| **Backend Framework** | Django 4.2 | Robust, scalable Python MVC framework (MVT structure). |
| **Language** | Python 3.9+ | Clean, object-oriented backend programming. |
| **Database** | SQLite3 | Local Relational database used for development storage. |
| **UI Styling** | Custom CSS3 + Bootstrap 5 | Bespoke luxury dark theme styling, flex grids, and utility classes. |
| **Icons & Fonts** | FontAwesome 6 & Google Fonts |Outfit & Inter typography styles paired with vector icons. |
| **Image Processing**| Pillow | Server-side image manipulation and processing library. |
| **Data Generation** | PIL Draw Scripts | Custom canvas image seed scripts to generate luxury dish banners. |

---

## 📂 Project Directory Structure

```text
Food Deliver App/
│
├── cravex/               # Django Project Core Configuration
│   ├── __init__.py
│   ├── settings.py       # Global Settings (Installed Apps, Static, Media)
│   ├── urls.py           # Global Routing Patterns
│   └── wsgi.py / asgi.py
│
├── accounts/             # Authentication & User Profile Manager
│   ├── models.py         # UserProfile (Phone, Address, Sign-up signals)
│   ├── forms.py          # UserProfile update & registration forms
│   └── views.py          # Register, Login, Profile controllers
│
├── menu/                 # Product Catalog & Category Engine
│   ├── models.py         # Category and FoodItem Schema (Price, Rating, Ingredients)
│   ├── urls.py           # Menu path mappings
│   └── views.py          # Menu list, detailed food display & sorting
│
├── cart/                 # Cart Lifecycle Manager
│   ├── models.py         # Cart & CartItem records
│   ├── context_processors.py # Injects live cart counts into Navbar globally
│   └── views.py          # AJAX add/remove/update logic
│
├── orders/               # Orders & Live Tracking Dispatcher
│   ├── models.py         # Order, OrderItem & Tracking statuses
│   └── views.py          # Checkout, order creation, and live tracking UI
│
├── static/               # Central Static Assets
│   ├── css/
│   │   └── style.css     # Premium luxury Dark-Theme Design Tokens
│   └── js/
│       └── main.js       # UI interactions, alerts, dynamic count adjustments
│
├── templates/            # Django HTML Document Templates
│   ├── base.html         # Base Layout (Header, Footer, Dark Navigation)
│   ├── accounts/         # Login, Register, Profile templates
│   ├── menu/             # Home page, Menu list, Food details
│   ├── cart/             # Cart Summary layout
│   └── orders/           # Checkout form, order receipts, status tracker
│
├── media/                # User uploaded & seeded food images
│   └── food_images/      
│
├── seed_data.py          # Automated Database Seeding Script (Users, Items, Custom Canvas Graphics)
├── manage.py             # Django Manager CLI Utility
└── db.sqlite3            # SQLite database file
```

---

## ⚡ Quick Setup & Local Installation

### 1. Prerequisites
Make sure you have **Python 3.9+** and `pip` installed on your machine.

### 2. Clone the Repository & Open Workspace
```bash
git clone https://github.com/SoubhagYA-Kabiraj/Food_Delivery_App.git
cd Food_Delivery_App
```

### 3. Install Required Packages
Install Django and Pillow (required for database images handling):
```bash
pip install django pillow
```

### 4. Apply Database Migrations
Set up your database tables and models:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Seed Database & Generate Luxury Image Assets
CraveX includes an automated database seeder (`seed_data.py`). Running this script:
1. Registers the administrator credentials.
2. Registers a demo customer account.
3. Automatically sets up food categories.
4. Generates custom food graphics and uploads them to the media folder.
5. Populates 13 premium food items with ingredients, ratings, prices, and settings.

```bash
python seed_data.py
```

### 6. Run the Development Server
```bash
python manage.py runserver 8080
```
Open your browser and navigate to: 👉 **[http://127.0.0.1:8080/](http://127.0.0.1:8080/)**

---

## 🔑 Pre-Configured Test Credentials

For quick evaluation, use the credentials seeded from `seed_data.py`:

### 👑 System Administrator (Admin Dashboard)
* **Access URL:** `http://127.0.0.1:8080/admin/`
* **Username:** `admin`
* **Password:** `admin123`
* *(Provides full access to manage categories, modify prices, update orders status, and view active user profiles).*

### 👤 Demo Customer Account (Front-End Checkout)
* **Access URL:** `http://127.0.0.1:8080/accounts/login/`
* **Username:** `crave_lover`
* **Password:** `password123`
* *(Preloaded with a delivery address and phone number for testing checkout and live order progression tracking).*

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more details.

---
*Created with ❤️ by [Soubhagya Kabiraj](https://github.com/SoubhagYA-Kabiraj)*
