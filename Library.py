from tkinter import *
from turtle import title
class Multiple():
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x900")
        self.root.title("Library Management System")
        self.root.config(bg="powderblue")
        title=Label(self.root,text="Home Page",bg="powderblue",font=("bold",'25'))
        title.pack()
        admin_button=Button(self.root,text="Admin",command=self.admin_page)
        admin_button.place(x=150,y=120)
    def admin_page(self):
        window=Tk()
        window.title("Admin Page")
        window.geometry("800x800")
        window.config(bg="powderblue")

        book_name_label=Label(window,text="Book Name : ",bg="powderblue",font=('bold','15'))
        book_name_label.place(x=20,y=40)

        author_label=Label(window,text="Author Name : ",bg="powderblue",font=('bold','15'))
        author_label.place(x=20,y=80)
    
        qty_label=Label(window,text="Quantity : ",bg="powderblue",font=('bold','15'))
        qty_label.place(x=20,y=120)

        book_entry=Entry(window)
        book_entry.place(x=150,y=40)

        author_entry=Entry(window)
        author_entry.place(x=150,y=80)

        qty_entry=Entry(window)
        qty_entry.place(x=150,y=120)

        admin_Submit=Button(window,text="Submt")
        admin_Submit.place(x=120,y=200)
    
root=Tk()
obj=Multiple(root)
root.mainloop()