students = {
    1:{"name": "Nikki", "marks": 20},
    2:{"name": "swetha", "marks": 21},
    3:{"name": "Harsha", "marks":50},
    4:{"name": "keerthi", "marks":19},
    5:{"name": "minty", "marks": 23},
}
for student_id, details in students.items():
    print(f"Student ID: {student_id}, Name:{details['name']}, Marks: {details['marks']}")