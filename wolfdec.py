import sys
import base64
from os import system
from time import sleep
from sys import platform
from os.path import exists
from bs4 import BeautifulSoup

try:

    choice = True

    while choice:

        if platform == "linux" or platform == "linux2":
            system("clear")
        elif platform == "win32":
            system("cls")

        print("""
                     .
                    / V\\
                  / `  /
                 <<   |        _    _  __  __    ___    _  _  __  ___  ___ 
                 /    |       ( \/\/ )/  \(  )  (  _)  ( )( )(  )(   \(  _)
               /      |        \    /( () ))(__  ) _)   )__(  )(  ) ) )) _)
             /        |         \/\/  \__/(____)(_)    (_)(_)(__)(___/(___)
           /    \  \ /                                          version 1.0
          (      ) | |
  ________|   _/_  | |
<__________\______)\__)                                     by:-rohit_singh
    """)

        filename = input("IMG : ")

        if exists(filename):
            with open(filename, "rb") as f:
                msg_fetch = f.readlines()[-1].decode()
                fetch = BeautifulSoup(str(msg_fetch), "html.parser")
                soup = fetch.find("secret")

            decryption = {
                    "ț":"a","Ȅ":"b","¢":"c","¥":"d","µ":"e","֍":"f","թ":"g","փ":"h","ջ":"i","ֆ":"j","Փ":"k",
                    "Ֆ":"l","Ԅ":"m","Ӝ":"n","Ѥ":"o","Ѭ":"p","Ѿ":"q","Ђ":"r","Щ":"s","Ы":"t","Ϟ":"u","Ψ":"v",
                    "Ξ":"w","ξ":"x","ĝ":"y","ŵ":"z","£":" ","Z":"1","X":"2","C":"3","V":"4","B":"5","N":"6",
                    "M":"7","A":"8","S":"9","D":"0","Q":"~","W":"!","E":"@","R":"#","T":"$","Y":"%","U":"&",
                    "P":"*","I":"+","O":"-","L":"_","J":"=","1":".","2":"`","3":"^","4":"(","5":")","6":"{",
                    "7":"}","8":"[","9":"]","0":"|","{":":","]":";",":":"<",";":">","?":",",">":"?","_":"\\",
                    "\\":"/",' ':'"',"~":"'",
                }

            animation = [
                "[■□□□□□□□□□]",
                "[■■□□□□□□□□]",
                "[■■■□□□□□□□]",
                "[■■■■□□□□□□]",
                "[■■■■■□□□□□]",
                "[■■■■■■□□□□]",
                "[■■■■■■■□□□]",
                "[■■■■■■■■□□]",
                "[■■■■■■■■■□]",
                "[■■■■■■■■■■]",
            ]

            for i in range(len(animation)):
                sleep(0.2)
                sys.stdout.write("\rDeanonymizing : " + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")

            print("Deanonymized Successfully ...")

            your_secret = ""
            fetch = soup.text

            secret_msg = fetch.encode("utf-8")
            secret_msg = base64.b64decode(secret_msg)
            secret_msg = secret_msg.decode("utf-8")

            for i in secret_msg:
                your_secret += i.replace(i, decryption[i])

            print("SECRET MESSAGE : " + your_secret)

            select = input("\n1 For Again or 0 For Exit : ")

            if select == "1":
                choice = True
            elif select == "0":
                choice = False
            else:
                choice = False

        else:
            sys.stderr.write("Filename Not Exist !")
            select = input("\n1 For Again or 0 For Exit : ")

            if select == "1":
                choice = True
            elif select == "0":
                choice = False
            else:
                choice = False

except:
    sys.stderr.write("\nDecryption Failed !!")
    sys.exit(0)