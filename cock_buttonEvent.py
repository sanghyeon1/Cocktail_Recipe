from tkinter import *


# 칵테일 레시피 검색 버튼 클릭 이벤트
def click_button1():
    win_b1 = Tk()
    win_b1.title("칵테일 레시피 검색")
    win_b1.geometry("500x700")
    win_b1.option_add("*Font", "맑은고딕 20")

    label = Label(win_b1, text='칵테일 레시피 검색하기')
    label.place(x=10, y=10)


def click_button2():
    win_b2 = Tk()
    win_b2.title("만들 수 있는 칵테일 검색")
    win_b2.geometry("500x700")
    win_b2.option_add("*Font", "맑은고딕 20")


def click_button3():
    win_b3 = Tk()
    win_b3.title("프로그램 사용 방법")
    win_b3.geometry("500x700")
    win_b3.option_add("*Font", "맑은고딕 20")
    label = Label(win_b3, text='이미지 출처 :\n<a href=\'https://kor.pngtree.com/so/칵테일\'>칵테일 png에서 kor.pngtree.com</a>')
    label.pack()

def click_button4():
    win_b4 = Tk()
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




