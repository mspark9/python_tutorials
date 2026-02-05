unit = input('변환할 온도 체계를 정해 주세요( c or f): ')

if unit !='c' and unit != 'f':
    print(f'{unit}은 변환할 수 없는 온도 체계 입니다.')
    exit()

temp = float(input('온도를 입력해 주세요: '))

c_or_f = ''

try:
    temp = float(temp)
except ValueError:
    print(f'{temp}는 유효하지 않은 문자열 입니다. 숫자로 입력해 주세요.')
    exit()

if unit.lower() == 'c':
    temp = round((temp * 9/5) + 32)
    c_or_f = '화씨'
elif unit.lower() == 'f':
    temp = round((temp - 32) * 5/9)
    c_or_f = '섭씨'

print(f'변환한 온도는 {c_or_f} {temp}도 입니다.')