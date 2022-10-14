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
        books_button=Button(self.root,text="Books",command=self.transaction_page)
        books_button.place(x=400,y=120)
        members_button=Button(self.root,text="Members",command=self.transaction_page)
        members_button.place(x=400,y=170)
        transaction_button=Button(self.root,text="Transaction",command=self.transaction_page)
        transaction_button.place(x=400,y=220)
    def transaction_page(self):
        window=Tk()
        window.title("Transaction Page")
        window.geometry("800x800")
        window.config(bg="powderblue")
        title=Label(window,text="Transaction Page",bg="powderblue",font=("bold",'20'))
        title.place(x=200,y=10)
        book_name_label=Label(window,text="Book Name : ",bg="powderblue",font=('bold','15'))
        book_name_label.place(x=20,y=80)

        author_label=Label(window,text="Author Name : ",bg="powderblue",font=('bold','15'))
        author_label.place(x=20,y=120)
    
        qty_label=Label(window,text="Quantity : ",bg="powderblue",font=('bold','15'))
        qty_label.place(x=20,y=160)

        book_entry=Entry(window)
        book_entry.place(x=150,y=80)

        author_entry=Entry(window)
        author_entry.place(x=150,y=120)

        qty_entry=Entry(window)
        qty_entry.place(x=150,y=160)

        admin_Submit=Button(window,text="Submt")
        admin_Submit.place(x=120,y=200)
    
root=Tk()
obj=Multiple(root)
root.mainloop()