#  칵테일 이름, 칠링여부(1은 칠링 / 0은 칠링X), 가니쉬(있으면 이름 / 0은 X), 재료
kir = ['kir', 0, 'twist lemon peel', 'white wine, 3', 'creme de cassis, 0.5']
negroni = ['negroni', 1, 'twist lemon peel', 'gin, 0.75', 'sweet vermouth, 0.75', 'campari, 0.75']

all_cocktail = [kir, negroni]

cock_name = input("검색 할 칵테일 이름을 영어로 입력하십시오 : ")
for i in all_cocktail:
    if cock_name == i[0]:
        print("내용을 찾았습니다. {}".format(i[0]))
    else:
        print("찾는 내용이 없습니다.")
