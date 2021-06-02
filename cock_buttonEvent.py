from tkinter import *
from PIL import Image, ImageTk
from cocktail_guiFunctions import *

from cock_images import cocktail_image as ci

all_images = ci()  # 리스트


# 칵테일 레시피 검색 버튼 클릭 이벤트
def click_button1():
    win_b1 = Toplevel()
    win_b1.title("칵테일 레시피 검색")
    win_b1.geometry("500x900")
    win_b1.option_add("*Font", "맑은고딕 20")

    label = Label(win_b1, text='칵테일 레시피 검색하기')
    label.place(x=10, y=10)

    def clear(event):
        if ent1.get() == "칵테일 이름(영어)":
            ent1.delete(0, len(ent1.get()))

    def get_str():
        name = ent1.get()
        return name

    def load_image(num):
        if num == 0:
            pos_y = 100
        else:
            pos_y = 110
        # 레이블 지우는 대신 이미지 로드로 레이블 덮어씌우기
        load = Image.open(all_images[num][1])
        photo = ImageTk.PhotoImage(load)
        load_label = Label(win_b1, image=photo)
        load_label.image = photo
        load_label.place(x=0, y=pos_y)
        # 칵테일 이름에 따른 이미지 로드

    def show_recipe():
        name = get_str()
        label4_y = 0  # 아래 "===" 출력 레이블에서의 y 좌표.
        if name == '칵테일 이름(영어)':
            search_label1 = Label(win_b1, text="유효하지 않은 값입니다.")
            search_label1.place(x=10, y=100)
        else:
            recipe_list = search(name)
            load_image(0)
            if recipe_list is False:
                srch_label5 = Label(win_b1, text="찾는 칵테일이 없습니다.\n띄어쓰기는 \"_\"입니다.")
                srch_label5.place(x=10, y=100)

            else:
                j = 0
                for i in all_images:
                    if i[0] == recipe_list[0]:
                        load_image(0)
                        load_image(j)
                    else:
                        j += 1
                        pass
                search_label2 = Label(win_b1, text="=====================================")
                search_label2.place(x=10, y=500)

                ingredient_list = recipe_list[3].split("재료 -[")
                ingredient_list = ingredient_list[1][0:len(ingredient_list[1]) - 1]
                ingredient_list = ingredient_list.split("', '")

                for i in range(4):
                    if i == 3:
                        for j in range(len(ingredient_list)):
                            search_label6 = Label(win_b1, text="재료 - ")
                            search_label6.place(x=10, y=550 + (i * 30))
                            search_label3 = Label(win_b1, text=ingredient_list[j])
                            search_label3.place(x=10, y=550 + ((i + 1) * 30) + (j * 30))
                            label4_y = 550 + ((i + 1) * 30) + (j * 30) + 30
                    else:
                        search_label3 = Label(win_b1, text=recipe_list[i])
                        search_label3.place(x=10, y=550 + (i * 30))

                search_label4 = Label(win_b1, text="=====================================")
                search_label4.place(x=10, y=label4_y)

    ent1 = Entry(win_b1)
    ent1.insert(0, "칵테일 이름(영어)")
    ent1.bind("<Button-1>", clear)
    ent1.config(width=18)
    ent1.place(x=10, y=60)

    btn_search = Button(win_b1, text="검색", command=show_recipe)
    btn_search.option_add("*Font", "맑은고딕 15")
    btn_search.place(x=310, y=50)

    win_b1.mainloop()


# 보유 중인 재료 선택 후 만들 수 있는 칵테일 검색 이벤트
def click_button2():
    win_b2 = Toplevel()
    win_b2.title("만들 수 있는 칵테일 검색")
    win_b2.geometry("550x900")
    win_b2.option_add("*Font", "맑은고딕 20")

    label = Label(win_b2, text='만들 수 있는 칵테일 찾기')
    label.pack()
    label = Label(win_b2, text='아래에서 보유 중인 재료를 체크하십시오.\n===============================')
    label.pack()

    hold_ingredient = []

    # 검색하기 버튼 클릭 이벤트
    def btn_check():
        for i in range(len(inhand)):
            if ck_val[i].get() is True:
                hold_ingredient.append(inhand[i])
            else:
                pass
        return hold_ingredient

    # 모두체크 기능
    def check_all():
        if ck_val2.get() is True:
            for i in range(len(inhand)):
                ck_val[i].set(True)

        else:
            for i in range(len(inhand)):
                ck_val[i].set(False)

    # ==========================체크 버튼 생성==========================================
    inhand = ['peach liqueur', 'tequila', 'rum', 'gin', 'bodka', 'coconut flavored rum',
              'triple sec', 'blue curacao', 'kahlua', 'midori', 'grenadine syrup',
              'creme de cassis', 'salt/pepper', 'sugar', 'club soda', 'ginger ale']

    ck_val = [None] * len(inhand)
    ck_btn = [None] * len(inhand)
    j = 0
    count = 0
    for i in range(len(inhand)):
        ck_val[i] = BooleanVar()
        ck_val[i].set(False)
        ck_btn[i] = Checkbutton(win_b2, text=inhand[i], font=("System", 20),
                                variable=ck_val[i])

        if i < 10:
            count = 100 + 40 * i
            ck_btn[i].place(x=30, y=count)
        else:
            ck_btn[i].place(x=300, y=100 + 40 * j)
            j += 1
    # ====================================================================================

    ck_val2 = BooleanVar()
    ck_val2.set(False)
    ck_btn2 = Checkbutton(win_b2, text="모두 체크", font=("System", 20),
                          variable=ck_val2, command=check_all)
    ck_btn2.place(x=200, y=count + 50)

    btn_b2 = Button(win_b2, text="검색하기", command=lambda: [valid_to_make_list(btn_check())])
    btn_b2.option_add("*Font", "맑은고딕 30")
    btn_b2.place(x=200, y=count + 80)

    win_b2.mainloop()


num = 0  # 글로벌 변수 / 이미지 출력 시 사용.


# 만들 수 있는 칵테일 목록을 새 창으로 출력
# hold : 체크된 보유재료 목록 리스트.
def valid_to_make_list(hold):
    def before_image():
        global num
        num -= 1
        if len(py_img) == 1:
            num = 0
        elif 0 < num < len(py_img):
            load = Image.open(py_img[num])
            photo = ImageTk.PhotoImage(load)
            label_img = Label(win_b2_1, image=photo)
            label_img.image = photo
            label_img.place(x=0, y=100)
        elif num <= 0:
            label_after = Label(win_b2_1, text='맨 처음입니다.')
            label_after.place(x=400, y=700)
            num += 1

    def after_image():
        global num
        num += 1
        if len(py_img) == 1:
            num = 0
        elif 0 <= num < len(py_img) - 1:
            load = Image.open(py_img[num])
            photo = ImageTk.PhotoImage(load)
            label_img = Label(win_b2_1, image=photo)
            label_img.image = photo
            label_img.place(x=0, y=100)
        elif num >= len(py_img) - 1:
            label_after = Label(win_b2_1, text='마지막입니다.')
            label_after.place(x=400, y=700)
            num -= 1

    win_b2_1 = Toplevel()
    win_b2_1.title("목록")
    win_b2_1.geometry("1000x800")
    win_b2_1.option_add("*Font", "맑은고딕 20")

    label = Label(win_b2_1, text='만들 수 있는 칵테일 목록\n===========================================================')
    label.pack()

    # 만들 수 있는 칵테일 이미지 목록 리스트.
    py_img = []

    # 만들 수 있는 칵테일의 레시피 리스트
    hold_ingredient = available_to_make(hold)

    # py_img 리스트 데이터 생성.
    for i in range(len(hold_ingredient)):
        for j in range(len(all_images)):
            if hold_ingredient[i][0] == all_images[j][0]:
                py_img.append(all_images[j][1])

            else:
                pass

    load = Image.open(py_img[0])
    photo = ImageTk.PhotoImage(load)
    label_img = Label(win_b2_1, image=photo)
    label_img.image = photo
    label_img.place(x=0, y=100)

    before_btn = Button(win_b2_1, text="이전", command=before_image)
    before_btn.place(x=200, y=600)

    after_btn = Button(win_b2_1, text="다음", command=after_image)
    after_btn.place(x=700, y=600)

    win_b2_1.mainloop()


def click_button3():
    win_b3 = Toplevel()
    win_b3.title("프로그램 사용 방법")
    win_b3.geometry("500x700")
    win_b3.option_add("*Font", "맑은고딕 20")
    label = Label(win_b3, text='이미지 출처 :\n<a href=\'\nhttps://kor.pngtree.com/so/칵테일\'\n>칵테일 png에서 kor.pngtree.com</a>')
    label.pack()


def click_button4():
    win_b4 = Toplevel()
    win_b4.title("나가기")
    win_b4.geometry("300x200")
    win_b4.option_add("*Font", "휴먼굵은팸체 30")
    label = Label(win_b4, text='정말 닫으시겠습니까?')
    label.place(x=20, y=20)

    # 나가기 확인, 취소 버튼
    exit_button = Button(win_b4, text='확인', command=quit)
    exit_button.place(x=200, y=100)

    cancel_button = Button(win_b4, text='취소', command=win_b4.destroy)
    cancel_button.place(x=20, y=100)
