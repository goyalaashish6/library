import os
import time
import datetime
import librarian
import sys
import welcome
def main(x):
    os.system('cls')
    welcome.func()
    f=open("/Python27/libr/stud_db1.txt")
    g=open("/Python27/libr/list_fin1.txt","w")
    g.write("STUDENT USN        BOOKS TO BE RETURNED\n")
    newlist=[]
    flag=0
    while True:
        pending=''
        lis=[]
        w=f.readline()
        if len(w)==0:
            break
        dic=eval(w)
        for k in dic:
            for i in [0,1,2]:
                if dic[k][i][0]!='#':
                        lis.append(dic[k][i][0])
                        if str(lis)!='':
                            pending=str(lis)
                      
        if pending!='':  
          
            g.write(k+"        "+pending+"\n")
    f.close()
    g.close()
    

    da1 =raw_input('Enter the final fine evaluation date(dd/mm/yyyy):')
    try:
        date2 = time.strptime(da1, '%d/%m/%Y')   #convert string into date
    except ValueError:
        print('Invalid date!\nEnter again')
        main()
    d=da1.split('/')           #for extracting date,year and month from the date1
    d1=''
    for i in d:
        d1=d1+i
  #print d1
    s2 =datetime.datetime.strptime(d1,'%d%m%Y').date()
    s1=datetime.date.today()
    if s2<s1:
        print("\nYou have typed a date which is already over...Type a valid date\n")
        main(x)
    os.system('cls')
    f=open("/Python27/libr/list_fin1.txt")
    print("\nThe following students are here by informed to return the books mentioned along with their USN on or before "+da1+"\n\nStudents who fail to return any books before mentioend date will have to pay the fine of Rs1000 in order to get the hall ticket\n")
    while True:
        w=f.readline()
        if (len(w)==0):
            break
        print ("\n"+w)
    f.close()
    print("\nOpen the file  'list_fin1.txt' to get a hard copy of students who are supposed to return books\n")      
    print("\n\nInstruction for the librarians:\nPlease calculate the fine after date: "+da1+" so that students can get time to return their due books")
    q=raw_input("1 to go back or any other key to exit")
    if(q=='1'):
        if (x==1):
            os.system('cls')
            librarian.main1()
        else:
            os.system('cls')
            librarian.main2()
    else:
        sys.exit()

