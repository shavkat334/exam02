def sort_numbers(numbers: list, reverse: bool = False) -> list:

    return sorted(numbers, reverse=reverse)


# Test cases
if __name__ == "__main__":
    print(sort_numbers([3, 7, 10, -5, -8, 15, 22, 0]))  # [-8, -5, 0, 3, 7, 10, 15, 22]
    print(sort_numbers([3, 7, 10, -5], reverse=True))    # [10, 7, 3, -5]
