# 자료 묶음 문법 : List, Tuple, Set, Dictionary
# List : 순서가 있고, 중복 데이터 입력이 가능하다.

a = ['apple', 'banana', 'cherry', 'apple']
print(a)
print(type(a))

# 범위 지정 변경
b = ['사과', '바나나', '체리', '사과', '오렌지', '망고']
# b[1:3] = ['포도', '자두'] 
b[1:2] = ['포도', '자두']  # 1번 인덱스 변경 후 나머지 데이터는 뒤로 밀린다.
# print(b)
# print(type(b))

# append: 리스트 맨 뒤에 데이터 추가
b.append('수박')

# insert: 특정 인덱스에 데이터 추가
b.insert(1, '키위')

# remove: 특정 데이터 삭제 - 중복 데이터가 있을 경우 맨 앞의 데이터만 삭제
b.remove('사과')

# del: 특정 데이터 삭제
del b[1]

# pop: 특정 인덱스 데이터 삭제 - 변수에 저장할 수 있음
c = b.pop(1)
# print(c)
# print(b)

# clear: 리스트의 전체를 삭제
b.clear()
print(b)
