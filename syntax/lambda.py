# lambda
y = lambda x : x * 2  # 인수 a를 받아서 2를 곱한다.
# print(y(5))

# 파라미터가 여러개인 람다 함수
z = lambda x, y : x * y
# print(z(5, 2))

# 람다 함수를 다른 함수에 사용
def myfunc(n):
    return lambda a : a * n

# mf1 = myfunc(2)
# print(mf1(5))

# 필터링을 사용한 람다
myList = list(filter(lambda x: x % 2, range(10)))
print(myList)