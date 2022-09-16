from core.models import Restaurant, Food


restaurant_data = [
    {
        "name": "Gaurav's Kitchen",
        "address": "plot no, Ground Floor, Pradirgha complex, 22, Swami Vivekanand Marg, near Neel hospital, Sector-1, New Panvel East, Panvel, Navi Mumbai, Maharashtra 410206",
        "phone_number": 9049277948,
        "description": "Spacious Hotel with Mexican and Asian food.",
    },
    {
        "name": "Atherv's Snacks Corner",
        "address": "plot no, Ground Floor, Pradirgha complex, 22, Swami Vivekanand Marg, near Neel hospital, Sector-1, New Panvel East, Panvel, Navi Mumbai, Maharashtra 410206",
        "phone_number": 8983914599,
        "description": "A place to grab a quick bite, Burgers and Pizza's are our assets",
    },
    {
        "name": "Indiana Chinese",
        "address": "plot no, Ground Floor, Pradirgha complex, 22, Swami Vivekanand Marg, near Neel hospital, Sector-1, New Panvel East, Panvel, Navi Mumbai, Maharashtra 410206",
        "phone_number": 2565555555,
        "description": "Tghe name represents our food options. Hygienic and delicious chinese foods",
    },
    {
        "name": "The Pizza Point",
        "address": "plot no, Ground Floor, Pradirgha complex, 22, Swami Vivekanand Marg, near Neel hospital, Sector-1, New Panvel East, Panvel, Navi Mumbai, Maharashtra 410206",
        "phone_number": 9049090926,
        "description": "Grab variety of pizza's with appetizers",
    },
    {
        "name": "Asian Darbar",
        "address": "plot no, Ground Floor, Pradirgha complex, 22, Swami Vivekanand Marg, near Neel hospital, Sector-1, New Panvel East, Panvel, Navi Mumbai, Maharashtra 410206",
        "phone_number": 8795956459,
        "description": "",
    },
]


def create_restaurant_data():
    """Creates restaurant data in Food model"""
    for item in restaurant_data:
        restaurant = Restaurant.objects.filter(name=item["name"]).first()
        if restaurant:
            restaurant.name = item.get("name")
            restaurant.address = item.get("address")
            restaurant.phone_number = item.get("phone_number")
            restaurant.description = item.get("description")
            restaurant.save()
            continue
        restaurant_item = Restaurant.objects.create(**item)
        restaurant_item.save()
    return None
