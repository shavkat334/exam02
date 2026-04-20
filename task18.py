def square_values(numbers: list) -> list:
    """
    Square the 'value' in each dictionary in the list.
    
    Args:
        numbers: List of dictionaries containing 'value' key
        
    Returns:
        New list with squared values
    """
    return [{'value': item['value'] ** 2} for item in numbers]


# Test cases
if __name__ == "__main__":
    # Test 1
    result1 = square_values([{'value': 2}, {'value': 3}, {'value': 4}])
    print(result1)  # [{'value': 4}, {'value': 9}, {'value': 16}]
    
    # Test 2
    result2 = square_values([{'value': -2}, {'value': 5}])
    print(result2)  # [{'value': 4}, {'value': 25}]
