import hashlib
def hash_with_sha256(str):
        hash_object = hashlib.sha256(str.encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
def h(length,maxVal,salt,hashed):
    for j in range (0,100):
        for i in range(0, maxVal+1):
            if length == 3:
               x = ("{0:03}").format(i)
               #print(x)
               salted_password = x + salt[j] #i
               hex_dig = hash_with_sha256(salted_password)
               if hex_dig == hashed[j]:
                   print("the user password is " + x )
                   print (j)
                   print(hex_dig)
                   #position = position - 1

            elif length == 4:
                x = ("{0:04}").format(i)
                salted_password = x + salt[j]  # i
                hex_dig = hash_with_sha256(salted_password)
                if hex_dig == hashed[j]:
                   print("the user password is " + x)
                   print (j)
                   print(hex_dig)

            if length == 5:
                x = ("{0:05}").format(i)
                salted_password = x + salt[j]  # i
                hex_dig = hash_with_sha256(salted_password)
                if hex_dig == hashed[j]:
                   #print(x)
                   print("the user password is " + x)
                   print(j)
                   print(hex_dig)
                   #position = position - 1
            elif length == 6:
                x = ("{0:06}").format(i)
                salted_password = x + salt[j]  # i
                hex_dig = hash_with_sha256(salted_password)
                if hex_dig == hashed[j]:
                    print("the user password is " + x)
                    print(j)
            elif length == 7:
                x = ("{0:07}").format(i)
                salted_password = x + salt[j ]  # i
                hex_dig = hash_with_sha256(salted_password)
                if hex_dig == hashed[j]:
                    print("the user password is " + x)
                    print(j)

def main():


    user = []
    salt = []
    hashed= []
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
    h(3,1000000,salt,hashed)
main()









