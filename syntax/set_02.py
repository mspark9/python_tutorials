a = {'바나나', '체리', '딸기'}
b = {'바나나', '포도'}

# union : 두개의 set을 새로운 변수에 합쳐서 담는다.
c = a.union(b)  # 중복 데이터는 제외된다.
# print(c)

# clear : set을 비운다.
# a.clear()  # 객체 공간은 유지
# print(a)

# copy : 복사
d = b.copy()
# print(d)

# difference : 차집합
e = a.difference(b)
# print(e)

# intersection : 교집합
f = a.intersection(b)
print(f)

# symmetric_difference : a와 b의 합집합에서 교집합 제거
print(a.symmetric_difference(b))
