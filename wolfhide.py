import sys
import base64
from os import system
from time import sleep
from sys import platform
from os.path import exists

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

        imgfile = input("IMG : ")

        if exists(imgfile):

            smsg = input("Your Secret's : ")

            msg = smsg
            message = msg.lower()

            encryption = {
                "a":"ț","b":"Ȅ","c":"¢","d":"¥","e":"µ","f":"֍","g":"թ","h":"փ","i":"ջ","j":"ֆ","k":"Փ",
                "l":"Ֆ","m":"Ԅ","n":"Ӝ","o":"Ѥ","p":"Ѭ","q":"Ѿ","r":"Ђ","s":"Щ","t":"Ы","u":"Ϟ","v":"Ψ",
                "w":"Ξ","x":"ξ","y":"ĝ","z":"ŵ"," ":"£","1":"Z","2":"X","3":"C","4":"V","5":"B","6":"N",
                "7":"M","8":"A","9":"S","0":"D","~":"Q","!":"W","@":"E","#":"R","$":"T","%":"Y","&":"U",
                "*":"P","+":"I","-":"O","_":"L","=":"J",".":"1","`":"2","^":"3","(":"4",")":"5","{":"6",
                "}":"7","[":"8","]":"9","|":"0","\\":"_",":":"{",";":"]","<":":",">":";",",":"?","/":"\\",
                "?":">",'"':' ',"'":"~",
            }

            secret_msg = ""
            for i in message:
                secret_msg += i.replace(i, encryption[i])

            with open(imgfile, "rb") as f:
                reading = f.read()

            secret_file = input("Output Filename : ")

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
                sys.stdout.write("\rAnonymizing : " + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")

            with open(secret_file, "wb") as secret:
                secret.write(reading)

            secret_msg_1 = secret_msg.encode("utf-8")
            secret_msg_1 = base64.b64encode(secret_msg_1)
            secret_msg_2 = secret_msg_1.decode("utf-8")

            with open(secret_file, "a") as f:
                f.writelines("\n<secret>" + secret_msg_2 + "</secret>")

            print("Anonymized Successfully ...")

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
    sys.stderr.write("\nEncryption Failed !!")
    sys.exit(0)