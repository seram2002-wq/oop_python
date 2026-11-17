# 학생 리스트 (students)를 선언해 주세요. 5명의 학생정보를 아래 속성으로 저장하세요
# 학생은 이름(name),  (4과목 점수 데이터를 갖는다.)
# 국어(korean),영어(english),수학(math),과학(science)속성갖는다
# 학생의 성적관리 프로그램
students = [{
   "name":"김유미","korean":80,"english":90, "math":95,"science":70,},
   {"name":"이서진","korean":90,"english":80, "math":72,"science":100,},
   {"name":"나형석","korean":70,"english":66, "math":80,"science":90,},
   {"name":"유재석","korean":50,"english":70, "math":88,"science":88,},
   {"name":"최우식","korean":80,"english":85, "math":84,"science":84,}]

# 학생명단(성적표) 출력하세요
print("이름","총점","평균",sep="\t")
for  student  in students:
     # 점수의 총합과 평균을 구하세요.
              score_sum = student["korean"]+student["english"]+student["math"]+student["science"]
              score_avg = score_sum/ 4
     # 출력
              print(student["name"], score_sum, score_avg,sep="\t")