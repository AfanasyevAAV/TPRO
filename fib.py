from tkinter import * 
from tkinter import messagebox


def clicked(): 
    res = txt.get()
    if int(res)==1:
        fibonacci=[0]
    elif int(res)==2:
        fibonacci=[0,1]
    else:
        fibonacci=[0,1,1]
        for parts in range(1,int(res)-2):
            addative=fibonacci[-2]+fibonacci[-1]
            fibonacci.append(addative)

    messagebox.showinfo(title='GUI', message=(fibonacci))

def singel_num():
    kek = xtx.get()
    if int(kek)==1:
        fibonacci=0
    elif int(kek)==0:
            fibonacci='Nothing'
    elif int(kek)==2:
        fibonacci=1
    else:
        fibonacci=[0,1,1]
        for parts in range(1,int(kek)-2):
            addative=fibonacci[-2]+fibonacci[-1]
            fibonacci.append(addative)

    messagebox.showinfo(title='GUI', message=(fibonacci[int(kek)-1]))

def amount():
    res = xxt.get()
    if int(res)==1:
        fibonacci=0
    elif int(res)==2:
        fibonacci=[0.1]
        agerage=.5
    else:
        fibonacci=[0,1,1]
        for parts in range(1,int(res)-2):
            addative=fibonacci[-2]+fibonacci[-1]
            fibonacci.append(addative)
        average=sum(fibonacci)/len(fibonacci)

    messagebox.showinfo(title='GUI', message=(average))


window = Tk()
window['bg']= 'grey90'
window.wm_attributes('-alpha',1)
window.title("Фибоначчи")  
window.geometry('450x120')
canvas = Canvas (window,height=500,width=500)


gdg = Label(window,bg="grey90", text="Вывести на экран столько элементов ряда Фибоначчи")  
gdg.grid(column=1, row=1)



btn = Button(window, text="выяснить!", command=clicked )  
btn.grid(column=3, row=2)
txt = Entry(window,width=10 )  
txt.grid(column=2, row=2)
lbl = Label(window,bg="grey90", text="Полная строка Фибоначчи")  
lbl.grid(column=1, row=2)


tnb = Button(window, text="выяснить!", command=singel_num )  
tnb.grid(column=3, row=3) 
xtx = Entry(window,width=10 )  
xtx.grid(column=2, row=3)
blb = Label(window,bg="grey90", text="Только единичное число")  
blb.grid(column=1, row=3)


ntb = Button(window, text="выяснить!", command=amount )  
ntb.grid(column=3, row=4) 
xxt = Entry(window,width=10 )  
xxt.grid(column=2, row=4)
bpb = Label(window,bg="grey90", text="Среднее значение части")  
bpb.grid(column=1, row=4)


window.mainloop()


