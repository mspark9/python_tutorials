# 프로그램이 시작되면 음식 이름 입력을 받는다
# 받은 음식은 foots 리스트에 추가된다.
# q를 입력하면 종료된다
# 음식의 가격을 묻는다.
# 받은 가격은 prices 리스트에 추가된다.
# 종료되면 선택한 모든 음식을 출력한다.
# 선택함 모든 음식의 가격을 합산하여 출력한다.

foods = []
prices = []
total = 0

# 방법 1
# def main():
#     while True:
#         food = input('원하는 음식 이름을 입력해 주세요: ')
#         if food == 'q':
#             break
#         foods.append(food)
#         price = int(input('음식 가격을 입력해 주세요: '))
#         prices.append(price)
#         total = sum(prices) 
#     print('선택한 음식:', foods)
#     print('선택한 음식 가격:', prices)
#     print('총 가격:', total)
#     print('프로그램을 종료합니다.')

# if __name__ == "__main__":
#     main()


# 방법 2
while True:
    food = input('원하는 음식 이름을 입력해 주세요. 종료는 q를 누르세요: ')
    if food == 'q':
        break
    else:
        foods.append(food)
        price = int(input(f'{food} 가격을 입력해 주세요: '))
        prices.append(price)

print('----------Your Cart--------------')

for food in foods:
    print(food)

for price in prices:
    total += price

print(f'총 카트에 담긴 상품의 가격 총액은 {total}원 입니다.')