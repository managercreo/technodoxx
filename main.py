#!usr/bin/python

import random
import colorama
import os
import requests
import re
import socket
import time
import string
import phonenumbers
import webbrowser
import subprocess
from colorama import Fore
from colorama import Style

# Proyecto TechnoDox - Herramienta de Doxing Gratuita

subprocess.call("clear", shell=True)


def menu():
    print(
        Fore.RED
        + f"""

    {Fore.WHITE} _______        _                 _____{Fore.RESET}
    {Fore.WHITE}|__   __|      | |               |  __ \{Fore.RESET}
    {Fore.WHITE}   | | ___  ___| |__  _ __   ___ | |  | | ___ _ _{Fore.RESET}
    {Fore.WHITE}   | |/ _ \/ __| '_ \| '_ \ / _ \| |  | |/ _ \ \/ /{Fore.RESET}
    {Fore.WHITE}   | |  __/ (__| | | | | | | (_) | |__| | (_) >  <{Fore.RESET}
    {Fore.WHITE}   |_|\___|\___|_| |_|_| |_|\___/|_____/ \___/_/\_\{Fore.RESET}
               
            By Manager.                         Doxing & Ethical OSINT Tools Recopilation
                                v1.0.0 (BETA)
               
               """
    )


menu()

menuinput = int(

    input(
        Fore.LIGHTRED_EX
        + f"""

 [1] OSINT Tools
 [2] Security Tools
 [3] IPLoggers
 [4] Pentesting Tools
 [5] Search Username
 [6] PhoneNumberInfo
 [7] doxing tips (SOON)...

    ~ $ """))
    


def osintools():
    subprocess.call("clear")
    menu()
    osintoolsinput = int(input(Fore.RED+'''

    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠈⠻⢿⠿⠋⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠉⠙⠛⠛⠛⠛⢛⣛⣉⣁⣀⣈⣉⣙⣛⣿⣿⣿⣿⣿
    ⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠼⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿
    ⣿⣿⣿⣿⣿⠿⠶⠶⣶⡶⣶⣴⣤⣤⣤⣤⣤⣤⣶⣶⣶⡶⠶⠿⢿⣿⣿⣿⣿⣿
    ⣿⣿⡿⠋⠁⠀⠀⠀⠹⣆⡀⠀⠀⣠⣶⣶⣄⠀⠀⢀⣾⡇⠀⠀⠀⠈⠻⣿⣿⣿
    ⣿⣯⣤⣄⣀⣀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⢀⣀⣀⣤⣤⣽⣿
    ⣿⣿⣿⣿⣿⣿⣿⠟⠃⠀⠙⢿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠛⢿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣥⣀⡀⠀⠀⠀⠙⢿⣿⣿⠏⠀⠀⠀⠀⣀⣠⣽⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⣸⠃⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡏⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        
     TechnoDox! - Security Tools... [BETA]


###########################################
#                                         #
#   1) OsintFramework                     #
#                                         #
#   2) Mitaka (GitHub)                    #
#                                         #
#   3) Shodan                             #
#                                         #
###########################################
    
    ~ $ '''))

    if osintoolsinput == 1:
        subprocess.call("clear")
        menu()
        tolosint = int(
            input(Fore.RED+ """ 
        
        TechnoDox !

###########################################
#                                         #
#       1) Open in Linux                  #
#                                         #
#       2) Open in Termux (Android)       #
#                                         #
#                                         #
#       3) Go Back...                     #
#                                         #
###########################################
        
        ~ $ """
            )
        )

        if tolosint == 1:
            print("\n Opening in Linux...")
            webbrowser.open("https://osintframework.com")
            return osintoolsinput
        if tolosint == 2:
            print("\n Opening in Termux...")
            os.system("termux-open https://osintframework.com")
        if tolosint == 3:
            return osintools()

    if osintoolsinput == 2:
        subprocess.call("clear")
        menu()
        tolmitaka = int(
            input(Fore.RED+"""
        
        TechnoDox !

###########################################
#                                         #
#       1) Open in Linux                  #
#                                         #
#       2) Open in Termux (Android)       #
#                                         #
#                                         #
#       3) Go Back ...                    #
#                                         #
###########################################
        
        ~ $ """
            )
        )

        if tolmitaka == 1:
            print("\n Opening in Linux...")
            webbrowser.open("https://github.com/ninoseki/mitaka")
        if tolmitaka == 2:
            print("\n Opening in Termux... ")
            os.system("termux-open https://github.com/ninoseki/mitaka")

        if tolmitaka == 3:
            return osintools()

    if osintoolsinput == 3:
        subprocess.call("clear")
        menu()
        tolshodan = int(
            input(Fore.RED+"""
        
        TechnoDox !

###########################################
#                                         #
#       1) Open in Linux                  #     
#                                         #
#       2) Open in Termux (Android)       #
#                                         #
#                                         #
#       3) Go Back...                     #
#                                         #
###########################################
        
        ~ $ """
            )
        )
        if tolshodan == 1:
            print("\n Opening in Linux...")
            webbrowser.open("https://shodan.io/")
        if tolshodan == 2:
            print("\n Opening in Termux")
            os.system("termux-open https://shodan.io/")
        if tolshodan == 3:
            return osintools()


####################################################################


def securitytools():
    subprocess.call("clear")
    menu()
    secinput = int(input(
        Fore.LIGHTGREEN_EX+"""
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--` 

    TechnoDox! - Security Tools... [BETA]


###########################################
#                                         #
#   1) Strong Password Generator          #
#                                         #
#   2) Proxychains                        #
#                                         #
#   3) Soon...                            #
#                                         #
###########################################

    ~ $ """
         )
    )

    if secinput == 1:
        print(Fore.LIGHTGREEN_EX+"""
        
        Strong Password Generator...
        
        """
        )
        os.system("cd cdm && python spg.py")

    if secinput == 2:
        subprocess.call("clear")
        menu()
        pxcsec = int(
            input(
                Fore.LIGHTGREEN_EX+"""
        
    
    TechnoDox! - Security Tools... [BETA]

###########################################  
#                                         #
#   1) Proxychains - NG                   #
#                                         #
#                                         #
#   2) Go Back...                         #
#                                         #
###########################################
            
    ~ $ """
            )
        )

        if pxcsec == 1:
            os.system("cd install && bash installation.sh")
        if pxcsec == 2:
            return securitytools()
        
    if secinput == 3:
        print(Fore.LIGHTGREEN_EX+"This option will be open later... ")
        exit()

######################################################################

def iploggers():
    subprocess.call("clear")
    menu()
    menuilg = int(input(Fore.LIGHTYELLOW_EX+'''


     4$$c                .$$r
     ^$$$b              e$$$"
     d$$$$$e          z$$$$$b
    4$$$*$$$$$c    .$$$$$*$$$r          They are the bests loggers of IP 
     ""    ^*$$$be$$$*"    ^"               in the Network. Use it own
              "$$$$"                          your responsabilitie.
            .d$$P$$$b
           d$$P   ^$$$b
       .ed$$$"      "$$$be.
     $$$$$$P          *$$$$$$
    4$$$$$P            $$$$$$"
     "*$$$"            ^$$P
        ""              ^"

      TechnoDox - IPLoggers
    
########################################### 
#                                         #
#   1) Grabify                            #
#                                         #
#   2) IPLogger (Network)                 #
#                                         #
###########################################
    
    ~ $ '''))
    
    if menuilg == 1:
        subprocess.call("clear")
        menu()
        toliplogger = int(input(Fore.LIGHTYELLOW_EX+'''
        
########################################### 
#                                         #
#   1) Open in Linux                      #
#                                         #
#   2) Open in Termux                     #
#                                         #
#                                         #
#   3) Go Back...                         #
#                                         #
###########################################
    
    ~ $ '''))
        
        if toliplogger == 1:
            print("\n Opening in Linux... ")
            webbrowser.open("https://grabify.org")
            return menuilg()
        if toliplogger == 2:
            print("\n Opening in Termux... ")
            os.system("termux-open https://grabify.org")
            return menuilg()
        if toliplogger == 3:
            return iploggers()
        
    if menuilg == 2:
        subprocess.call("clear")
        menu()
        tolipip = int(input(Fore.LIGHTYELLOW_EX+'''

########################################### 
#                                         #
#   1) Open in Linux                      #
#                                         #
#   2) Open in Termux                     #
#                                         #
#                                         #
#   3) Go Back...                         #
#                                         #
###########################################

    ~ $ '''))

        if tolipip == 1:
            print("\n Opening in Linux... ")
            webbrowser.open("https://iplogger.org")
        if tolipip == 2:
            print("\n Opening in Termux... ")
            os.system("termux-open https://iplogger.org")
        if tolipip == 3:
            return iploggers()
    
    if menuilg == 3:
        print("This option will be open later... ")
        exit()


def pentools():
    subprocess.call("clear")
    menu()
    peninput = int(input(Fore.LIGHTRED_EX+'''
    
        TechnoDox - Pentesting Tools 
          
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠚⠉⠀⠀⠉⠑⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀This place is the acces to the
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀some tools for pentesting.
    ⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀       
    ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣠⠔⠋⠉⣩⣍⠉⠙⠢⣄⠀⢸             We not are responsables
    ⠀⠀⠀⠀⠀⠀⠀⠀⢧⡜⢏⠓⠒⠚⠁⠈⠑⠒⠚⣹⢳⡸        to the uses that you give to this.
    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠸⡄⠀⠀⠀⠀⠀⠀⢠⠇⣰⠃⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⡴⠚⠉⢣⡙⢦⡀⠀⠀⢀⡰⢋⡜⠉⠓⠦⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡴⠁⢀⣀⣀⣀⣙⣦⣉⣉⣋⣉⣴⣋⣀⣀⣀⡀⠈⢧⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⡸⠁⠀⢸⠀⠀⠀⠀⢀⣔⡛⠛⡲⡀⠀⠀⠀⠀⡇⠀⠈⢇⠀⠀⠀⠀        ATTENTION: 
    ⠀⠀⠀⢠⠇⠀⠀⠸⡀⠀⠀⠀⠸⣼⠽⠯⢧⠇⠀⠀⠀⠀⡇⠀⠀⠘⡆⠀⠀⠀
    ⠀⠀⠀⣸⠀⠀⠀⠀⡇⠀⠀⠀⠳⢼⡦⢴⡯⠞⠀⠀⠀⢰⠀⠀⠀⠀⢧⠀⠀⠀  This place will redirect your browser
    ⠀⠀⠀⢻⠀⠀⠀⠀⡇⠀⠀⠀⢀⡤⠚⠛⢦⣀⠀⠀⠀⢸⠀⠀⠀⠀⡼⠀⠀⠀  to the siteweb of tool that you choice
    ⠀⠀⠀⠈⠳⠤⠤⣖⣓⣒⣒⣒⣓⣒⣒⣒⣒⣚⣒⣒⣒⣚⣲⠤⠤⠖⠁⠀⠀    You can install it or view info about it. 
          

    1) MetasploitFramework (Network)

    2) SQLMap (GitHub)

    3) Hydra (Guide)

    4) Wireshark (GitHub)

    5) BurpSuite (Network)
    
    
    ~ $ '''))
    

    if peninput == 1:
        subprocess.call("clear")
        menu()
        chome = int(input(Fore.LIGHTRED_EX+'''
        
########################################### 
#                                         #
#   1) Open in Linux                      #
#                                         #
#   2) Open in Termux                     #
#                                         #
#                                         #
#   3) Go Back...                         #
#                                         #
###########################################
    
    ~ $ '''))
        if chome == 1:
            webbrowser.open("https://www.metasploit.com")
        if chome == 2:
            os.system("termux-open https://www.metasploit.com")
        if chome == 3:
            return pentools()
    
    if peninput == 2:
        subprocess.call("clear")
        menu()
        chosq = int(input(Fore.LIGHTRED_EX+'''
        
########################################### 
#                                         #
#   1) Open in Linux                      #
#                                         #
#   2) Open in Termux                     #
#                                         #
#                                         #
#   3) Go Back...                         #
#                                         #
###########################################
    
    ~ $ '''))
        if chosq == 1:
            webbrowser.open("https://sqlmap.org")
        if chosq == 2:
            os.system("termux-open https://sqlmap.org")
        if chosq == 3:
            return pentools()
        
    if peninput == 3:
        subprocess.call("clear")
        menu()
        chohy = int(input(Fore.LIGHTRED_EX+'''
        
########################################### 
#                                         #
#   1) Open in Linux                      #
#                                         #
#   2) Open in Termux                     #
#                                         #
#                                         #
#   3) Go Back...                         #
#                                         #
###########################################
    
    ~ $ '''))
        if chohy == 1:
            webbrowser.open("https://www.kali.org/tools/hydra/")
        if chohy == 2:
            os.system("termux-open https://www.kali.org/tools/hydra")
        if chohy == 3:
            return pentools()
    
    if peninput == 4:
        subprocess.call("clear")
        menu()
        chowi = int(input(Fore.LIGHTRED_EX+'''
        
########################################### 
#                                         #
#   1) Open in Linux                      #
#                                         #
#   2) Open in Termux                     #
#                                         #
#                                         #
#   3) Go Back...                         #
#                                         #
###########################################
    
    ~ $ '''))
        if chowi == 1:
            webbrowser.open("https://www.wireshark.org")
        if chowi == 2:
            os.system("termux-open https://www.wireshark.org")
        if chowi == 3:
            return pentools()
            
    if peninput == 5:
        subprocess.call("clear")
        menu()
        chobu = int(input(Fore.LIGHTRED_EX+'''
        
########################################### 
#                                         #
#   1) Open in Linux                      #
#                                         #
#   2) Open in Termux                     #
#                                         #
#                                         #
#   3) Go Back...                         #
#                                         #
###########################################
    
    ~ $ '''))
        if chobu == 1:
            webbrowser.open("https://www.kali.org/tools/burpsuite")
        if chobu == 2:
            os.system("termux-open https://www.kali.org/tools/burpsuite")
        if chobu == 3:
            return pentools()
        
def searchuser():
    subprocess.call("clear")
    menu()
    suinput = int(input(Fore.BLUE+f'''
    
    TechnoDox - Search Username / OSINT Username

      XXX                        XXX
    XXXXX                        XXXXX
     XXXXXXXXXX             XXXXXXXXXX
             XXXXX     XXXXX
                 XXXXXXX
             XXXXX     XXXXX
     XXXXXXXXXX             XXXXXXXXXX
    XXXXX                        XXXXX
      XXX                        XXX
        
        1) Automatized search in Social media sites (BETA)
                        
 {Fore.LIGHTWHITE_EX} WARNING: Can may be failures in process.

        ~ $ '''))

    if suinput == 1:
        
        target = str(input(Fore.RED+'''
        
    
                    .-"      "-.
                  /            
                 |              |
                 |,  .-.  .-.  ,|       All most visited social media sites
                 | )(_o/  \o_)( |            will be scanned looking 
                 |/     /\     \|            the target on the tool.
       (@_       (_     ^^     _)
  _     ) \_______\__|IIIIII|__/__________________________
 (_)@8@8{}<________|-\IIIIII/-|___________________________>     SEARCHER
        )_/        \          /
       (@           `--------`                  

     
                    
            
        
        Type a Target: '''))

        sms = [f"https://github.com/{target}", f"https://replit.com/@{target}", f"https://twitter.com/{target}", f"https://instagram.com/{target}", f"https://www.pinterest.com/{target}", f"https://www.reddit.com/user/{target}", f"https://xboxgamertag.com/search/{target}", f"https://open.spotify.com/user/{target}", f"https://www.twitch.tv/{target}", f"https://www.roblox.com/user.aspx?username={target}", f"https://t.me/{target}", f"https://www.youtube.com/user/{target}", f"https://www.codecademy.com/profiles/{target}", f"https://forum.hackthebox.eu/profile/{target}"]

        for link in sms:
            req = requests.get(link)
            rsl = re.findall(target, req.text)
            if rsl:
                print(Fore.GREEN+f" - Target has been finded in {link}")
            else: 
                print(Fore.RED+' - Target not found in ')

def phonesearch():
    searchinput = int(input('''
    
          ⣀⣠⠤⠶⠶⣖⡛⠛⠿⠿⠯⠭⠍⠉⣉⠛⠚⠛⠲⣄⠀⠀⠀⠀⠀
    ⠀⠀⢀⡴⠋⠁⠀⡉⠁⢐⣒⠒⠈⠁⠀⠀⠀⠈⠁⢂⢅⡂⠀⠀⠘⣧⠀⠀⠀⠀
    ⠀⠀⣼⠀⠀⠀⠁⠀⠀⠀⠂⠀⠀⠀⠀⢀⣀⣤⣤⣄⡈⠈⠀⠀⠀⠘⣇⠀⠀⠀
    ⢠⡾⠡⠄⠀⠀⠾⠿⠿⣷⣦⣤⠀⠀⣾⣋⡤⠿⠿⠿⠿⠆⠠⢀⣀⡒⠼⢷⣄⠀      LOOK for the INFO 
    ⣿⠊⠊⠶⠶⢦⣄⡄⠀⢀⣿⠀⠀⠀⠈⠁⠀⠀⠙⠳⠦⠶⠞⢋⣍⠉⢳⡄⠈⣧       in a PHONENUMBER
    ⢹⣆⡂⢀⣿⠀⠀⡀⢴⣟⠁⠀⢀⣠⣘⢳⡖⠀⠀⣀⣠⡴⠞⠋⣽⠷⢠⠇⠀⣼          too easy...
    ⠀⢻⡀⢸⣿⣷⢦⣄⣀⣈⣳⣆⣀⣀⣤⣭⣴⠚⠛⠉⣹⣧⡴⣾⠋⠀⠀⣘⡼⠃
    ⠀⢸⡇⢸⣷⣿⣤⣏⣉⣙⣏⣉⣹⣁⣀⣠⣼⣶⡾⠟⢻⣇⡼⠁⠀⠀⣰⠋⠀⠀
    ⠀⢸⡇⠸⣿⡿⣿⢿⡿⢿⣿⠿⠿⣿⠛⠉⠉⢧⠀⣠⡴⠋⠀⠀⠀⣠⠇⠀⠀⠀
    ⠀⢸⠀⠀⠹⢯⣽⣆⣷⣀⣻⣀⣀⣿⣄⣤⣴⠾⢛⡉⢄⡢⢔⣠⠞⠁⠀⠀⠀⠀
    ⠀⢸⠀⠀⠀⠢⣀⠀⠈⠉⠉⠉⠉⣉⣀⠠⣐⠦⠑⣊⡥⠞⠋⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⡀⠀⠁⠂⠀⠀⠀⠀⠀⠀⠒⠈⠁⣀⡤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠙⠶⢤⣤⣤⣤⣤⡤⠴⠖⠚⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

###########################################
#                                         #
#                                         #
#   1) RevealName (Network)               #
#                                         #
#                                         #
#   2) Phonenumbers method... (SOON)      #
#                                         #
###########################################

    ~ $ '''))

    if searchinput == 1:
        subprocess.call("clear")
        menu()
        searchlot = int(input(Fore.RED+'''

########################################### 
#                                         #
#   1) Open in Linux                      #
#                                         #
#   2) Open in Termux                     #
#                                         #
#                                         #
#   3) Go Back...                         #
#                                         #
###########################################

    ~ $ '''))
        if searchlot == 1:
            webbrowser.open("https://phoneinfoga.en.softonic.com")
        if searchlot == 2:
            os.system("termux-open https://phoneingoga.en.softonic.com")
        if searchlot == 3:
            return phonesearch()
        

if menuinput == 1:
    osintools()
if menuinput == 2:
    securitytools()
if menuinput == 3:
    iploggers()
if menuinput == 4:
    pentools()
if menuinput == 5:
    searchuser()
if menuinput == 6:
    phonesearch()
if menuinput == 7:
    print("This option will be disponible soon...")


### if ###
