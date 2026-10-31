PRODUCTS = {
    "ethiopian-yirgacheffe": {
        "name": "Ethiopian Yirgacheffe Single-Origin",
        "origin": "Yirgacheffe region, Ethiopia",
        "flavor_profile": "Bright citrus, floral aroma, light body",
        "price": 18.99,
        "certifications": ["Fair Trade", "Organic"]
    },
    "house-blend": {
        "name": "GlobalJava House Blend",
        "origin": "Colombia and Brazil blend",
        "flavor_profile": "Balanced, chocolatey, nutty",
        "price": 12.99,
        "certifications": []
    },
    "geisha-reserve": {
        "name": "Limited Edition Geisha Reserve",
        "origin": "Hacienda La Esmeralda, Panama",
        "flavor_profile": "Jasmine, bergamot, white peach",
        "price": 89.99,
        "certifications": ["Single Estate", "Competition Grade"]
    }
}
def get_product_info(product_id: str) -> dict:
    """Get detailed information about a GlobalJava Roasters product, including
    name, origin, flavor profile, price, and certifications.
    Valid product ids: 'ethiopian-yirgacheffe', 'house-blend', 'geisha-reserve'.
    """
    print("TOOL CALLED with:", product_id)
    if product_id not in PRODUCTS:
        return {"error": f"Product {product_id} not found"}
    return PRODUCTS[product_id]

def calculate_total_price(product_ids: list[str]) -> dict:
    """Calculate the total price of the coffees a customer wants to buy.
    Pass the product ids, repeating an id once for each unit
    (for example 2 house blends = ['house-blend', 'house-blend']).
    Valid product ids: 'ethiopian-yirgacheffe', 'house-blend', 'geisha-reserve'.
    """
    print("TOOL CALLED with:", product_ids)
    total = 0
    for product_id in product_ids:
        if product_id not in PRODUCTS:
            return {"error": f"Product {product_id} not found"}
        total =total + PRODUCTS[product_id]["price"]
    return {"total": total}