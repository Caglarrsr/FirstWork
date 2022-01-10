
import random
user_int = input("START: ")
def pass_gen(y, user_int):
    numbers = ("0","1","2","3","4","5","6","7","8","9","0","!","'","+","?","*","&","/","*","-","^","<", ">")              
    answer = ''.join(random.choice(numbers) for s in range(y))
    if len(user_int) <= 7 and all(x.isalpha() or x.isspace() for x in user_int):
        return answer
for i in range(10):
    print(pass_gen(random.choice([80, 100, 120, 150, 170, 200, 250, 300, 400, 500]), user_int=user_int))
    print(30*"--")
 --------------------------------------


import random , sys

user_ask_main = input("ENTER YOUR PASSWORD TO ENCODE: ").replace(" ","").upper()
def user_check(user_input=str):
    try:
        pass_list = ["1","2","3","4","5","6","7","8","9","0"]
        control_list = ["0","1","2","3","4","5","6","7","8","9"]
        strig_list = ["!","+","%","&","/","(",")","'","=","?"]
        user_new_list = []
        user_last_password = []
        user_out = []
        last_password_list = []
        user_password_last = []
        st_new = ""
        last_new = ""
        end_str = ""
        i_count_table = 0
        if len(user_input) <= 7:
            for x_line in user_input:
                if x_line in control_list:
                    print("TYPE ONLY STRING")
                    sys.exit()
                    break
                else:
                    x_line = random.choice(pass_list)
                    st_new += x_line
                    user_new_list.append(st_new)
                    i_count_table += 1
        else:
            print("TYPE 7 WORDS OR LESS AND IT MUST BE STRING")
        for x in range(10):
            user_last_password.append(random.choice(user_new_list))
        for x_last in user_last_password:
            if x_last == int:
                x_last = random.choice(random.uniform(0, 4)) * 2
                last_new += str(x_last)
                if len(last_new) >= 10:
                    user_out.append(last_new)
            else:
                last_new += str(x_last) + random.choice(pass_list)
                if len(last_new) >= 10:
                    user_out.append(last_new)
        for x in range(10):
            x_pat_last = random.choice(user_out)
            for x_end in x_pat_last:
                x_end = random.choice(control_list)
                end_str += x_end
            last_password_list.append(int(end_str) + int(random.choice(control_list)) * int(random.choice(control_list)))
            
        for x_t in last_password_list:
            for x in range(11):
                x_t = str(x_t).replace(f"{x}",random.choice(strig_list)+f"{random.choice(control_list)}")
                user_password_last.append(x_t)
        new_usr_pass = []
        for x in range(10):
            new_usr_pass.append(random.choice(user_password_last))
        for x_p in new_usr_pass:
            print("\n")
            print(x_p)
            print("\n"+"------"*10+"\n")
    except:
        print("ERROR")
            
user_check(user_ask_main)    

---------------------------------------------------------------------------------------------------------
import random , sys
user_int = input("Enter User Acc: ")
def pass_gen2(y, user_int):   
        numbers = ("0","1","2","3","4","5","6","7","8","9","0","!","'","+","?","*","&","/","*","-","^","<", ">")        
        answer = "".join(random.choice(numbers) for s in range(y))
        if len(user_int) >= 12 and len(user_int) <= 20 and all(x.isalpha() for x in user_int):
            return answer
        else:
            sys.exit("Please min 12, max 20 char and only str")
            

for i in range(1):
            randoms = [12,13,14,15,16,17,18,19,20] 
            user = pass_gen2(random.choice(randoms), user_int=user_int)
            print(user)        
            again_pass = input("please again your pass: ")
            if again_pass == user:
                print("welcome " + user_int)
            else:
                print("It's not your password, try again!")

---------------------------------------------------------------------------------------------------------------


import random , sys
import string , os
users = input("Enter User Name: ")
password =  "".join(random.choice(string.hexdigits) for x in range(random.randint(7, 14)))
if len(users) <= 16 and len(users) >= 8:
    print("Your password is: " + password)
else:
    sys.exit("Please min8, max 16 char")
    
s = input("Do you want to continue? Y/N ")
if s == "Y" or s == "y":
    k = input("Cool! Please take your password here: ")
    
elif s != "Y" or s != "y":
    sys.exit("Okay, goodbye!")        
        
if k == password:
    print("Nice! Welcome " + users)

elif k != password:
       sys.exit("It's not your password, please try again..")
    
p = input("Can you go to the cmd panel? Y/N ")
if p == "Y" or p =="y":
    os.system("start cmd ")
    
elif s != "Y" or s != "y":
    print("Oke, bye")

    ---------------------------------------------------------------------------------------------------------------
import socket,os,sys,random
from subprocess import call
from datetime import datetime


print("-"*34 + "Welcome" + "-"*26)
print("1-Cmd Panel", "2-Chrome", "3-Instagram", 
      "4-Twitter", "5-Linkedin","6-Facebook",
      "7-Github","8-Calculator","9-Port Scan",
      "10-Powershell","11-Make Password","12-DDoS",sep = "\t" )
print(" ")
print("What you want?")
user = input("Write here ---> ")
def pc(user):
        if user == "1":
            return os.system("start cmd")      
        elif user == "2":
            return os.system("start chrome")        
        elif user == "3":
            return os.system("start www.instagram.com")        
        elif user == "4":
            return os.system("start www.twitter.com")        
        elif user == "5":
            return os.system("start www.linkedin.com")       
        elif user == "6":
            return os.system("start www.facebook.com")      
        elif user == "7":
            return os.system("start www.github.com")     
        elif user == "8":
            return call(["calc.exe"]) 
        
        elif user == "9":
            remoteServer = input("Enter a remote host to scan: ")
            remoteServerIP = socket.gethostbyname(remoteServer)
            print ("-" * 60)
            print ("Please wait, scanning remote host", remoteServerIP)
            print ("-" * 60)
            t1 = datetime.now()
            
            try:
                for port in range(1,1024):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((remoteServerIP, port))
                    if result == 0:
                        print("Port {}: Open".format(port))
                    else:
                        print("Port {}: Close".format(port))
                    sock.close()
            except KeyboardInterrupt:
                print ("You pressed Ctrl+C")
                sys.exit()
            except socket.gaierror:
                print ('Hostname could not be resolved. Exiting')
                sys.exit()
            except socket.error:
                print ("Couldn't connect to server")
                sys.exit()
            t2 = datetime.now()
            total = t2 - t1
            print ('Scanning Completed in: ', total)
            
            
        elif user == "10":
            return os.system("start powershell")
        
        elif user =="11":
            user_int = input("START: ")
            def pass_gen(y, user_int):
                numbers = ("0","1","2","3","4","5","6","7","8","9","0","!","'","+","?","*","&","/","*","-","^","<", ">")              
                answer = ''.join(random.choice(numbers) for s in range(y))
                if len(user_int) <= 7 and all(x.isalpha() or x.isspace() for x in user_int):
                    return answer
            for i in range(10):
                print(pass_gen(random.choice([80, 100, 120, 150, 170, 200, 250, 300, 400, 500]), user_int=user_int))
                print(30*"--")
        
        else: 
            return "-"*34 + "Bye" + "-"*30
print(pc(user=user))
