class Student:
    def __init__(self, name, korean, english, math, science):
        self.name=name
        self.korean=korean
        self.english=english
        self.math=math
        self.science=science

    # 학생 한명의 총점을 리턴하는 메서드
    def get_sum(self):
        score_sum=self.korean + self.english + self.math + self.science
        return score_sum

    # 학생 한명의 평균을 리턴하는 메서드
    def get_average(self):
        return self.get_sum() / 4

    # 학생 한명의 점수를 문자열로 리턴하는 메서드
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())


students=[
    Student("동균", 90, 85, 78, 92),
    Student("준수", 75, 88, 95, 80),
    Student("세람", 100, 77, 100, 100),
    Student("민재", 82, 70, 90, 86),
    Student("현준", 95, 80, 72, 88),
]

# 학생명단(성적표) 출력하세요
print("이름","총점","평균",sep="\t")
for student in students:
    print(student.to_string())
