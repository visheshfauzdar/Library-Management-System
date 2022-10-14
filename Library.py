from pydoc import text
from re import search
from tkinter import *
from turtle import title
class Multiple():
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x700")
        self.root.title("Library Management System")
        self.root.config(bg="powderblue")
        title=Label(self.root,text="Admin Page",bg="powderblue",font=("bold",'20'))
        title.pack()
        books_button=Button(self.root,text="Books",command=self.books_page)
        books_button.place(x=200,y=120)
        members_button=Button(self.root,text="Members",command=self.member_page)
        members_button.place(x=400,y=120)
        transaction_button=Button(self.root,text="Transaction",command=self.transaction_page)
        transaction_button.place(x=600,y=120)
    def transaction_page(self):
        window=Tk()
        window.title("Transaction Page")
        window.geometry("800x800")
        window.config(bg="powderblue")
        title=Label(window,text="Transaction Page",bg="powderblue",font=("bold",'20'))
        title.place(x=300,y=10)
        book_name_label=Label(window,text="Book Name ",bg="powderblue",font=('bold','12'))
        book_name_label.place(x=60,y=80)

        author_label=Label(window,text="Issuer ",bg="powderblue",font=('bold','12'))
        author_label.place(x=300,y=80)
    
        qty_label=Label(window,text="Payment Status ",bg="powderblue",font=('bold','12'))
        qty_label.place(x=460,y=80)

        admin_Submit=Button(window,text="Back to HomePage")
        admin_Submit.place(x=300,y=200)
    def member_page(self):
       window=Tk()
       window.title("Members Page")
       window.geometry("800x800")
       window.config(bg="powderblue")
       title=Label(window,text="Member Page",bg="powderblue",font=("bold",'20'))
       title.place(x=300,y=10)
    def books_page(self):
        window=Tk()
        window.title("Books Page")
        window.geometry("800x800")
        window.config(bg="powderblue")
        title=Label(window,text="Books Page",bg="powderblue",font=("bold",'20'))
        title.place(x=300,y=10)
        search_books=Label(window,text="Search ",bg="powderblue",font=("bold","10"))
        search_books.place(x=200,y=70)
        search_box=Entry(window)
        search_box.place(x=290,y=70)
root=Tk()
obj=Multiple(root)
root.mainloop()