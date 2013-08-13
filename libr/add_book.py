import librarian
import os
import sys
def main(x):
    lis=[]
    f=open("/Python27/libr/books.txt","r")
    while True:
        l=f.readline()
        if (len(l)==0):
            break
        m=eval(l)
        lis.append(m)
        id=m[0]
    f.close()
    q=list(id)
    s1=q[5]
    s1=int(s1)
    s2=q[4]
    s2=int(s2)
    s3=q[3]
    s3=int(s3)
    s=s1+(10*s2)+(100*s3)
    s=s+1
    if(s<=9):
        q[5]=str(s)
    elif(s<=99):
        a=s%10
        q[5]=a
        s=s/10
        q[4]=s
    else:
        q[5]=s%10
        s=s/10
        q[4]=s%10
        s=s/10
        q[3]=s
    s1 = ''.join(str(n) for n in q)
    print s1
    n=0
    while (n==0):
        try:
            b_n=raw_input("\nenter book name\n")
            b_c=raw_input("\nenter book category\n")
            b_a=raw_input("\nenter book author\n")
            b_p=input("\nenter book price\n")
            b_e=input("\nenter book edition\n")
            b_y=input("\nenter book year\n")
            b_pu=raw_input("\nenter book publisher\n")
            n=1
        except SyntaxError:
            print "wrong Input"
            n=0       
        except:
            print "wrong Input"
            n=0         
    l=[s1,b_n,b_c,b_a,b_p,b_e,b_y,b_pu,'#']
    lis.append(l)
    f.close()
    f=open("/Python27/libr/books.txt","w")
    f.write(str(lis[0]))
    for i in lis[1:]:
        f.write("\n"+str(i))
    print("\nBook added Succesfully\n")
    f.close()
    a=raw_input("\nTo Add Another book Enter 1\npress any key to go back\n")
    if a=='1':
        main(x)
    else:
        if (x==1):
            os.system('cls')
            librarian.main1()
        else:
            os.system('cls')
            librarian.main2()
