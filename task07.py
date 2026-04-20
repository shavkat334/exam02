def calculate_cart(cart: dict) -> int:
    """
    Calculate total cost of shopping cart items.
    
    Args:
        cart: Dictionary where values are dictionaries with 'price' and 'quantity' keys
        
    Returns:
        Total cost (sum of price × quantity for all items)
    """
    total = 0
    for item in cart.values():
        total += item['price'] * item['quantity']
    
    return total


# Test cases
if __name__ == "__main__":
    # Test case from README
    cart = {
        'non': {'price': 1000, 'quantity': 2},
        'sut': {'price': 8000, 'quantity': 1},
        'olma': {'price': 5000, 'quantity': 5}
    }
    result = calculate_cart(cart)
    print(result)  # 37000
