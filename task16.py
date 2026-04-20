def count_by_grade(grades: dict, target_grade: int) -> dict:
    # Ma'lum bahoga ega talabalar ismlari ro'yxati
    students_list = []
    
    for name, grade in grades.items():
        if grade == target_grade:
            students_list.append(name)
    
    # Natijani talab qilingan formatda qaytaramiz
    return {
        "count": len(students_list),
        "students": students_list
    }

# Test case-lar:
print(count_by_grade({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}, 5))
# Natija: {"count": 2, "students": ["Ali", "Husan"]}

print(count_by_grade({"Aziz": 4, "Bobur": 4, "Diyor": 3}, 4))
# Natija: {"count": 2, "students": ["Aziz", "Bobur"]}
