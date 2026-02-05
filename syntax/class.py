class myClass:
    x = 5

p1 = myClass()
# print(p1.x)

# 생성자 : 클래스 생성되는 객체의 초기화를 담당하는 함수
class Person:
    def __init__(self, name, age):  
        # self는 객체 자신을 의미(default)
        self.name = name
        self.age = age

p2 = Person('maya', 50)
print(p2.name)
print(p2.age)