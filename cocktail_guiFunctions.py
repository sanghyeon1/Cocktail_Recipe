from cock_information import *

all_cocktail = cocktails()
# 만들 수 있는 칵테일의 정보를 담고, 원하는 칵테일의 레시피를 보여주기 위한 변수.
valid_cocktail = []


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

    ingredients = []
    for j in range(len(name[3])):
        ingredients.append(name[3][j])

    str_list = ['', '칠링 - ', '가니쉬 - ', '재료 -']
    info_list = [name[0], chill, check_garnish, ingredients]
    recipe_list = []
    for i in range(4):
        recipe_list.append(str_list[i] + str(info_list[i]))

    return recipe_list


#  칵테일 이름을 찾는 함수
def search(cock_name):
    check = 0
    for i in all_cocktail:
        if cock_name in i[0]:  # 찾았을 때
            return information(i)
        else:
            check += 1
            pass

    if check == len(all_cocktail):  # 없을 때
        return False


def valid_search(name):
    check = 0
    print("{}의 레시피를 출력합니다.".format(name))
    for i in all_cocktail:
        if name == i[0]:
            print("=====================================")
            information(i)  # 칵테일 정보 출력
            print("=====================================")
        else:
            check += 1
            pass

    if check == len(all_cocktail):
        print("찾는 칵테일이 없습니다.")


#  현재 내가 가지고 있는 재료를 가지고 뭘 만들 수 있는지 찾는 함수
def available_to_make(hold):
    global valid_cocktail
    valid_cocktail.clear()

    for i in range(len(all_cocktail)):
        name = all_cocktail[i]
        stack = 0
        for j in range(len(name[3])):
            str1, num1 = name[3][j].split(", ")  # 만약 not enough values to unpack 일경우 데이터에 ","가 있는지 확인할 것.
            if str1 in hold or 'juice' in str1:
                stack += 1
            else:
                break
        if stack >= len(name[3]):
            valid_cocktail.append(name)

    return valid_cocktail
