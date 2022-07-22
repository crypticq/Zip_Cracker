
import zipfile
import sys

file = input("Enter Your File to crack ")
in_Zip = file

password = []

with open("2020-200_most_used_passwords.txt" , 'r') as f:
    for line in f:
        password.append(line.strip())

i = 0
for passwords in password:
    try:
        i+=1
        z = zipfile.ZipFile(in_Zip, 'r')
        pas = bytes(passwords, encoding="utf-8")
        z.extractall(pwd=pas)
        print(f"Hacked Password is  {passwords}")
        break
    except Exception as e:
        print(i , f'Wrong password ! {passwords}')

