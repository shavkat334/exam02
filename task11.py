from collections import Counter

def analyze_list(items: list) -> dict:
    total = len(items)
    unique_items = set(items)
    unique = len(unique_items)
    counts = Counter(items)
    duplicates = [item for item, count in counts.items() if count > 1]
    most_common = counts.most_common(1)
    most_common_value = most_common[0][0] if most_common else None
    return {
        "total": total,
        "unique": unique,
        "duplicates": duplicates,
        "most_common": most_common_value,
    }

if __name__ == "__main__":
    result = analyze_list(["Ali", "Vali", "Ali", 1, 2, 1])
    print(result)
