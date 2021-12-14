
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

