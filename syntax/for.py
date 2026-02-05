# for 

myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
myTuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
mySet = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

# for i in myList:
#     if i == 'b':
#         continue  # b만 건너뛰고 출력    
#     print(i)

# range(start, end, step)
# for i in range(3, 10, 2):
#     print(i)
# else:
#     print("반복문 종료")

for i in range(2, 10):
    for j in range(2, 10):
        print(i, 'x', j, '=', i * j)

    print('------------------')
