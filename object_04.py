class Student:
    def __init__(self, name, korean, english, math, science):
        self.name=name
        self.korean=korean
        self.english=english
        self.math=math
        self.science=science

students=[
    Student("동균", 90, 85, 78, 92),
    Student("준수", 75, 88, 95, 80),
    Student("세람", 100, 77, 100, 100),
    Student("민재", 82, 70, 90, 86),
    Student("현준", 95, 80, 72, 88),
]

# 확인용 출력
for student in students:
    print(student.name, student.korean, student.english, student.math, student.science)
