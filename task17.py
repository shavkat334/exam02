def filter_positive(numbers: list) -> list:
    return [item for item in numbers if item['value'] > 0]



if __name__ == "__main__":
    # Test 1
    result1 = filter_positive([{'value': -5}, {'value': 10}, {'value': -3}, {'value': 7}])
    print(result1)  # [{'value': 10}, {'value': 7}]
    
    # Test 2
    result2 = filter_positive([{'value': 0}, {'value': 5}, {'value': -3}])
    print(result2)  # [{'value': 5}]
