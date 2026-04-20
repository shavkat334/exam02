def count_words(text: str) -> dict:
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count


# Test cases
if __name__ == "__main__":
    # Test 1
    result1 = count_words("salom salom dunyo")
    print(result1)  # {"salom": 2, "dunyo": 1}
    
    # Test 2
    result2 = count_words("Python python PYTHON")
    print(result2)  # {"python": 3}
