# default parameter는 오른쪽부터 설정이 가능하고, 중간부터는 불가능하다.
def add(a, b = 2):
    return a + b

print(add(1, 3))
print(add(1))

# 변수의 scope - 함수 내의 변수는 로컬변수, 함수 밖의 변수는 글로벌 변수
# 함수 내에서 global a라고 호출 가능


#함수 정의 1
def add(a, b = 2):
    return a + b

a = 2

#함수 정의 2
def blankA():
    a = 3
    return a

#정의가 두개지만, 출력 시에는 직전 함수의 영향만 받게 됨.
print(blankA())