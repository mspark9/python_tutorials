# 자료 묶음 문법 : List, Tuple, Set, Dictionary
# set : 
# - 인덱스로 접근할 수 없다.
# - 내부 요소를 수정할 수 없다.
# - 중복된 요소가 포함될 수 없다. - 중복 데이터가 있을 경우 오류가 나지는 않지만 중복 데이터는 표현되지 않는다.
# - 순서가 없어서 매번 바뀐다.
# - 중괄호를 사용한다.

a = {1, 2, 3, 4, 5}  # 숫자는 순서가 바뀌지 않는다.
# print(a)

b = {'체리', '오렌지', '파인애플', '포도'}
# print(b)

c = {True, 1, 2, 3}  # True는 1, False는 0으로 인식된다. True와 1은 중복되어 하나만 표시.
# print(c)

# 생성자 사용
d = set(('a', 'b', 'c'))
# print(d)
# print(type(d))

# 존재 여부
e = '사과' in b
# print(e)

# 요소 추가 : add()
b.add('사과')  # 추가 위치는 정해지지 않는다.
# print(b)

# 여러 요소 추가 : update()
b.update(a)
# print(b)

# 요소 삭제 : remove(), discard()
# b.remove('망고')  # 에러 발생
b.discard('망고')  # 에러 발생하지 않음
b.pop()  # 랜덤으로 삭제
print(b)
