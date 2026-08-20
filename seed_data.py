import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cravex.settings')
django.setup()

from django.contrib.auth.models import User
from menu.models import Category, FoodItem
from accounts.models import UserProfile
from PIL import Image, ImageDraw, ImageFont

def create_food_image(filename, text, bg_color1, bg_color2):
    media_dir = os.path.join(os.path.dirname(__file__), 'media', 'food_images')
    os.makedirs(media_dir, exist_ok=True)
    filepath = os.path.join(media_dir, filename)

    img = Image.new('RGB', (800, 600), color=bg_color1)
    draw = ImageDraw.Draw(img)

    # Draw luxury gradient stripes
    for i in range(600):
        r = int(bg_color1[0] + (bg_color2[0] - bg_color1[0]) * (i / 600))
        g = int(bg_color1[1] + (bg_color2[1] - bg_color1[1]) * (i / 600))
        b = int(bg_color1[2] + (bg_color2[2] - bg_color1[2]) * (i / 600))
        draw.line([(0, i), (800, i)], fill=(r, g, b))

    # Add dark vignette glass box
    draw.rectangle([(80, 180), (720, 420)], fill=(10, 11, 14, 200), outline=(229, 9, 20), width=3)

    # Draw Brand Title & Food Name text
    draw.text((400, 230), "CRAVEX EXCLUSIVE", fill=(255, 183, 3), anchor="mm", font_size=28)
    draw.text((400, 310), text, fill=(255, 255, 255), anchor="mm", font_size=42)
    draw.text((400, 370), "★ PREMIUM TASTE ★", fill=(229, 9, 20), anchor="mm", font_size=22)

    img.save(filepath)
    return f'food_images/{filename}'

def run_seed():
    print("Seeding CraveX Database...")

    # 1. Admin Superuser
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser('admin', 'admin@cravex.com', 'admin123')
        print("Created Superuser: admin / admin123")
    
    # 2. Demo User
    if not User.objects.filter(username='crave_lover').exists():
        demo_user = User.objects.create_user('crave_lover', 'user@cravex.com', 'password123')
        demo_user.first_name = "Alex"
        demo_user.last_name = "Morgan"
        demo_user.save()
        
        profile, _ = UserProfile.objects.get_or_create(user=demo_user)
        profile.phone_number = "+1 (555) 789-4561"
        profile.address = "742 Evergreen Terrace, Luxury District, NY 10001"
        profile.save()
        print("Created Demo User: crave_lover / password123")

    # 3. Categories
    categories_data = [
        {'name': 'Chicken Specials', 'slug': 'chicken-specials'},
        {'name': 'Burgers', 'slug': 'burgers'},
        {'name': 'Pizza', 'slug': 'pizza'},
        {'name': 'Sides', 'slug': 'sides'},
        {'name': 'Drinks', 'slug': 'drinks'},
        {'name': 'Desserts', 'slug': 'desserts'},
    ]

    cat_map = {}
    for cat_data in categories_data:
        cat, _ = Category.objects.get_or_create(name=cat_data['name'], defaults={'slug': cat_data['slug']})
        cat_map[cat.name] = cat

    # 4. Premium Food Items
    items_data = [
        {
            'category': cat_map['Chicken Specials'],
            'name': 'Crispy Chicken Bucket',
            'description': '12 pieces of secret-recipe golden fried crispy chicken served with signature garlic dip and honey mustard.',
            'ingredients': 'Farm-Fresh Chicken, 11 Secret Spices, Buttermilk Batter, Garlic Dip',
            'price': 599.00,
            'rating': 4.9,
            'image': create_food_image('bucket.jpg', 'Crispy Chicken Bucket', (180, 20, 30), (40, 5, 10)),
            'is_featured': True
        },
        {
            'category': cat_map['Chicken Specials'],
            'name': 'Glazed Wings Deluxe',
            'description': '10 jumbo tender chicken wings tossed in smoked honey BBQ glazed sauce with sesame seeds.',
            'ingredients': 'Jumbo Wings, Honey BBQ Glaze, Roasted Sesame, Celery Sticks',
            'price': 349.00,
            'rating': 4.8,
            'image': create_food_image('wings.jpg', 'Glazed Wings Deluxe', (160, 40, 20), (30, 10, 5)),
            'is_featured': True
        },
        {
            'category': cat_map['Chicken Specials'],
            'name': 'Spicy Crunch Tenders',
            'description': '8 hand-breaded spicy chicken tenders fried to golden perfection with chipotle mayo.',
            'ingredients': 'Chicken Breast Tenders, Cayenne Pepper Batter, Chipotle Sauce',
            'price': 299.00,
            'rating': 4.7,
            'image': create_food_image('tenders.jpg', 'Spicy Crunch Tenders', (200, 50, 10), (50, 10, 5)),
            'is_featured': False
        },
        {
            'category': cat_map['Burgers'],
            'name': 'Spicy Chicken Burger',
            'description': 'Extra crispy zesty chicken breast patty, melted cheddar cheese, jalapenos, and spicy mayo on a toasted brioche bun.',
            'ingredients': 'Crispy Chicken Filet, Aged Cheddar, Jalapeño Slices, Brioche Bun, Spicy Mayo',
            'price': 249.00,
            'rating': 4.9,
            'image': create_food_image('spicy_burger.jpg', 'Spicy Chicken Burger', (140, 30, 20), (30, 5, 5)),
            'is_featured': True
        },
        {
            'category': cat_map['Burgers'],
            'name': 'Double Smash Cheese Burger',
            'description': 'Two 100% Angus beef patties smashed with caramelized onions, double Swiss cheese, and secret house sauce.',
            'ingredients': 'Angus Beef Patties, Swiss Cheese, Caramelized Onions, CraveX Secret Sauce',
            'price': 299.00,
            'rating': 4.8,
            'image': create_food_image('smash_burger.jpg', 'Double Smash Burger', (120, 40, 10), (20, 5, 5)),
            'is_featured': True
        },
        {
            'category': cat_map['Pizza'],
            'name': 'Chicken Cheese Pizza',
            'description': 'Hand-tossed sourdough pizza crust topped with rich tomato herb sauce, grilled chicken cubes, mozzarella, and gouda cheese.',
            'ingredients': 'Artisanal Dough, Roasted Chicken, Fresh Mozzarella, Smoked Gouda, Basil',
            'price': 499.00,
            'rating': 4.9,
            'image': create_food_image('chicken_pizza.jpg', 'Chicken Cheese Pizza', (170, 60, 20), (40, 10, 5)),
            'is_featured': True
        },
        {
            'category': cat_map['Pizza'],
            'name': 'Truffle & Chicken Pizza',
            'description': 'Luxury white sauce pizza infused with black truffle oil, rosemary chicken, wild mushrooms, and parmesan.',
            'ingredients': 'Black Truffle Oil, Creamy Alfredo Base, Rosemary Chicken, Mushrooms, Parmesan',
            'price': 599.00,
            'rating': 5.0,
            'image': create_food_image('truffle_pizza.jpg', 'Truffle Chicken Pizza', (90, 40, 80), (20, 10, 20)),
            'is_featured': False
        },
        {
            'category': cat_map['Sides'],
            'name': 'Loaded Fries',
            'description': 'Crispy golden crinkle fries smothered in warm cheese sauce, crispy bacon bits, chopped green onions, and ranch.',
            'ingredients': 'Golden Crinkle Cut Fries, Liquid Cheddar, Bacon Bits, Chives, House Ranch',
            'price': 179.00,
            'rating': 4.7,
            'image': create_food_image('loaded_fries.jpg', 'Loaded Fries', (180, 120, 20), (40, 25, 5)),
            'is_featured': True
        },
        {
            'category': cat_map['Sides'],
            'name': 'Garlic Butter Breadsticks',
            'description': '6 warm garlic butter glazed sourdough breadsticks sprinkled with parmesan and parsley.',
            'ingredients': 'Sourdough Sticks, Fresh Garlic Butter, Aged Parmesan, Chopped Parsley',
            'price': 149.00,
            'rating': 4.6,
            'image': create_food_image('breadsticks.jpg', 'Garlic Breadsticks', (150, 100, 30), (30, 20, 5)),
            'is_featured': False
        },
        {
            'category': cat_map['Desserts'],
            'name': 'Chocolate Brownie',
            'description': 'Rich Belgian dark chocolate fudgy brownie served warm with a drizzle of salted caramel.',
            'ingredients': 'Belgian Dark Chocolate, Dutch Cocoa, Sea Salt, Caramel Drizzle',
            'price': 129.00,
            'rating': 4.9,
            'image': create_food_image('brownie.jpg', 'Chocolate Brownie', (60, 25, 15), (15, 5, 5)),
            'is_featured': False
        },
        {
            'category': cat_map['Desserts'],
            'name': 'Molten Lava Cake',
            'description': 'Decadent chocolate cake with a warm flowing chocolate lava center.',
            'ingredients': 'Valrhona Chocolate, Eggs, Butter, Powdered Sugar Drizzle',
            'price': 159.00,
            'rating': 4.9,
            'image': create_food_image('lava_cake.jpg', 'Molten Lava Cake', (80, 20, 20), (20, 5, 5)),
            'is_featured': False
        },
        {
            'category': cat_map['Drinks'],
            'name': 'Premium Cold Coffee',
            'description': 'Double shot Arabica espresso blended with cold whole milk, vanilla bean syrup, and ice.',
            'ingredients': 'Arabica Espresso, Cold Milk, Madagascar Vanilla Bean Syrup',
            'price': 119.00,
            'rating': 4.8,
            'image': create_food_image('cold_coffee.jpg', 'Premium Cold Coffee', (90, 60, 40), (20, 15, 10)),
            'is_featured': False
        },
        {
            'category': cat_map['Drinks'],
            'name': 'Sparkling Berry Mocktail',
            'description': 'Refreshing sparkling water infused with wild blackberry puree, mint leaves, and lime juice.',
            'ingredients': 'Sparkling Mineral Water, Blackberry Puree, Fresh Mint, Lime Juice',
            'price': 139.00,
            'rating': 4.7,
            'image': create_food_image('mocktail.jpg', 'Sparkling Berry Mocktail', (160, 30, 80), (30, 5, 15)),
            'is_featured': False
        },
    ]

    for item in items_data:
        FoodItem.objects.update_or_create(
            name=item['name'],
            defaults=item
        )
        print(f"Seeded Food Item: {item['name']}")

    print("Seeding Complete Successfully!")

if __name__ == '__main__':
    run_seed()
