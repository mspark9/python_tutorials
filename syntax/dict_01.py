# 자료 묶음 문법 : List, Tuple, Set, Dictionary
# dictionary : 
# - 중복이 허용되지 않는다.
# - 변경이 가능하다.
# - 순서가 없다.
# - key와 value 쌍으로 구성된다.
# - 자바스크립트의 객체와 유사하다.

a = {
    'name': 'John',
    'age': 30, 
    'address': 'New York',
    'phone': ['010-1111-1111', '010-1234-5678']
    }
# print(a)
# print(type(a))

# 데이터 접근
# print(a['name'])
# print(a['age'])
# print(a['address'])
# print(a['phone'][0])

# get으로 접근
# print(a.get('name'))

# key 값만 출력
# print(a.keys())

# 길이
# print(len(a))

# 생성자 사용
b = dict(name='John', age=30, address='New York')
# print(b)

# 요소의 변경
a['name'] = 'John Doe'
a.update({'age': 39})

# 요소의 추가
a['color'] = ['yellow', 'green', 'blue']
# print(a)

# 반복문 사용
for x in a:
    print(x, a.get(x))