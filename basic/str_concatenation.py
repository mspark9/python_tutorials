# 문자열 연결
a = "hello"
b = " world"
print(a+b)

# 문자열 포맷팅
name = 'Alice'
age = 20
txt = "내이름은 {}야. 나이는 {}살.".format(name, age)
print(txt)

# f-string
print(f'내이름은 {name}야. 나이는 {age}살.')

# escape : https://zzozzomin08.tistory.com/39
# 1. 내부 특수문자
hello = "hello. my age is \\\"20\\\" years old."
print(hello)

# 2. 문자열 개행
hello = "hello. my \nage is 20 years old."
print(hello)

# 3. 문자열 탭
hello = "hello\tmy age is 20 years old."
print(hello)

# 4. 백스페이스
hello = "hello\bmy age is 20 years old."
print(hello)