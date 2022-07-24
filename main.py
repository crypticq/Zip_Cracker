
import zipfile
import sys


password_file = input("Enter Your password file : ")


file = input("Enter Your File to crack: ")

in_Zip = file

password = [line.strip() for line in open(password_file)]




for i , passwords in enumerate(password):
    try:
        
        z = zipfile.ZipFile(in_Zip, 'r')
        pas = bytes(passwords, encoding="utf-8")
        z.extractall(pwd=pas)
        print(f"Hacked Password is  {passwords}")
        break
    except Exception as e:
        print(i , f'Wrong password ! {passwords}')

