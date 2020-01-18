def calculator(calcType, a, b):
    if calcType == "add":
        return a + b
    elif calcType == "sub":
        return a - b
    elif calcType == "mul":
        return a * b
    elif calcType == "div":
        return a / b
    else:
        return "올바른 계산 타입이 아닙니다."

# 파라미터가 없는 함수가 있을 수 있다.
def sayGoodBye():
    return "Good Bye!"
# 함수값으로 함수를 넣을 수 있다.
def printGoodBye():
    print(sayGoodBye())

# try 에러가 날 가능성이 있는 코드가 들어감.
try:
    result = calculator("add", 2, 3)
    print(result)
    result = calculator("sub", 2, 3)
    print(result)
    result = calculator("mul", 2, 3)
    print(result)
    result = calculator("div", 2, 0)
    print(result)

# 에라가 났을 경우 except를 수행.
except:
    print("Error 발생했습니다.")

print(sayGoodBye())
printGoodBye()


#아래 두개는 같음.
result1 = calculator("add", 2, 3)
print(result1)

result1 = calculator(a=2, b=3, calcType="add")
print(result1)
