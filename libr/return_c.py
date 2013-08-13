import sys
import os
import datetime
import librarian
def main(bid,d1,x):
    f=open("/Python27/libr/books.txt")
    flag=0
    newlines=[]
    while True:
        w=f.readline()
        if(len(w)==0):
            break
        b=eval(w)
        if(b[0]==bid and b[8]!='#'):
            book_cost=b[4]
            flag=1
            break
        newlines.append(b)
   
    usn=b[8]
    b[8]='#'
    newlines.append(b)
    while True:
        q=f.readline()
        if len(q)==0:
            break
        q1=eval(q)
        newlines.append(q1)
    f.close()
    f=open("/Python27/libr/books.txt","w")
    f.write(str(newlines[0]))
    for k in newlines[1:]:
        f.write("\n"+str(k))                                
    f.close()
    newlines=[]
    f=open("/Python27/libr/stud_db1.txt")
    while True:
        w=f.readline()
        if(len(w)==0):
            break
        dic=eval(w)
        if dic.has_key(usn):
            for i in dic[usn]:
                if i[0]==bid:
                    d1=datetime.date.today()# date of return
                                 # date of issue
                    i[1]=str(i[1])  
                    d2=i[1].split('-')               
                    d3=''
                    for h in d2:
                        d3=d3+h
                    d4=datetime.datetime.strptime(d3, '%Y%m%d').date()
                    d5=d1-d4
                 
                    if d5==datetime.timedelta(0):
                        days=0
                    else:
                        days=int(str(d5).split()[0])
                    if(days>15):
                        print("\nStudent has a fine of "+str(days-15))
                        dic[usn][3]+=(days-15)
                    i[0]='#'
                    i[1]='@'
                    flag=1                        
                    break
            break
        newlines.append(dic)
    newlines.append(dic)
    while True:
        w=f.readline()
        if(len(w)==0):
            break
        dic=eval(w)
        newlines.append(dic)
    f.close()
    f=open("/Python27/libr/stud_db1.txt","w")
    f.write(str(newlines[0]))
    for k in newlines[1:]:
        f.write("\n"+str(k))                                
    f.close()
    print "\nThe book has been returned\n"
    vv=raw_input("1 to go back or any other key to exit")
    if(vv=='1'):
        if (x==1):
            os.system('cls')
            librarian.main1()
        else:
            os.system('cls')
            librarian.main2()
    else:
        sys.exit()
