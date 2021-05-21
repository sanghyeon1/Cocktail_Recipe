#  칵테일 이름, 칠링여부(1은 칠링 / 0은 칠링X), 가니쉬(있으면 이름 / 0은 X), 재료
kir = ['kir', 0, 'twist lemon peel', ['white wine, 3', 'creme de cassis, 0.5']]
negroni = ['negroni', 1, 'twist lemon peel', ['gin, 0.75', 'sweet vermouth, 0.75', 'campari, 0.75']]
oldfashioned = ['oldfashioned', 0, 'sliced orange & cherry', ['american whiskey, 1.5', 'cubed suger, 1', 'angostura bitters, 1', 'club soda, 0.5']]
rustynail = ['rustynail', 1, 0, ['scotch whiskey, 0.75', 'drambuie, 0.5']]
blackrussian = ['blackrussian', 1, 0, ['bodka, 1', 'kahlua 0.5']]
moscowmule = ['moscowmule', 1, 'sliced lemon', ['bodka, 1.5', 'lime juice 0.5', 'ginger ale']]

all_cocktail = [kir, negroni, oldfashioned, rustynail, blackrussian, moscowmule]


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


search = input("찾고싶은 칵테일 이름을 영어로 입력하십시오. ")
check = 0
for i in all_cocktail:
    if search in i[0]:
        print("찾았습니다\n")
        print("=====================================")
        information(i)
        print("=====================================")
    else:
        check += 1
        pass

if check == len(all_cocktail):
    print("찾는 칵테일이 없습니다.")
