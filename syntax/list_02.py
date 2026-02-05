a = ['사과', '바나나', '체리', '사과', '오렌지', '망고']

for x in a:
    print(x)

# sort(): 정렬
# 별도 변수에 저장할 수 없다.
# reverse=True : 역순 정렬
# a.sort()  
a.sort(reverse=True)  
# print(a)

# 리스트 복사 시 b = a 형식으로 복사하면 같은 주소를 참조하기 때문에 a, b 모두 바뀌게 된다. 따라서 복사할 때는 copy()를 사용한다.
b = a.copy()
a[0] = '포도'
# print(a)
# print(b)

# list() : 특정 리스트를 담아서 새로운 리스트를 반환
c = list(a)
c[0] = '자두'
# print(a)
# print(c)

# 리스트 합치기
d = ['new list1', 'new list2']
# e = a + d
# print(e)

# for x in d:
#     a.append(x)
# print(a)

# extend(): 리스트에 다른 리스트를 추가
a.extend(d)
print(a)
