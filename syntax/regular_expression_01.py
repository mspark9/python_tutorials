# 정규표현식이란 문자열을 처리하는 방법 중의 하나로 특정한 조건의 문자를 '검색'하거나 '치환'하는 과정을 매우 간편하게 처리할 수 있도록 하는 수단이다.

import re

# search
a = 'I live in seoul 123'
# ^ : 문자열의 시작
# $ : 문자열의 끝
# . : 임의의 문자
# * : 전체

# I로 시작해서 seoul로 끝나는 문자열을 검색
b = re.search("^I.*seoul$", a)
# print(b)

#findall() : 매칭되는 모든 문자열을 리스트로 반환
c = re.findall("[a-zA-Z0-9]", a)
d = re.findall("\d", a)  # 숫자만 검색(digit)
e = re.findall("\w", a)  # 문자, 숫자, 언더스코어
# print(c)
# print(d)
# print(e)

f = re.findall("K.*a", a)  # k로 시작해서 a로 끝나는 문자열 검색
g = re.findall("Kore.+a", a)  # Kore와 a 사이에 어떤 문자가 1개 이상 있는 문자열 추출 Korema, koremoa... 등으로 수정하면 찾을 수 있음
h = re.findall("live|seoul", a)
print(h)