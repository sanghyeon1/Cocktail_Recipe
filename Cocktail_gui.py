from cock_buttonEvent import *

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


# 인트로 창 생성
win_intro = Tk()  # 창 생성
win_intro.geometry("800x700")
win_intro.title("칵테일 레시피")
win_intro.option_add("*Font", "휴먼편지체 25")

button1 = Button(win_intro, text='칵테일 레시피 검색', command=click_button1)
button1.config(width=22)
button1.place(x=200, y=390)

button2 = Button(win_intro, text='만들 수 있는 칵테일 검색', command=click_button2)
button2.config(width=22)
button2.place(x=200, y=460)

button3 = Button(win_intro, text='프로그램 사용 방법', command=click_button3)
button3.config(width=22)
button3.place(x=200, y=530)

button4 = Button(win_intro, text='나가기', command=click_button4)
button4.config(width=22)
button4.place(x=200, y=600)

win_intro.mainloop()  # 창 실행
