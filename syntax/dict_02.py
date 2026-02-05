a = {
    'name': 'John',
    'age': 30, 
    'address': 'New York',
    'phone': ['010-1111-1111', '010-1234-5678'],
    'hobby': ['reading', 'running', 'listening to music']
    }

# key 값만 출력
# for x in a.keys():
#     print(x)

# value 값만 출력
# for x in a.values():
#     print(x)

# items
# print(a.items())  # key와 value를 튜플 리스트로 출력
for key, value in a.items():
    print(key, value)