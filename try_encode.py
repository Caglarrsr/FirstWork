
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

