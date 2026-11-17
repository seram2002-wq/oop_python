#딕셔너리를 리턴하는 함수를 선언
def create_student(name,korean,math,english,science):
    return {
        "name":name,
        "korean": korean,
        "math": math,
        "english":english,
        "science":science
    }
students = [
    create_student("김유미",80,90,95,70),
    create_student("이서진",80,90,95,70),
    create_student("나형석",80,90,95,70),
    create_student("유재석",80,90,95,70),
    create_student("서유미",80,90,95,70),
   ]

# 학생명단(성적표) 출력하세요
print("이름","총점","평균",sep="\t")
for  student  in students:
     # 점수의 총합과 평균을 구하세요.
              score_sum = student["korean"]+student["english"]+student["math"]+student["science"]
              score_avg = score_sum/ 4
     # 출력
              print(student["name"], score_sum, score_avg,sep="\t")