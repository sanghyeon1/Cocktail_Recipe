from cock_information import *

all_cocktail = cocktails()


#  칵테일의 정보들을 출력해주는 함수
def information(name):
    if name[1] == 1:
        chill = '칠링'
    else:
        chill = '칠링안함'
    if name[2] == 0:
        check_garnish = '가니쉬 없음'
    else:
        check_garnish = name[2]
    print("{}:\n칠링 - {}\n가니쉬 - {}\n재료 -".format(name[0], chill, check_garnish))
    for j in range(len(name[3])):
        print(name[3][j])


#  칵테일 이름을 찾는 함수
def search():
    cock_name = input("찾고싶은 칵테일 이름을 영어로 입력하십시오. ")
    check = 0
    for i in all_cocktail:
        if cock_name in i[0]:
            print("찾았습니다\n")
            print("=====================================")
            information(i)  # 칵테일 정보 출력
            print("=====================================")
        else:
            check += 1
            pass

    if check == len(all_cocktail):
        print("찾는 칵테일이 없습니다.")


#  현재 내가 가지고 있는 재료를 가지고 뭘 만들 수 있는지 찾는 함수
def available_to_make():
    inhand = ['peach liqueur', 'tequila', 'rum', 'gin', 'bodka',
              'triple sec', 'blue currasso', 'kahlua', 'midori', 'grenadine syrup',
              'creme de cassis', 'salt/pepper']

    for i in range(len(all_cocktail)):
        name = all_cocktail[i]
        stack = 0
        for j in range(len(name[3])):
            str1, num1 = name[3][j].split(", ")  # 만약 not enough values to unpack 일경우 데이터에 ","가 있는지 확인할 것.
            if str1 in inhand or 'juice' in str1:
                stack += 1
            else:
                break
        if stack >= len(name[3]):
            print("{}은 가지신 재료로 만들 수 있습니다.".format(name[0]))


def main():
    while True:
        work = input("무엇을 하시겠습니까?\n[1] 칵테일 레시피 검색\n[2] 가지고있는 재료로 만들 수 있는 칵테일 찾기\n--> ")
        if work == '1':
            search()
        elif work == '2':
            available_to_make()

        else:
            print("1 또는 2 를 입력해주세요.", end='')
        work = 0
        print("\n")


main()
