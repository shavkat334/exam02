def atm_operation(balance: int, action: str, amount: int) -> int:
    if amount < 0:
        return "Error: Manfiy summa kiritish mumkin emas"
    
    if action == "deposit":
        balance += amount
    elif action == "withdraw":
        if amount > balance:
            return "Error: Balansda mablag' yetarli emas"
        balance -= amount
    else:
        return "Error: Noto'g'ri amal"
        
    return balance

# Test case-lar:
print(atm_operation(100000, "deposit", 50000))
print(atm_operation(100000, "withdraw", 30000))
print(atm_operation(50000, "withdraw", 60000))
print(atm_operation(100000, "deposit", -5000))
