def deleteAddressBook():
    name = input('삭제할 전화번호를 입력하세요:')
    if name in AddressBook.keys():
        del AddressBook[name]
        print('삭제되었습니다.')
    else:
        print('삭제할 번호가 없습니다.')

def addAddressBook():
    data = input('이름, 전화번호를 입력하세요: ').split()
    AddressBook[data[0]] = data[1]
    print('추가되었습니다.')

def queryAddressBook():
    if len(AddressBook) == 0:
        print('등록된 번호가 없습니다.')
    else:
        for data in AddressBook.items():
            print('이름:', data[0], '전화번호:', data[1])

AddressBook = dict()

while True:
    command = input('전화번호부를 조회하려면 조회 / 추가하려면 추가 / 삭제하려면 삭제를 입력하세요 끝내려면 끝을 입력하세요: ')
    if command == '조회':
        queryAddressBook()
    elif command == '추가':
        addAddressBook()
    elif command == '삭제':
        deleteAddressBook()
    elif command == '끝':
        break
    else:
        print('명령어가 잘못되었습니다.')
