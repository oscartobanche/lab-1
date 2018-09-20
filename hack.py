#OSCAR TOBANCHE
#PROF DIEGO AGUIRRE
#LAB 1 VERSION C
#9/18/2018
import hashlib
def hash_with_sha256(str):
        hash_object = hashlib.sha256(str.encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
#THIS IS THE METHOD WITH THE RECURSIVE FUNCTION, AND HAS 6 PARAMETERS
def h(position,password,initial,maxVal,salt,hashed):
    password = initial
    #2 FOR LOOPS, THE OUTERMOST KEEPS TRACK OF THE USER, THE INNER LOOP USES BRUTEFORCE TO DECODE
    for j in range (100,0,-1):
        for i in range(0, maxVal+1):
            if i == maxVal:
                print("...")
                h(position,password, initial + '0',maxVal*10,salt,hashed)
            else :
                salted_password = str(password) + str(salt[position])
                #THIS PART SENDS THE SALTED PASSWORD AND PASS IT THROUGH THE METHOD THE PROFESSOR GAVE US
                hex_dig = hash_with_sha256(salted_password)
                if hex_dig == hashed[position]:
                    print("the password is :" + str(password) + "   user"+ str(position))
                    #print(hex_dig)
                    #print(salted_password)
                    position = position -1
                    h(position,password,initial,maxVal,salt,hashed)
                else:
                    #THIS PART ADD ONE TO THE PASSWORD GUESS
                    password = int(password)
                    password = password + 1
                    str(password)
    return
def main():


    #DECLARING 3 ARRAYS
    user = []
    salt = []
    hashed= []
    #THIS PART READS THE FILE AND SPLIT THE LINE IN 3, EACH IS STORED IN ARRAYS
    with open('password_list.txt','r') as file:
        for line in file:
            first = line.strip().split(',')
            for i in range (0,3):
                if i == 0:
                    user.append(first[i])
                elif i == 1:
                    salt.append(first[i])
                elif i == 2:
                    hashed.append(first[i])
    h(99, '00','000',1000,salt,hashed)
main()


