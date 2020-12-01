from tkinter import * 
from tkinter import messagebox


  
  
def clicked():  
    res = txt.get()
    a = res.count('?')
    b = res.count('!')
    c = res.count('.')
    messagebox.showinfo(title='GUI', message=('В вашем тексте', a+b+c ,'предложений'))
    
  
  
window = Tk()
window.wm_attributes('-alpha',1)
window.title("Считыватель")  
window.geometry('320x100')



gon = Label(window)  
gon.grid(column=0, row=0)

lbl = Label(window, text="Ваш текст")  
lbl.grid(column=0, row=9)

txt = Entry(window,width=30 )  
txt.grid(column=1, row=9)


btn = Button(window, text="ок", command=clicked)  
btn.grid(column=3, row=9) 

window.mainloop()


