# 리스트는 각각의 Element에 의미를 부여하기 어렵다.
a = list()
a.append("010-1234-5678")
a.append("010-3456-7890")

firstValueInA = a = [0]

# 대안으로 나온 Dictionary
b = {"김도한" : ["010-1212-3434", "010-5555-5555"], "이용섭" : "010-3434-5656"}
dohanValueInB = b["김도한"]
print(type(dohanValueInB))

phoneDictionary = {"김도한" : ["010-1111-2222", "성남시 수정구"]}

c = dict(김도한 = "복정", 이용섭 = "대전")
print(c)

# Dictionary에 존재하지 않는 key를 이용할 경우
# d = c["이근호"] => 에러 발생
# print(d)

is_heywon_exist = "조혜원" in c
print(is_heywon_exist)

if is_heywon_exist:
    print(c["조혜원"])
else:
    print("혜원님은 Dict에 없습니다.")

c["조혜원"] = "010-7890-1234"
c.pop("김도한")

is_dohan_exist = "김도한" in c
is_heywon_exist = "조혜원" in c

print(is_dohan_exist)
print(is_heywon_exist)