"""Problem Statement:
You're given a nested list of dictionaries, where each dictionary represents a student's
performance in multiple subjects across multiple semesters. Write a code that calculates the
total marks in all semesters only for those students who scored more than 80 in every
subject of every semester.
"""



students = [
    {
        'name': 'Amit',
        'semesters': [
            {'Math': 88, 'Science': 91, 'English': 85},
            {'Math': 90, 'Science': 92, 'English': 84}
        ]
    },
    {
        'name': 'Pooja',
        'semesters': [
            {'Math': 79, 'Science': 95, 'English': 88},
            {'Math': 82, 'Science': 81, 'English': 85}
        ]
    },
    {
        'name': 'Ravi',
        'semesters': [
            {'Math': 87, 'Science': 88, 'English': 89},
            {'Math': 91, 'Science': 90, 'English': 93}
        ]
    }
]

result = []

for student in students:
    if all(mark > 80 for sem in student['semesters'] for mark in sem.values()):
        total = sum(mark for sem in student['semesters'] for mark in sem.values())
        result.append({'name': student['name'], 'total_marks': total})

print(result)
