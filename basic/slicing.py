# 슬라이싱: 문자열 일부를 추출하는 방법

a = 'Loremipsumdolorsitametconsecteturadipisicingelit'
print(a[0])
print(a[7])
print(a[-1])

# slicing
print(a[0:5])  # 0에서 5미만 까지
print(a[:5])  # 0에서 5미만 까지
print(a[5:])  # 5에서 마지막 까지
print(a[2:5])  # 2에서 5미만 까지
print(a[:])  # 전체 

# str[start:end:step]
print(a[::2])  # 2칸씩 이동 출력
print(a[::-1])  # 역순으로 출력
print(a[2:10:1])  # 2에서 10미만까지 1칸씩 이동 출력

# 문자열 길이
print(len(a))

# 대소문자
b = '  park park  '
print(b)
print(b.upper())
print(b.lower())
print(b.strip())
