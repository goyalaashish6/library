import os
import welcome
import librarian
import sys
def main(x):
    os.system('cls')
    welcome.func()
    print("\nSearch based on the following attributes:-\n")
    inp=raw_input("\n1.Author name and Book Title[Recommended]\n\n2.Author name\n\n3.BookTitle\n\n4.Book Category\n\n5.Back\n\n6.Exit")
    if inp=='1':
        main1(x)
    elif inp=='2':
        main2(x)
    elif inp=='3':
        main3(x)
    elif inp=='4':
        main4(x)
    elif inp=='5':
        if (x==1):
            os.system('cls')
            librarian.main1()
        else:
            os.system('cls')
            librarian.main2()
    elif inp=='6':
        sys.exit()
    else:
        print "\nWrong choice\n"
        main(x)
        
def main1(x):
    os.system('cls')
    welcome.func()
    aut=raw_input("\nType the author name with alteast 3 characters\n")
    if len(aut)<3:
        print("\nToo less Characters for an efficient searching...\nTry again")
        main1(x)
    tit=raw_input("\nType the book title with alteast 3 characters\n")
    if len(tit)<3:
        print("Too less Characters for an efficient searching...Try again")
        main1(x)
    f=open("/Python27/libr/books.txt")
    flag=0
    while True:
        os.system('cls')
        welcome.func()
        w=f.readline()
        if(len(w)==0):
            break
        b=eval(w)   
        if(b[3].find(aut)!=-1 and b[1].find(tit)!=-1 and b[8]=='#'):
            print "\nBook Available in the library\n" "\nBook Serial no ="+b[0]+"\nBook Title ="+b[1]+"\nCategory ="+b[2]+"\nBook Author ="+b[3]+"\nBook Edition ="+str(b[5])+"\nBook Publisher ="+str(b[7])
            inp1=raw_input("\nIs this the book which you where looking for?\nPress 1 for yes  else any other key to continue searching\n")
            if inp1=='1':
                flag=1
                break
        elif(b[3].find(aut)!=-1 and b[1].find(tit)!=-1 and b[8]!='#'):
            print "\nBook is present in the library but has been allocated to some one else\n"
            inp1=raw_input("\nTo stop searching press 1\n else any other key to continue searching\n")
            if inp1=='1':
                flag=1
                break
            else:
                main(x)
    f.close()
    if(flag==0):
        q=raw_input("\n\nSorry\nThere are no books available based on your query\nPress 1 to Try Again \nAny other key to go back\n")
        if(q=='1'):
            main1(x)
        else:
            if (x==1):
                os.system('cls')
                librarian.main1()
            else:
                os.system('cls')
                librarian.main2()
    elif(flag==1):
        if (x==1):
            os.system('cls')
            librarian.main1()
        else:
            os.system('cls')
            librarian.main2()
def main2(x):
    os.system('cls')
    welcome.func()
    aut=raw_input("\nType the author name with alteast 3 characters\n")
    if len(aut)<3:
        print("\nToo less Characters for an efficient searching...\nTry again")
        main2(x)
    f=open("/Python27/libr/books.txt")
    flag=0
    while True:
        os.system('cls')
        welcome.func()
        w=f.readline()
        if(len(w)==0):
            break
        b=eval(w)   
        if(b[3].find(aut)!=-1 and b[8]=='#'):
            print "\n\nBook Available\n" "\nBook Serial no ="+b[0]+"\nBook Title ="+b[1]+"\nCategory ="+b[2]+"\nBook Author ="+b[3]+"\nBook Edition ="+str(b[5])+"\nBook Publisher ="+str(b[7])
            inp1=raw_input("\nIs this the book which you where looking for?\nPress 1 for yes  else any other key to continue searching\n")
            if inp1=='1':
                flag=1
                break
    f.close()
    if(flag==0):
        q=raw_input("\nSorry\nThere are no books available based on your query\nPress 1 to Try Again \nAny other key to go back\n")
        if(q=='1'):
            main2(x)
        else:
            if (x==1):
                os.system('cls')
                librarian.main1()
            else:
                os.system('cls')
                librarian.main2()
    elif(flag==1):
        if (x==1):
            os.system('cls')
            librarian.main1()
        else:
            os.system('cls')
            librarian.main2()
       
            
        
                       

def main3(x):  
    os.system('cls')
    welcome.func()
    tit=raw_input("\nType the book title with alteast 3 characters\n")
    if len(tit)<3:
        print("Too less Characters for an efficient searching...Try again")
        main3(x)
    f=open("/Python27/libr/books.txt")
    flag=0
    while True:
        os.system('cls')
        welcome.func()
        w=f.readline()
        if(len(w)==0):
            break
        b=eval(w)   
        if(b[1].find(tit)!=-1 and b[8]=='#'):
            print "\n\nBook Available\n" "\nBook Serial no ="+b[0]+"\nBook Title ="+b[1]+"\nCategory ="+b[2]+"\nBook Author ="+b[3]+"\nBook Edition ="+str(b[5])+"\nBook Publisher ="+str(b[7])
            inp1=raw_input("\nIs this the book which you were looking for?\nPress 1 for yes \nAny other key to continue searching\n")
            if inp1=='1':
                flag=1
                break
    f.close()
    if(flag==0): 
       q=raw_input("Sorry\nThere are no books available based on your query\nPress 1 to Try Again\n Any other key to go back\n")
       if(q=='1'):
            main3(x)
       else:
            if (x==1):
                os.system('cls')
                librarian.main1()
            else:
                os.system('cls')
                librarian.main2()
    elif(flag==1):
        if (x==1):
            os.system('cls')
            librarian.main1()
        else:
            os.system('cls')
            librarian.main2()

def main4(x):
    os.system('cls')
    welcome.func()
    cat=raw_input("\nType the category(minimum 5 characters)\n")
    if len(cat)<5:
        print("Too less Characters for an efficient searching...Try again")
        main4(x)
    f=open("/Python27/libr/books.txt")
    flag=0
    while True:
        os.system('cls')
        welcome.func()
        w=f.readline()
        if(len(w)==0):
            break
        b=eval(w)   
        if(b[2].find(cat)!=-1 and b[8]=='#'):
            print "\n\nBook Available\n" "\nBook Serial no ="+b[0]+"\nBook Title ="+b[1]+"\nCategory ="+b[2]+"\nBook Author ="+b[3]+"\nBook Edition ="+str(b[5])+"\nBook Publisher ="+str(b[7])
            inp1=raw_input("\n\nIs this the book which you where looking for?\nPress 1 for yes \nAny other key to continue searching\n")
            if inp1=='1':
                flag=1
                break
    f.close()
    if(flag==0):
        q=raw_input("\nSorry\nThere are no books available based on your query\nPress 1 to Try Again or any other key to go back\n")
        if(q=='1'):
            main4(x)
        else:
            if (x==1):
                os.system('cls')
                librarian.main1()
            else:
                os.system('cls')
                librarian.main2()

    elif(flag==1):
        if (x==1):
            os.system('cls')
            librarian.main1()
        else:
            os.system('cls')
            librarian.main2()

