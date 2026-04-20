def analyze_grades(students: dict) -> dict:

    if not students:
        return {"average": 0, "above_average": []}
    
    grades = list(students.values())
    average = sum(grades) / len(grades)
    above_average = [name for name, grade in students.items() if grade > average]
    
    return {
        "average": average,
        "above_average": above_average
    }
if __name__ == "__main__":
    result1 = analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3})
    print(result1)  # {"average": 4.25, "above_average": ["Ali", "Hasan"]}
    
    result2 = analyze_grades({"Aziz": 3, "Bobur": 4, "Diyor": 3})
    print(result2)  # {"average": 3.33..., "above_average": ["Bobur"]}
