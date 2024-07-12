# Online Pharmacy With Django
Welcome to the Online Pharmacy Shop! This repository contains the codebase for an online pharmacy website built using Django. Below is a brief overview of the structure and functionality of the website.
Description
This project implements a modern and user-friendly online pharmacy where customers can browse and purchase medicines conveniently from their homes. Here's a breakdown of its components:

Base HTML (base.html): Defines the basic structure of the website layout, including navigation, header, footer, and essential scripts.

Homepage (index.html): Displays a carousel of featured slides, highlights key features like free delivery and new arrivals, and showcases a selection of products.

Shop Page (shop.html): Lists all available products with options to filter by price range and sort by relevance, name, or price. Each product card provides details and links to individual product pages.

Product Details Page (shop_single.html): Displays detailed information about a specific product, including its image, name, price, and description. Customers can add the product to their cart directly from this page.

# Installation
# 1. Clone this repository:
```bash
git clone https://github.com/EmmaHarutyunyan/Online_Pharmacy_With_Django.git
```

2. **Create virtual environment and activate:**
```bash


python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. **Install packages:**
```bash
pip install -r requirements.txt
```

4. **Run the development server:**
```bash
python manage.py runserver
```

