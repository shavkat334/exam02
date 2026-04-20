def find_min_max(numbers: list) -> dict:

    if not numbers:
        return {"max": None, "min": None}
    
    return {
        "max": max(numbers),
        "min": min(numbers)
    }

if __name__ == "__main__":
    # Test 1
    result1 = find_min_max([3, 7, 10, -5, -8, 15, 22])
    print(result1)  # {"max": 22, "min": -8}

    result2 = find_min_max([100, 50, 200, -10])
    print(result2)

