#  칵테일 이름, 칠링여부(1은 칠링 / 0은 칠링X), 가니쉬(있으면 이름 / 0은 X), 재료
kir = ['kir', 0, 'twist lemon peel', ['white wine, 3', 'creme de cassis, 0.5']]
negroni = ['negroni', 1, 'twist lemon peel', ['gin, 0.75', 'sweet vermouth, 0.75', 'campari, 0.75']]
oldfashioned = ['oldfashioned', 0, 'sliced orange & cherry', ['american whiskey, 1.5', 'cubed suger, 1', 'angostura bitters, 1', 'club soda, 0.5']]
rustynail = ['rustynail', 1, 0, ['scotch whiskey, 0.75', 'drambuie, 0.5']]
blackrussian = ['blackrussian', 1, 0, ['bodka, 1', 'kahlua, 0.5']]
moscowmule = ['moscowmule', 1, 'sliced lemon', ['bodka, 1.5', 'lime juice, 0.5', 'ginger ale, 8']]


all_cocktail = [kir, negroni, oldfashioned, rustynail, blackrussian, moscowmule]


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
              'creme de cassis']

    for i in range(len(all_cocktail)):
        name = all_cocktail[i]
        stack = 0
        for j in range(len(name[3])):
            str1, num1 = name[3][j].split(", ")  # 만약 not enough values to unpack 일경우 데이터에 ","가 있는지 확인할 것.
            if str1 in inhand:
                stack += 1
            else:
                break
        if stack >= len(name[3]):
            print("{}은 가지신 재료로 만들 수 있습니다.".format(name[0]))


def main():

    while True:
        work = int(input("무엇을 하시겠습니까?\n[1] 칵테일 레시피 검색\n[2] 가지고있는 재료로 만들 수 있는 칵테일 찾기\n--> "))
        if work == 1:
            search()
        elif work == 2:
            available_to_make()

        else:
            work = int(input("1 또는 2 를 입력해주세요."))
        work = 0
        print("\n")


main()
