class Library:

    def __init__(self,ListOfBooks):
        self.books=ListOfBooks


    def AvilableBooks(self):
        print("This Avilable Books in Library Are Following Below")
        for book in self.books:
            print("-->>  ",book)

    def BooksIssue(self,BookName):
        if BookName in self.books:
            print(f"A book Name ----{BookName}----is Issue ")
            self.books.remove(BookName)
        else:
            print("Sorry Dear this book is Already issued to someone please contact after some days may be book is avilable")

    def BookReturn(self,BookName):
        
        self.books.append(BookName)
        print(f"A book Name----{BookName}----is Returned")
        print("Thank you for using this library Visit Again")






class Student:
    def Details(self):

        self.id=int(input("enter the id number: "))
        self.name=input("enter your name: ")
        self.branch=input("enter your branch: ")
        
        


    def requstBooks(self):
       
        self.book=input("Enter the book You want to Issue: ")
        return self.book
    
    def retrunBooks(self):
       
        self.book=input("Enter the book You want to return: ")

        return self.book
       

        




if __name__ == "__main__":
    EngneeringBooks=Library(["Let Us C","Java","Python","DBMS","Fundamentals of Computer"])
    student=Student()
   
    while True:
        student.Details()
        welcomemsg=''' ======****** HElLO EveryOne Welcome to the Central Engeering Libaray=====*****
            
            1 For Avilable Books
            2 For Book Issue
            3 For Book Return
            4 For Exit'''
        print(welcomemsg)
        a=int(input("Enter Your Choice Please read the Instructions: "))
        
        if a == 1:
            EngneeringBooks.AvilableBooks()
        elif a == 2:
            EngneeringBooks.BooksIssue(student.requstBooks())
        elif a == 3:
            EngneeringBooks.BookReturn(student.retrunBooks())
        elif a == 4:
            print("Thank You For using this Library I hope You get Your books!! Have a Nice Day")
            exit()
        else:
            print("Invalid Number----:::::----Please read the Instructions Carefully")







