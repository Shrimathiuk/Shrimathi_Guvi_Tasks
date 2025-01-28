def distribute_mangoes(mangoes, students):
    if students <= 0:
        return "Number of students must be greater than zero."

    mangoes_per_student = mangoes // students
    remaining_mangoes = mangoes % students

    distribution = [mangoes_per_student] * students

    for i in range(remaining_mangoes):
        distribution[i] += 1

    return distribution


# Example usage
mangoes = int(input("Enter the number of mangoes: "))
students = int(input("Enter the number of students: "))

result = distribute_mangoes(mangoes, students)
print("Mangoes distribution among students:", result)