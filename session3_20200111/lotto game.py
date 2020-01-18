from random import randint

user_numbers = []
lucky_numbers = []

print('1~10까지의 숫자를 5개 입력하십시오.')

#추첨 엔트리용 숫자를 고른다.
while 0 <= len(user_numbers) < 5 :
    input_numbers = input('>')

    try:
        a = int(input_numbers)
    except:
        print('무효한 값입니다. 다시 입력하십시오.')
        continue

    if 0 > a or a > 10:
        print('1~10까지의 숫자를 입력하십시오.')
        continue
    elif a in user_numbers:
        print(user_numbers, '이외의 숫자를 입력하십시오.')
        continue
    user_numbers.append(a)
print('당신이 고른 숫자는', user_numbers, '입니다. \n')

#당첨 번호를 고른다.
print('추첨을 시작합니다.')
while 0 <= len(lucky_numbers) < 5:
    b = randint(1, 10)
    if b not in lucky_numbers:
        lucky_numbers.append(b)
    else:   #추첨한 숫자의 중복을 피한다.
        continue
print(lucky_numbers, '\n')

#추첨 엔트리용 번호와 당첨 번호를 비교하나다.
userset = set(user_numbers)
luckyset = set(lucky_numbers)
winset = userset.intersection(luckyset)
print('당첨된 숫자는', winset)
print('당첨된 개수는', len(winset), '개입니다.')