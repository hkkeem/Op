#딕셔너리 while문

def deleteAdressBook():
    name = input('삭제할 사람의 이름을 입력하세요:')
    if name in AdressBook:
        del AdressBook[name]
        print('삭제되었습니다.')

def addAdressBook():
    data = input('이름, 번호를 입력하세요:')
    name = data[0]
    number = data[1]
    AdressBook[data[0]] = data[1]
    print('추가되었습니다.')

def queryAdressBook():
    if len(AdressBook) == 0:
        print('등록된 번호가 없습니다.')
    else:
        print(AdressBook)

def endAdressBook():

AdressBook = dict()
while True:
    command = input('전화번호부를 조회하려면 조회 / 추가하려면 추가 / 삭제하려면 삭제를 입력하세요 끝내려면 끝을 입력하세요.')
    if command == "조회":
        queryAdressBook()
    elif command == "추가":
        addAdressBook()
    elif command == "삭제":
        deleteAdressBook()
    elif command == "끝":
        break
        endAdressBook()
    else:
        print("명령어가 잘못되었습니다.")

