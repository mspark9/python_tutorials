# if 조건문
a = 100
b = 200
c = 300

# if a > b:
#     print("a는 b보다 크다")
# elif b > c:
#     print("b는 c보다 크다")
# else:
#     print("c는 a보다 크다")

# if 축약형
# if a < b: print("a는 b보다 작다")
# print('a가 b보다 작다.') if a < b else print('a가 b보다 크다.')
# print('a') if a < b else print('=') if a == b else print('b')

# 논리 연산: and, or, not
# if a < b and b < c:
#     print("a는 b보다 작고 b는 c보다 작다")

# if a < b or b < c:
#     print("a는 b보다 작거나 b는 c보다 작다")

# if not a < b:
#     print("a는 b보다 크다")

# if nesting
x = 4
if x > 5:
    print("x는 5보다 크다")
    if x > 10:
        print("x는 10보다 크다")
    else:
        print("x는 5보다 크고 10보다 작다")
else:
    print("x는 5보다 작다")