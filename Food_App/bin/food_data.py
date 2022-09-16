from core.helpers.constants import FoodCategoryTypes, FoodSubCategoryTypes
from core.models import Food

food_data = [
    {
        "name": "Maharaja Mac",
        "category": FoodCategoryTypes.HAMBURGER,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 149.00,
    },
    {
        "name": "Crunchy Chicken Burger",
        "category": FoodCategoryTypes.HAMBURGER,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 179.00,
    },
    {
        "name": "McEgg",
        "category": FoodCategoryTypes.HAMBURGER,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 129.00,
    },
    {
        "name": "Veg Supreme Burger",
        "category": FoodCategoryTypes.HAMBURGER,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 119.00,
    },
    {
        "name": "Chicken Clear Soup",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 70.00,
    },
    {
        "name": "Veg Clear Soup",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 50.00,
    },
    {
        "name": "Chicken Fried Rice",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 100.00,
    },
    {
        "name": "Fried Rice",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 90.00,
    },
    {
        "name": "Chicken Manchurian Rice",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 120.00,
    },
    {
        "name": "Chicken Triple Rice",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 130.00,
    },
    {
        "name": "Chicken Crispy",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 100.00,
    },
    {
        "name": "Paneer Crispy",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 80.00,
    },
    {
        "name": "Chicken Hakka Noodles",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 120.00,
    },
    {
        "name": "Veg Hakka Noodles",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 100.00,
    },
    {
        "name": "Chicken Schezwan Noodles",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 130.00,
    },
    {
        "name": "Schezwan Noodles",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 110.00,
    },
    {
        "name": "Chicken Manchurian",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 100.00,
    },
    {
        "name": "Veg Manchurian",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 90.00,
    },
    {
        "name": "Chicken Lolipop",
        "category": FoodCategoryTypes.CHINESE,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 150.00,
    },
    {
        "name": "Supreme Pizza",
        "category": FoodCategoryTypes.ITALIAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 300.00,
    },
    {
        "name": "Indi-Chicken Tandoori Pizza",
        "category": FoodCategoryTypes.ITALIAN,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 400.00,
    },
    {
        "name": "Margarita Pizza",
        "category": FoodCategoryTypes.ITALIAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 350.00,
    },
    {
        "name": "Chicken Peri-Peri Pizza",
        "category": FoodCategoryTypes.ITALIAN,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 450.00,
    },
    {
        "name": "Chicken Dominator",
        "category": FoodCategoryTypes.ITALIAN,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 470.00,
    },
    {
        "name": "Mexican green wave",
        "category": FoodCategoryTypes.ITALIAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 370.00,
        "description": "A pizza loaded with crunchy onions, crisp capsicum, juicy tomatoes and jalapeno with a liberal sprinkling of exotic Mexican herbs.",
    },
    {
        "name": "Extravaganza",
        "category": FoodCategoryTypes.ITALIAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 400.00,
        "description": "A pizza that decidedly staggers under an overload of golden corn, exotic black olives, crunchy onions, crisp capsicum, succulent mushrooms, juicyfresh tomatoes and jalapeno - with extra cheese to go all around.",
    },
    {
        "name": "Chicken Dum Biryani",
        "category": FoodCategoryTypes.ASIAN,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 200.00,
    },
    {
        "name": "Mutton Dum Biryani",
        "category": FoodCategoryTypes.ASIAN,
        "sub_category": FoodSubCategoryTypes.NON_VEG,
        "price": 250.00,
    },
    {
        "name": "Ramen",
        "category": FoodCategoryTypes.ASIAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 150.00,
    },
    {
        "name": "Dal Khichdi",
        "category": FoodCategoryTypes.ASIAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 100.00,
    },
    {
        "name": "Paneer Kolhapuri",
        "category": FoodCategoryTypes.ASIAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 100.00,
    },
    {
        "name": "Paneer Tikka Masala",
        "category": FoodCategoryTypes.ASIAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 120.00,
    },
    {
        "name": "Veg Pulao",
        "category": FoodCategoryTypes.ASIAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 100.00,
    },
    {
        "name": "Paneer Pulao",
        "category": FoodCategoryTypes.ASIAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 170.00,
    },
    {
        "name": "Nachos",
        "category": FoodCategoryTypes.MEXICAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 120.00,
    },
    {
        "name": "Nachos with Cheese",
        "category": FoodCategoryTypes.MEXICAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 150.00,
    },
    {
        "name": "Burritos",
        "category": FoodCategoryTypes.MEXICAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 180.00,
    },
    {
        "name": "Quesadilla",
        "category": FoodCategoryTypes.MEXICAN,
        "sub_category": FoodSubCategoryTypes.VEG,
        "price": 250.00,
    },
]


def create_food_data():
    """Creates food data in Food model"""
    for item in food_data:
        food = Food.objects.filter(name=item["name"]).first()
        if food:
            food.name = item.get("name")
            food.category = item.get("category")
            food.sub_category = item.get("sub_category")
            food.price = item.get("price")
            food.description = item.get("description")
            food.save() 
            continue
        food_item = Food.objects.create(**item)
        food_item.save()
    return None
