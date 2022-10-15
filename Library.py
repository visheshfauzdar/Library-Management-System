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
        headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        headingLabel = Label(headingFrame1, text="Welcome to \n MEC Library Hyderabad", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        btn1 = Button(self.root,text="Add Book Details",bg='black', fg='white')
        btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
        btn2 = Button(self.root,text="Delete Book",bg='black', fg='white')
        btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
        btn3 = Button(self.root,text="View Book List",bg='black', fg='white',command=self.books_page)
        btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
        btn4 = Button(self.root,text="Issuer Details",bg='black', fg='white',command=self.member_page)
        btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
        btn5 = Button(self.root,text="Transactions",bg='black', fg='white',command=self.transaction_page)
        btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

       
    def transaction_page(self):
        window=Tk()
        window.title("Transaction Page")
        window.geometry("800x800")
        window.config(bg="powderblue")
        headingFrame1 = Frame(window,bg="#FFBB00",bd=5)
        headingFrame1.place(relx=0.35,rely=0.1,relwidth=0.3,relheight=0.1)
        headingLabel = Label(headingFrame1, text="Transactions", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
       
        labelFrame = Frame(window,bg='black')
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5) 
        lb1 = Label(labelFrame,text="Book Name", bg='black', fg='powderblue')
        lb1.place(relx=0.05,rely=0.2)
        
        inf1 = Label(labelFrame,text="Issuer ",bg="black",fg="powderblue")
        inf1.place(relx=0.40,rely=0.2)
    
        inf1 = Label(labelFrame,text="Payment Status ",bg="black",fg="powderblue")
        inf1.place(relx=0.75,rely=0.2)

        admin_Submit=Button(window,text="Back to HomePage")
        admin_Submit.place(x=300,y=400)
    def member_page(self):
       window=Tk()
       window.title("Members Page")
       window.geometry("800x800")
       window.config(bg="powderblue")
      
       headingFrame1 = Frame(window,bg="#FFBB00",bd=5)
       headingFrame1.place(relx=0.35,rely=0.1,relwidth=0.3,relheight=0.1)
       headingLabel = Label(headingFrame1, text="Members Page", bg='black', fg='white', font=('Courier',15))
       headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
       
       labelFrame = Frame(window,bg='black')
       labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5) 
       lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
       lb1.place(relx=0.05,rely=0.2)
        
       inf1 = Entry(labelFrame)
       inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
       lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
       lb2.place(relx=0.05,rely=0.4)
        
       inf2 = Entry(labelFrame)
       inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
       issueBtn = Button(window,text="Issue",bg='#d1ccc0', fg='black')
       issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
       quitBtn = Button(window,text="Quit",bg='#aaa69d', fg='black')
       quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    def books_page(self):
        window=Tk()
        window.title("Books Page")
        window.geometry("800x800")
        window.config(bg="powderblue")
       
        headingFrame1 = Frame(window,bg="#FFBB00",bd=5)
        headingFrame1.place(relx=0.35,rely=0.08,relwidth=0.3,relheight=0.1)
        headingLabel = Label(headingFrame1, text="View Books List", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        search_books=Label(window,text="Search ",bg="powderblue",font=("bold","10"))
        search_books.place(x=270,y=200)
        search_box=Entry(window)
        search_box.place(relwidth=0.25,x=330,y=200)
        
        labelFrame = Frame(window,bg='black')
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5) 
        lb1 = Label(labelFrame,text="Book Id", bg='black', fg='powderblue')
        lb1.place(relx=0.05,rely=0.2)
        
        inf1 = Label(labelFrame,text="Book Name",bg="black",fg="powderblue")
        inf1.place(relx=0.40,rely=0.2)
    
        inf1 = Label(labelFrame,text="Publisher ",bg="black",fg="powderblue")
        inf1.place(relx=0.75,rely=0.2)
root=Tk()
obj=Multiple(root)
root.mainloop()