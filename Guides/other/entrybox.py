from tkinter import *
def display():
   if(x.get()):
       print("I like Python")
   else:
       print("I don't like Python")

window = Tk()

x = IntVar()

python_photo = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\Python_color.png")

checkbox = Checkbutton(window,
                      text='Python',
                      variable=x,
                      onvalue=True,
                      offvalue=False,
                      command=display,
                      font=('Arial',20),
                      fg='#00FF00',
                      bg='#000000',
                      activeforeground='#0000FF',
                      activebackground='#000000',
                      padx=25,
                      pady=10,
                      width=200,
                      height=50,
                      anchor='w',
                      image=python_photo,
                      compound='left')
checkbox.pack()

window.mainloop()