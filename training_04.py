
class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def get_employee_count(self):
        return sum(len(dept.employees) for dept in self.departments)

    def get_payroll(self):
        total = 0
        for dept in self.departments:
            total += dept.get_payroll()
        return total

    def print_report(self):
        print("=" * 70)
        print("부서", "인원", "급여 총액", "평균 경력", sep="\t")
        for department in self.departments:
            print(
                department.name,
                f"{len(department.employees)}명",
                f"{department.get_payroll():.0f}",
                f"{department.get_avg_career():.1f}년",
                sep="\t",
            )
        print("-" * 70)
        print(
            f"{self.name} 전체",
            f"{self.get_employee_count()}명",
            f"{self.get_payroll():.0f}",
            sep="\t",
        )
        print("=" * 70)

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_payroll(self):
        return sum(employee.salary.get_total() for employee in self.employees)

    def get_avg_career(self):
        if not self.employees:
            return 0
        return sum(employee.get_career() for employee in self.employees) / len(self.employees)

    def print_members(self):
        print(f"[{self.name}]")
        print("이름", "경력", "급여 총액", sep="\t")
        for employee in self.employees:
            print(
                employee.name,
                f"{employee.get_career()}년",
                f"{employee.salary.get_total():.0f}",
                sep="\t",
            )


#급여 계산만 담당
class Salary:
    def __init__(self,base_pay,bonus,overtime):
        self.base_pay = base_pay
        self.bonus = bonus
        self.overtime = overtime

    def get_total(self):
        pay = self.base_pay + self.bonus + self.overtime
        return pay

    def get_tax(self):
        tax = self.get_total() * 0.1
        return tax

    def get_net(self):
        net = self.get_total() - self.get_tax()
        return net

class WorkHistory:
    def __init__(self,company,position,start_year,end_year):
        self.company = company    #회사명
        self.position = position  #직급
        self.start_year = start_year  #입사연도
        self.end_year = end_year      #퇴사연도

    def get_years(self):
        return self.end_year - self.start_year

    def to_string(self):
        return "{}\t{}\t{}\t{}\t{}".format(
            self.company, self.position,self.start_year,
            self.end_year, self.get_years()
        )



# 사원정보 + Salary 객체를 속성으로 가진다. (has-a)
class Employee:
    def __init__(self,name,dept,salary):
        self.name = name
        self.dept = dept
        self.salary = salary     #1:1 Saraly
        self.histories = []     #WorkHistory 객체를 담을 리스트

    def add_history(self,history):
        self.histories.append(history)

    def to_string(self):
        return "{}\t{}\t{}\t{}\t{}\t{}".format(self.name,
                         self.dept,self.get_career(),
                         self.salary.get_total(),
                         self.salary.get_tax(),
                         self.salary.get_net()   )
    def get_career(self):
        total = 0
        for h in self.histories:
            total += h.get_years()
        return total


if __name__ == "__main__":
    company = Company("블루웨이브")
    departments = {
        name: Department(name)
        for name in ("개발팀", "인사팀", "영업팀", "마케팅팀")
    }
    for department in departments.values():
        company.add_department(department)

    employees = [
        Employee("김민수", "개발팀", Salary(300, 50, 20)),
        Employee("이지은", "인사팀", Salary(320, 40, 30)),
        Employee("박준호", "영업팀", Salary(280, 60, 10)),
        Employee("최서연", "개발팀", Salary(350, 30, 25)),
        Employee("한도윤", "마케팅팀", Salary(300, 70, 15)),
    ]
    for employee in employees:
        departments[employee.dept].add_employee(employee)

    employees[0].add_history(WorkHistory("넥슨", "사원", 2015, 2018))
    employees[0].add_history(WorkHistory("네오위즈", "대리", 2018, 2022))
    employees[1].add_history(WorkHistory("블루웨이브", "사원", 2018, 2022))
    employees[3].add_history(WorkHistory("데이터랩", "사원", 2012, 2016))
    employees[3].add_history(WorkHistory("클라우드원", "과장", 2016, 2020))
    employees[3].add_history(WorkHistory("넥스트AI", "차장", 2020, 2023))
    employees[4].add_history(WorkHistory("스타트업", "사원", 2021, 2024))

    company.print_report()

