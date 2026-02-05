# center : 문자열을 중앙에 위치시키는 기능\
a = "world"
b = a.center(10)
c = a.center(20)
dummy = "123456789876543210"
print(b)
print(c)
print(dummy)

# count: 문자열에서 특정 문자열 개수 확ㅇ니
d = "Loremipsum,dolorsitametcon,secteturadipis,icingelit"
print(d.count('a'))

# endswitch: 문자열이 특정 문자열로 끝나는지 확인
e = d.endswith('lit')
f = d.endswith('li')
print(e)
print(f)

# split: 특정 문자열 기준으로 분류
g = d.split(',')
print(g)