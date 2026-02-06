# 1. 현재 잔액 출력
# 2. 입금
# 3. 출금
# 4. 종료

def show_balance(balance):
    # {{:,}}: 3자리마다 ,를 추가(1000단위 표시)
    print(f'현재 잔액은 {{:,}}'.format(balance) + '원 입니다,')

def deposit():
    while True:
        amount = input('입금할 금액을 입력해 주세요: ')

        try:
            amount = int(amount)
        except ValueError:
            print(f'{amount}은 유효한 숫자가 아닙니다. 다시 입력해 주세요.')
            continue
        
        if amount <= 0:
            print('입금 금액은 0보다 커야 합니다.')
            continue
        else:
            return amount

def withdraw(balance):
    while True:
        amount = input('출금할 금액을 입력해 주세요: ')

        try:
            amount = int(amount)
        except ValueError:
            print(f'{amount}은 유효한 숫자가 아닙니다. 다시 입력해 주세요.')
            continue
        
        if amount > balance:
            print('잔액이 부족합니다....')
            continue
        elif amount <= 0:
            print('출금 금액은 0보다 커야 합니다.')
            continue
        else:
            return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print('1. 잔액보기')
        print('2. 입금하기')
        print('3. 출금하기')
        print('4. 종료하기')

        choice = input('1, 2, 3, 4 중에서 선택해 주세요: ')

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('잘못된 입력이네요. 다시 선택하세요.')
            continue
    print('프로그램을 종료합니다.')

if __name__ == "__main__":  # 파일이 실행되면 main() 함수를 호출
    main()
