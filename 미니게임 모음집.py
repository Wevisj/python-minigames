from tkinter import *
import random
from tkinter import font
import tkinter.messagebox as msgbox
import time
import winsound

a=Tk()

a.title("Big Game")
a.geometry("750x750")
a.resizable(0, 0)
a.configure(bg="gray")
font1=font.Font(family="스스로넷 설립체", size=18)
font2=font.Font(family="스스로넷 설립체", size=25)
font3=font.Font(family="스스로넷 설립체", size=12)
font4=font.Font(family="궁서체", size=20)
font5=font.Font(family="스스로넷 설립체", size=40)
font6=font.Font(family="스스로넷 설립체", size=22)
font7=font.Font(family="스스로넷 설립체", size=40)
font8=font.Font(family="궁서체", size=40)
font9=font.Font(family="스스로넷 설립체", size=8)

fr=[0]*30

fr[0]=Frame(a, width=750, height=750, bg="gray")
fr[0].pack()
fr[1]=Frame(a, width=750, height=750, bg="gray")
fr[2]=Frame(a, width=750, height=750, bg="white")
fr[3]=Frame(a, width=750, height=750, bg="gray")
fr[4]=Frame(a, width=750, height=750, bg="white")
fr[5]=Frame(a, width=750, height=750, bg="gray")
fr[6]=Frame(a, width=750, height=750, bg="white")
fr[20]=Frame(a, width=750, height=750, bg="gray")
fr[21]=Frame(a, width=750, height=750, bg="skyblue2")
fr[22]=Frame(a, width=750, height=750, bg="skyblue2")
fr[23]=Frame(a, width=750, height=750, bg="gray")

fr2=[0]*5
fr2[0]=Frame(a, width=750, height=750, bg="gray")
fr2[1]=Frame(a, width=750, height=750, bg="gray")
fr2[2]=Frame(a, width=750, height=750, bg="gray")
fr2[3]=Frame(a, width=750, height=750, bg="gray")
fr2[4]=Frame(a, width=750, height=750, bg="gray")

fr3=[0]*10
fr3[0]=Frame(a, width=750, height=750, bg="white")
fr3[1]=Frame(a, width=750, height=750, bg="gray")
fr3[2]=Frame(a, width=750, height=750, bg="gray")
fr3[3]=Frame(a, width=750, height=750, bg="gray")
fr3[4]=Frame(a, width=750, height=750, bg="gray")

img1=PhotoImage(file="uc1.gif")
img2=PhotoImage(file="front.gif")
img3=PhotoImage(file="back.gif")
img4=PhotoImage(file="snail_1.gif")
img5=PhotoImage(file="snail_2.gif")
img6=PhotoImage(file="snail_3.gif")

def final_go1():
    fr[21].destroy()
    fr[22].pack()
    end3=Label(fr[22], font=font7, bg="skyblue2", text="당신은 최종 승자입니다 !\n축하드립니다.", fg="white")
    end3.place(x=100, y=300)
    a.update()
    winsound.PlaySound("승리.wav", winsound.SND_FILENAME)

def final_go2():
    fr[21].destroy()
    fr[23].pack()
    end3=Label(fr[23], font=font8, bg="gray", text="당신은 패배자입니다.\n다음 기회를 노려보세요 !", fg="black")
    end3.place(x=70, y=300)
    a.update()
    winsound.PlaySound("패배화면-녹픽.wav", winsound.SND_FILENAME)

def final():
    fr[0].destroy()
    end1.destroy()
    fr[21].pack()
    global main_count
    if main_count>=2:
        end2=Button(fr[21], text="최종 결과 확인하기", font=font1, bg="skyblue3", fg="black", command=final_go1)
        end2.place(x=250, y=500)
    elif main_count<2:
        end2=Button(fr[21], text="최종 결과 확인하기", font=font1, bg="skyblue3", fg="black", command=final_go2)
        end2.place(x=250, y=500)

end1=Button(a, text="최종 화면으로", font=font1, bg="gray", fg="black", command=final)

x=1
k=0
k1=3

def count_plus(i):
    i+=1
    return i

def count_minus(i):
    i-=1
    return i

score_count=0
main_count=0
game_count=0

def g1_r():
    global k1
    fr[0].destroy()
    global x
    global k
    if k==3:
        fr[0].destroy()
        fr3[1].destroy()
    elif k==2:
        fr[0].destroy()
        fr2[1].destroy()
    k=1
    if x==1 and k1!=1:
        del select[0]
    if x==1:
        k1-=1
    select_1=random.choice(select)
    global score_count
    global game_count
    global main_count
    if x==1:
        fr[0].destroy()
    else :
        fr[x-1].destroy()
    if x==7 or score_count>=2:
        if score_count>=2:
            fr[20].pack()
            a6=Label(fr[20], text="  당신은 이 게임에서 이겼습니다 !\n축하드립니다.", font=font2, bg="gray", fg="white")
            a6.place(x=100, y=120)
            main_count+=1
            game_count+=1
            a7=Label(fr[20], text="버튼을 누르면 다음 게임으로 넘어갑니다.", font=font1, bg="gray", fg="white")
            a7.place(x=150, y=400)
            a8=Button(fr[20], text="다음 게임으로", font=font1, bg="gray", fg="black", command=select_1)
            a8.place(x=270, y=450)
            if game_count==3:
                fr[20].destroy()
                end1.place(x=290, y=450)
        elif score_count<2:
            fr[20].pack()
            a6=Label(fr[20], text="  당신은 이 게임에서 패배하셨습니다\n안타깝네요.", font=font2, bg="gray", fg="white")
            a6.place(x=100, y=120)
            game_count+=1
            a7=Label(fr[20], text="버튼을 누르면 다음 게임으로 넘어갑니다.", font=font1, bg="gray", fg="white")
            a7.place(x=150, y=400)
            a8=Button(fr[20], text="다음 게임으로", font=font1, bg="gray", fg="black", command=select_1)
            a8.place(x=270, y=450)
            if game_count==3:
                fr[20].destroy()
                end1.place(x=290, y=450)
    elif x==5 and score_count==0:
        fr[20].pack()
        a6=Label(fr[20], text="  당신은 이 게임에서 패배하셨습니다\n안타깝네요.", font=font2, bg="gray", fg="white")
        a6.place(x=100, y=120)
        game_count+=1
        a7=Label(fr[20], text="버튼을 누르면 다음 게임으로 넘어갑니다.", font=font1, bg="gray", fg="white")
        a7.place(x=150, y=400)
        a8=Button(fr[20], text="다음 게임으로", font=font1, bg="gray", fg="black", command=select_1)
        a8.place(x=270, y=450)
        if game_count==3:
            fr[20].destroy()
            end1.place(x=290, y=450)
        
    else :
        fr[x].pack()
        inf=Label(fr[x], text="이번 게임은 동전의 앞 뒤 맞추기 입니다.\n\n게임은 3판 2선으로 진행됩니다.\n\n학 그림은 앞, 숫자는 뒤입니다.", font=font1, bg="gray", fg="white")
        inf.place(x=150, y=100)
        a1=Label(fr[x], text="엔터키를 누르면 동전의 앞뒤가 결정됩니다.", font=font1, bg="gray", fg="white")    
        a1.place(x=150, y=350)
        a.bind("<Return>", g1)

def g1(self):
    winsound.PlaySound("동전소리.wav", winsound.SND_FILENAME)
    global b1
    global b2
    global x
    fr[x].destroy()
    fr[x+1].pack()
    b1=random.randint(1,2)
    b2=0
    a1=Label(fr[x+1], image=img1)
    a1.place(x=300, y=200)
    a2=Label(fr[x+1], text="앞, 뒤 중 선택 !", font=font1)
    a2.place(x=270, y=400)
    a3=Button(fr[x+1], text="앞", font=font1, fg="white", bg="black", relief="flat", command=g1_1)
    a3.place(x=250, y=450)
    a4=Button(fr[x+1], text="뒤", font=font1, fg="white", bg="black", relief="flat", command=g1_2)
    a4.place(x=410, y=450)
    
def g1_1():
    global score_count
    global x
    if b1==count_plus(b2):
        winsound.PlaySound("딩동.wav", winsound.SND_FILENAME)
        a5=Label(fr[x+1], text="정답입니다 !\n버튼을 누르면 다음 판으로 넘어갑니다.", font=font1)
        a5.place(x=140, y=500)
        a10=Label(fr[x+1], image=img2)
        a10.place(x=300, y=200)
        a30=Button(fr[x+1], font=font1, text="다음 판으로", command=g1_r, bg="white", fg="black")
        a30.place(x=280, y=600)
        x+=2
        score_count+=1
    else :
        winsound.PlaySound("땡.wav", winsound.SND_FILENAME)
        a5=Label(fr[x+1], text="오답입니다. 뒷면이였네요 !\n버튼을 누르면 다음 판으로 넘어갑니다, 힘내세요 !", font=font1)
        a5.place(x=80, y=500)
        a10=Label(fr[x+1], image=img3)
        a10.place(x=300, y=200)
        a30=Button(fr[x+1], font=font1, text="다음 판으로", command=g1_r, bg="white", fg="black")
        a30.place(x=280, y=600)
        x+=2

def g1_2():
    global score_count
    global x
    if b1==count_plus(b2+1):
        winsound.PlaySound("딩동.wav", winsound.SND_FILENAME)
        a5=Label(fr[x+1], text="정답입니다 !\n버튼을 누르면 다음 판으로 넘어갑니다.", font=font1)
        a5.place(x=140, y=500)
        a10=Label(fr[x+1], image=img3)
        a10.place(x=300, y=200)
        a30=Button(fr[x+1], font=font1, text="다음 판으로", command=g1_r, bg="white", fg="black")
        a30.place(x=280, y=600)
        x+=2
        score_count+=1
    else :
        winsound.PlaySound("땡.wav", winsound.SND_FILENAME)
        a5=Label(fr[x+1], text="오답입니다. 앞면이였네요 !\n버튼을 누르면 다음 판으로 넘어갑니다, 힘내세요 !", font=font1)
        a5.place(x=80, y=500)
        a10=Label(fr[x+1], image=img2)
        a10.place(x=300, y=200)
        a30=Button(fr[x+1], font=font1, text="다음 판으로", command=g1_r, bg="white", fg="black")
        a30.place(x=280, y=600)
        x+=2

def g2_r():
    global k1
    fr[0].destroy()
    global k
    if k==3:
        fr[0].destroy()
        fr3[1].destroy()
    elif k==1:
        fr[0].destroy()
        fr[20].destroy()
    if k1==3:
        del select[1]
    elif k1==2 and k==3:
        del select[1]
    elif k1==2 and k==1:
        del select[0]
    elif k1==2 and k==0:
        del select[1]
    k1-=1
    k=2
    global x
    fr2[0].pack()
    inf=Label(fr2[0], text="이번 게임은 1~20 사이의 랜덤한 숫자 맞추기 입니다.\n\n기회는 총 다섯번 주어집니다.", font=font1, bg="gray", fg="white")
    inf.place(x=90, y=100)
    a1=Label(fr2[0], text="엔터키를 누르면 랜덤한 숫자가 정해집니다.", font=font1, bg="gray", fg="white")    
    a1.place(x=150, y=550)
    a.bind("<Return>", g2)

def g2(self):
    winsound.PlaySound("숫자.wav", winsound.SND_FILENAME)
    global c1
    global d1
    global j1
    j1=0
    fr2[0].destroy()
    fr2[1].pack()
    d1=random.randint(1, 20)
    c1=Entry(fr2[1])
    c1.place(x=290, y=300)
    c2=Label(fr2[1], text="1~20사이의 정수를 입력해보세요", font=font4, bg="gray")
    c2.place(x=180, y=200)
    c3=Button(fr2[1], text="입력", font=font3, command=GetEntText)
    c3.place(x=440, y=295)

def GetEntText():
    select_1=random.choice(select)
    global main_count
    global game_count
    global j1
    global k1
    n1=c1.get()
    d2=int(n1)
    if d1==d2:
        main_count+=1
        game_count+=1
        msgbox.showinfo("결과", "정답입니다! 축하드려요\n버튼을 누르면 다음게임으로 넘어갑니다.")
        c4=Button(fr2[1], text="다음 게임으로", font=font1, bg="gray", fg="black", command=select_1)
        c4.place(x=290, y=450)
        if game_count==3:
            fr2[1].destroy()
            end1.place(x=290, y=450)
    elif d1>d2:
        j1+=1
        msgbox.showinfo("결과", "Up ! 다시 입력하세요.")
    elif d1<d2:
        j1+=1
        msgbox.showinfo("결과", "Down ! 다시 입력하세요.")
    if j1==5:
        game_count+=1
        msgbox.showinfo("결과", "아쉽게도 기회를 다 사용하셨네요\n이번 게임에서 패배하셨습니다.\n버튼을 누르면 다음게임으로 넘어갑니다.")
        c4=Button(fr2[1], text="다음 게임으로", font=font1, bg="gray", fg="black", command=select_1)
        c4.place(x=290, y=450)
        if game_count==3:
            fr2[1].destroy()
            end1.place(x=290, y=450)

def g3_r():
    global k1
    fr[0].destroy()
    global k
    if k==2:
        fr[0].destroy()
        fr2[1].destroy()
    elif k==1:
        fr[0].destroy()
        fr[20].destroy()
    k=3
    if k1==3:
        del select[2]
    elif k1==2:
        del select[1]
    k1-=1
    global o
    o=0
    fr3[0].pack()
    inf=Label(fr3[0], text="이번 게임은 세마리의 달팽이 경주 게임 입니다.\n\n아래의 달팽이들 중 한마리를 클릭해 골라주세요", font=font1, bg="white", fg="green")
    inf.place(x=90, y=100)
    w1=Button(fr3[0], image=img4, relief="flat", command=lambda:[g3(count_plus(o))])
    w1.place(x=80, y=370)
    w2=Button(fr3[0], image=img5, relief="flat", command=lambda:[g3(count_plus(o+1))])
    w2.place(x=315, y=370)
    w3=Button(fr3[0], image=img6, relief="flat", command=lambda:[g3(count_plus(o+2))])
    w3.place(x=550, y=370)
    q1=Label(fr3[0], text="달팽이를 정하면 경주가 시작됩니다.", font=font1, bg="white", fg="green")    
    q1.place(x=160, y=550)

def g3(t1):
    winsound.PlaySound("달팽이.wav", winsound.SND_FILENAME)
    select_1=random.choice(select)
    global k1
    global main_count
    global game_count
    result=0
    sum1=0
    sum2=0
    sum3=0
    fr3[0].destroy()
    canvas=Canvas(a, width=750, height=750, bg="white")
    canvas.pack()
    e1=canvas.create_image(0, 90, anchor = NW, image = img4)
    e2=canvas.create_image(0, 320, anchor = NW, image = img5)
    e3=canvas.create_image(0, 550, anchor = NW, image = img6)

    for z in range(1, 100):
        f1=random.randint(20,80)
        canvas.move(e1, f1, 0)
        sum1+=f1
        if sum1>=570:
            result=1
            if t1==result:
                main_count+=1
                game_count+=1
                msgbox.showinfo("결과", "축하드립니다 !\n당신의 달팽이가 1등입니다!")
                canvas.destroy()
                fr3[1].pack()
                q2=Button(fr3[1], text="다음 게임으로", font=font1, bg="gray", fg="black", command=select_1)
                q2.place(x=290, y=450)
                if game_count==3:
                    fr3[1].destroy()
                    end1.place(x=290, y=450)
            else :
                game_count+=1
                msgbox.showinfo("결과", "안타깝네요.\n당신의 달팽이는 1등에 실패했습니다.")
                canvas.destroy()
                fr3[1].pack()
                q2=Button(fr3[1], text="다음 게임으로", font=font1, bg="gray", fg="black", command=select_1)
                q2.place(x=290, y=450)
                if game_count==3:
                    fr3[1].destroy()
                    end1.place(x=290, y=450)
            break
        f2=random.randint(20,80)
        canvas.move(e2, f2, 0)
        sum2+=f2
        if sum2>=570:
            result=2
            if t1==result:
                main_count+=1
                game_count+=1
                msgbox.showinfo("결과", "축하드립니다 !\n당신의 달팽이가 1등입니다!")
                canvas.destroy()
                fr3[1].pack()
                q2=Button(fr3[1], text="다음 게임으로", font=font1, bg="gray", fg="black", command=select_1)
                q2.place(x=290, y=450)
                if game_count==3:
                    fr3[1].destroy()
                    end1.place(x=290, y=450)
            else :
                game_count+=1
                msgbox.showinfo("결과", "안타깝네요.\n당신의 달팽이는 1등에 실패했습니다.")
                canvas.destroy()
                fr3[1].pack()
                q2=Button(fr3[1], text="다음 게임으로", font=font1, bg="gray", fg="black", command=select_1)
                q2.place(x=290, y=450)
                if game_count==3:
                    fr3[1].destroy()
                    end1.place(x=290, y=450)
            break
        f3=random.randint(20,80)
        canvas.move(e3, f3, 0)
        sum3+=f3
        a.update()
        time.sleep(0.35)
        if sum3>=570:
            result=3
            if t1==result:
                main_count+=1
                game_count+=1
                canvas.destroy()
                fr3[1].pack()
                msgbox.showinfo("결과", "축하드립니다 !\n당신의 달팽이가 1등입니다!")
                q2=Button(fr3[1], text="다음 게임으로", font=font1, bg="gray", fg="black", command=select_1)
                q2.place(x=290, y=450)
                if game_count==3:
                    fr3[1].destroy()
                    end1.place(x=290, y=450)
            else :
                game_count+=1
                canvas.destroy()
                fr3[1].pack()
                msgbox.showinfo("결과", "안타깝네요.\n당신의 달팽이는 1등에 실패했습니다.")
                q2=Button(fr3[1], text="다음 게임으로", font=font1, bg="gray", fg="black", command=select_1)
                q2.place(x=290, y=450)
                if game_count==3:
                    fr3[1].destroy()
                    end1.place(x=290, y=450)
            break

select=[g1_r, g2_r, g3_r]
select_1=random.choice(select)
main1=Label(fr[0], font=font5, bg="gray", text="미니게임 모음집", fg="yellow2")
main1.place(x=185, y=170)
main2=Label(fr[0], font=font6, bg="gray", text="2271271 최현우", fg="snow2")
main2.place(x=470, y=240)
a.update()
winsound.PlaySound("메인화면-뱀서.wav", winsound.SND_FILENAME)
start=Button(fr[0], text="버튼을 누르면 시작", fg="white", font=font1, bg="black", relief="flat")
start.config(command=select_1)
start.place(x=260, y=500)

a.mainloop()
