# 변수: 특정 키워드 없이 사용
x = 10
print(x)

y = 'park'
print(type(y))

z = 3.14
print(type(z))

print(type(str(x)))

name, age, adress = 'park', 30, 'seoul'
print(name, age, adress)

a = b = c = 11
print(a, b, c)

# 콜렉션 구조분해 할당
fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
print(y)
