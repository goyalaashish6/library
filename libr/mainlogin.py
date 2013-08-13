import welcome
import os
import sys
import getpass
import librarian
super_id="pes"                        #set the super user id
super_pass="bsc"                  #set the super user password
def sup_log():
    log=raw_input("\nChief Login ID:\n")
    password=getpass.getpass()
    if not(log==super_id and password==super_pass):
        print("\nInvalid super user ID or Password\n")
        sup_a=raw_input("1.Retry\nany other key to go back")
        if sup_a=='1':
            os.system('cls')            
            welcome.func()
            sup_log()
        else:
            os.system('cls')
            main()
    else:
        librarian.main2()

def lib_log():
    log=raw_input("\nMemeber ID:\n")
    password=getpass.getpass()
    f=open("/Python27/libr/librarians.txt")
    g=0    
    while True:       
        a=f.readline()
        if(len(a)==0):
            break
        mem=eval(a)
        if (mem[0]==log and mem[1]==password):
            g=1
            break
    if g==0:    
        print("\nInvalid  user ID or Password\n")
        sup_a=raw_input("\n1.Retry\nany other key to go back")
        if sup_a=='1':
            os.system('cls')            
            welcome.func()
            lib_log()
        else:
            os.system('cls')
            main()
    else:
        librarian.main1()
def main():
    welcome.func()
    print("\nLogin")
    print("\n1.Chief Librarian")
    print("\n2.Librarian")
    print("\n3.Exit")
    a=raw_input("\nEnter the Option\n")
    if a not in ['1','2','3']:
        print ("Wrong input")
        os.system('cls')
        main()
    elif a=='3':
        sys.exit()                      #call the exit function
    elif a=='1':
        sup_log()
    elif a=='2':
        lib_log()
main()
