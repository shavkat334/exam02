def calculate_stats(numbers: list) -> dict:

    if not numbers:
        return {"sum": 0, "average": 0}
    
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    
    return {
        "sum": total_sum,
        "average": round(average, 2)
    }
if __name__ == "__main__":

    result1 = calculate_stats([3, 7, 10, -5, -8, 15, 22])
    print(result1) 

    result2 = calculate_stats([10, 0, 50])
    print(result2)
