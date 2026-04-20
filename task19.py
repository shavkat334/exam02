def find_longest_name(names: list) -> str:
    if not names:
        return ""
    
    longest_name = max(names, key=len)
    return longest_name

if __name__ == "__main__":
    print(find_longest_name(["Ali", "Diyor", "Jasurbek", "Muhammad"]))  # Jasurbek
    print(find_longest_name(["Bo", "Ali", "Zara"]))  # Zara
