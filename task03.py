def calculate_tax(salary: int) -> dict:
    """
    Calculate tax based on progressive tax brackets.
    
    Tax brackets:
    - 0 - 5,000,000: 0%
    - 5,000,001 - 10,000,000: 12%
    - 10,000,001 - 20,000,000: 18%
    - 20,000,001+: 25%
    
    Args:
        salary: Gross salary amount
        
    Returns:
        Dictionary with gross, tax, net, and rate
    """
    tax = 0
    rate = "0%"
    
    if salary <= 5_000_000:
        tax = 0
        rate = "0%"
    elif salary <= 10_000_000:
        tax = (salary - 5_000_000) * 0.12
        rate = "12%"
    elif salary <= 20_000_000:
        tax = (5_000_000 * 0.12) + (salary - 10_000_000) * 0.18
        rate = "18%"
    else:  # salary > 20_000_000
        tax = (5_000_000 * 0.12) + (10_000_000 * 0.18) + (salary - 20_000_000) * 0.25
        rate = "25%"
    
    net = salary - int(tax)
    
    return {
        "gross": salary,
        "tax": int(tax),
        "net": net,
        "rate": rate
    }


# Test cases
if __name__ == "__main__":
    # Test 1
    result1 = calculate_tax(8_000_000)
    print(result1)  # {"gross": 8000000, "tax": 360000, "net": 7640000, "rate": "12%"}
    
    # Test 2
    result2 = calculate_tax(3_000_000)
    print(result2)  # {"gross": 3000000, "tax": 0, "net": 3000000, "rate": "0%"}
