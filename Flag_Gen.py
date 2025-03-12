import random
import string

length = random.randint(5,10)

def flag_gen(number):
    output = []
    index = list(string.ascii_letters)
    for i in range(0,number):
        N = random.randint(0,51)
        output.append(index[N])
    return output

flag = str(flag_gen(length)).replace("'","").replace(",","").replace("[","").replace("]","").replace(" ","")
print(flag)