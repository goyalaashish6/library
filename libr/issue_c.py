import welcome
import os
import sys
import datetime
import librarian
def main(x):
    os.system('cls')
    welcome.func()
    f=open("/Python27/libr/stud_db1.txt")
    flag=0
    line_count=-1
    newlines=[]                             #to store the lines until specified usn is found
    usn=raw_input("\nEnter the USN\n")  
    while True:
        line=f.readline()                    # read a line from student database
        if len(line)==0:
            break
        line_count+=1
        dic=eval(line)                      #convert it into dictionary
        newlines.append(dic)       
        if dic.has_key(usn):                # check if the read usn exists    
            flag=1
            break
    if flag==0:
        print"\nInvalid USN\n"
        inp=raw_input("\nPress 1 to type again or anything else to go back\n")
        if inp=='1':
            os.system('cls')
            main(x)
        else:
            if (x==1): 
                os.system('cls')
                librarian.main1()
            else:
                os.system('cls')
                librarian.main2()
    space=-1
    count=0
    for i in dic[usn]:
        check=isinstance( i, int ) 
        if check==True:
            i=str(i)
        space+=1                            #i is status of 3 slots of books to each usn
        if i[0]=='#':   
            break
        else:
            count+=1
    #print space
    if count==4:
        v=raw_input("\n\nYou have already issued 3 books\n\nPress 1 to go back\n\nelse anything else to exit\n")
        if v=='1':
            if (x==1): 
                os.system('cls')
                librarian.main1()
            else:
                os.system('cls')
                librarian.main2()
        else:
            sys.exit()
    else:
        flag_1=0
        line_count2=-1
        newlines2=[]   
        sid=raw_input("\nType the book ID\n")
        g=open("/Python27/libr/books.txt")
        while True:
            w=g.readline()
            if(len(w)==0):
                break
            line_count2+=1
            b=eval(w)
            if(b[0]==sid and b[8]=='#'):
                flag_1=1
                print "\n\nBook Allocated\n" "\nBook Serial no ="+b[0]+"\nBook Title ="+b[1]+"\nCategory ="+b[2]+"\nBook Author ="+b[3]+"\nBook Edition ="+str(b[5])+"\nBook Publisher ="+str(b[7])
                d2 = datetime.date.today()+ datetime.timedelta(days=15)
                print("\nReturn Date : "+str(d2))
                break
            newlines2.append(b)
            
        if flag_1==0:
            inpu_2=raw_input("No book available with this book ID in the library\nPress1.to go back\nelse any other key to exit")
            if inpu_2=='1':
                 if (x==1): 
                    os.system('cls')
                    librarian.main1()
                 else:
                    os.system('cls')
                    librarian.main2()
            else:
                sys.exit()
            
        if flag_1==1:
            b[8]=usn
            newlines2.append(b)
            while True:
                q=g.readline()
                if len(q)==0:
                    break
                q1=eval(q)
                newlines2.append(q1)
            g.close()
            usn_line=newlines[line_count]
            #print line_count
            #for z in range(0,line_count):          #for testing
            #   print newlines[z]                   #for testing
            #print usn_line                         #get the line to be changed
            x=usn_line[usn]                         #get the key value of that line
            x[space][0]=sid
            d1=datetime.date.today()
            x[space][1]=str(d1)
            while True:
                q=f.readline()
                if len(q)==0:
                    break
                q1=eval(q)
                newlines.append(q1)
            f.close()
            g=open('/Python27/libr/books.txt',"w")
            g.write(str(newlines2[0]))
            for i in newlines2[1:]:
                g.write("\n"+str(i))                                
            g.close()
            f=open('/Python27/libr/stud_db1.txt',"w")
            f.write(str(newlines[0]))
            for i in newlines[1:]:
                f.write("\n"+str(i))                                
            f.close()
            inpu_2=raw_input("\nPress1.to go back\nelse any other key to exit")
            if inpu_2=='1':
                 if (x==1): 
                    os.system('cls')
                    librarian.main1()
                 else:
                    os.system('cls')
                    librarian.main2()
            else:
                sys.exit()
