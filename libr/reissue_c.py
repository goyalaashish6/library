import datetime
import return_c
import librarian
import sys
import os
import welcome
def main(x):
    os.system('cls')
    welcome.func()
    sid=raw_input("Enter the book ID to be reissued")
    f=open("/Python27/libr/books.txt")
    flag=0
    l=[]
    usn='0'
    while True:
        w=f.readline()
        if(len(w)==0):
            break
        b=eval(w)
        if(b[0]==sid and b[8]!='#'):
            flag=1
            usn=b[8]      
    if flag==0:
        f.close()
        print"This book was never been issued or wrong book ID"
        inp=raw_input("\nPress 1 for typing the book id again\nAny other key to go back")
        if(inp=='1'):
            main(x)
        else:
            if (x==1): 
                os.system('cls') 
                librarian.main1()
            else:
                os.system('cls') 
                librarian.main2()
    f.close()
    print"\nThe book has beeen re issued\n"
    g=open("/Python27/libr/stud_db1.txt")
    while True:
        w=g.readline()
        if(len(w)==0):
            break
        dic=eval(w)
        if dic.has_key(usn):
            for i in dic[usn]:
                if(isinstance(i,int)==False):
                    if i[0]==sid:
                        d1=datetime.date.today()# date of return
                        i[1]=str(i[1])              # date of issue 
                        d2=i[1].split('-')               
                        d3=''
                        for h in d2:
                            d3=d3+h
                        d4=datetime.datetime.strptime(d3, '%Y%m%d').date()
                        d5=d1-d4
                        #print d5
                        if d5==datetime.timedelta(0):
                            days=0
                        else:
                            days=int(str(d5).split()[0])
                        if(days>15):
                            print("\nStudent has a fine of "+str(days-15))
                            dic[usn][3]+=(days-15)
                        i[1]=str(d1)
        l.append(str(dic))
    g.close()
    h=open("/Python27/libr/stud_db1.txt","w")
    h.write(l[0])
    for i in l[1:]:
        h.write("\n"+i)
    h.close()
    q=raw_input("\n1 to go back or any other key to exit")
    if(q=='1'):
        if (x==1):
            os.system('cls')
            librarian.main1()
        else:
            os.system('cls')
            librarian.main2()
    else:
        sys.exit()



