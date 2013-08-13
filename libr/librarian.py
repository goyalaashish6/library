import searching
import issue_c
import return_c
import final_fine_eval
import datetime
import getpass
import os
import final_collect_fine
import reissue_c
import add_book
import sys
import welcome
class lib:
    def search(self,x):
        searching.main(x)   
    def issue(self,x):
        issue_c.main(x)         
    def renew(self,x):
        reissue_c.main(x)
    def retrn(self,x):
        flag=0
        os.system('cls')
        welcome.func()
        bid=raw_input("\nEnter the book ID to be returned\n")
        f=open("/Python27/libr/books.txt")
        while True:
            w=f.readline()
            if(len(w)==0):
                break
            b=eval(w)
            if(b[0]==bid and b[8]!='#'):
                flag=1
                break
        if flag==0:
            print"\nEither this book doesnt exist in the library or this book has not been isssued to anyone\n"
            inp=raw_input("\nPress 1 for typing the book id again\nAny other key to go back")
            if(inp=='1'):
                self.retrn(x)
            else:
                if (x==1): 
                    os.system('cls')
                    main1()
                else:
                    os.system('cls')
                    main2()
        f.close()
        d1=datetime.date.today()
        return_c.main(bid,d1,x)
    def add(self,x):
        add_book.main(x)
    def exi(self):
        sys.exit()
class sup_lib(lib):  
    def addmem(self,x):
        y=0
        l=[]
        g=open("/Python27/libr/librarians.txt")
        a=raw_input("\nEnter the Unique login ID\n")
        while True:
            w=g.readline()
            if(len(w)==0):
                break
            d=eval(w)
            l.append(d)
            if d[0]==a:
                y=1           
        g.close()        
        if y==1:
            inp=raw_input("\nThis login name already Exists\nPress 1 to select a new login name\nAny other key to go back")
            if inp=='1':
                self.addmem(y)
            else:
                if (x==1):
                    os.system('cls')
                    main1()
                else:
                    os.system('cls')
                    main2()
        f=open("/Python27/libr/librarians.txt","w")
        print("\nLogin name is Valid\nType a password\n")
        password=getpass.getpass()
        print("\n"+a+" has been added as a memeber of PESIT South Campus Library\n")
        y=[a,password]
        l.append(y)
        f.write(str(l[0]))
        for i in l[1:]:
            f.write("\n"+str(i))
        f.close()
        inp=raw_input("\nType 1 to enter another\nElse anything else to go back\n")
        if inp=='1':
            self.addmem(x)
        else:  
          # if (x==1):                   
         #      os.system('cls')
           #    main1()
           #else:
               os.system('cls')
               main2()
   
                   
    def gendue(self,x):
        final_fine_eval.main(x)
    def finecollect(self,x):
        final_collect_fine.main(x)       
def main1():
    x=1
    obj=lib()
    os.system('cls')
    welcome.func()
    print("\nWelcome Librarian ")
    a=raw_input("\n\n1.SEARCH A BOOK\n\n2.ISSUE A BOOK\n\n3.REISSUE A BOOK\n\n4.RETURN A BOOK\n\n5.Add a Book\n\n6.Exit\n")
    if a=='1':
        obj.search(x)
    elif a=='2':
        obj.issue(x)
    elif a=='3':
        obj.renew(x)
    elif a=='4':
        obj.retrn(x)
    elif a=='5':
        obj.add(x)
    elif a=='6':
        obj.exi()
    else:
        print "\nWrong Entry\n"
        main1()
def main2():
    x=2
    obj=sup_lib()
    os.system('cls')
    welcome.func()
    print("\nWelcome Chief Librarian\n")
    a=raw_input("\n1.SEARCH A BOOK\n\n2.ISSUE A BOOK\n\n3.REISSUE A BOOK\n\n4.RETURN A BOOK\n\n5.ADD A NEW LIBRARIAN\n\n6.Generate the list of the students with due books\n\n7.Generate the list of students with fine\n\n8.Add a Book\n\n9.Exit\n")
    if a=='1':
        obj.search(x)
    elif a=='2':
        obj.issue(x)
    elif a=='3':
        obj.renew(x)
    elif a=='4':
        obj.retrn(x)
    elif a=='5':
        obj.addmem(x)
    elif a=='6':
        obj.gendue(x)
    elif a=='7':
        obj.finecollect(x)
    elif a=='8':
        obj.add(x)
    elif a=='9':
        obj.exi()
    else:
        print"\nWrong Entry\n"
        main2()
