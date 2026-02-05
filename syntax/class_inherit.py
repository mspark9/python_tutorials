# 클래스 기능 상속(확장)
class Person:
    def __init__(self, fname, lname):  
        # self는 객체 자신을 의미(default)
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

y = Person("John", "Doe")
y.printname()

class Student(Person):  # Person 클래스 상속 받음
    def __init__(self, fname, lname, year): 
        # super(): 부모 클래스의 생성자 호출 함수
        super().__init__(fname, lname)  # self를 제외한 부모 클래스의 생성자 호출
        self.graduationyear = year
    
    def printname(self):
        print(self.firstname, self.lastname, self.graduationyear)

x = Student("Jane", "Doe", 2026)
x.printname()
