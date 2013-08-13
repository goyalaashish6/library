import os
import librarian
import sys
import welcome
def main(x):
    os.system('cls')
    welcome.func()
    flag=0
    f=open("/Python27/libr/stud_db1.txt")
    g=open("/Python27/libr/students_list_with_fine.txt","w")
    g.write("USN        FINE\n")
    l=[]
    while True:        
        w=f.readline()
        if(len(w)==0):           
            break
        d=eval(w)
        for k in d:
            for i in [0,1,2]:
                if d[k][i][0]!='#':
                    d[k][3]+=1000
                    d[k][i][0]='#'
                    d[k][i][1]='@'
                    
            if d[k][3]>0:
               flag=1 
               g.write(k+"  "+"Rs."+str(d[k][3]))
               print("\n"+k+"  "+"Rs."+str(d[k][3]))
               d[k][3]=0     
        l.append(d)
    f.close()
    if flag==0:
        print("None of the students have any fine\n")
    else:
        print("\nOpen the file  'students_list_with_fine.txt' to get a hard copy of students who have fine")              
    f=open("/Python27/libr/stud_db1.txt","w")
    f.write(str(l[0]))
    for i in l[1:]:
       f.write("\n"+str(i))
    g.close()
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
