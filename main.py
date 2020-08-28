import uuid, socket, ipaddress, webbrowser, platform, os, time, requests, random, sys, ctypes
from colorama import init, Fore; init()
from random import *
import json
from os import system, path
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
if platform.system() == 'Windows':
    clear = lambda: os.system('clr') # Change to 'clear' if not on Windows.
    init()
else:
    clear = lambda: os.system('clear') # Change to 'clear' if not on Windows.
    init()
clear()
print('What language do you speak!')
language = input('English:Deutsche:日本人:中文:русский:svenska: ')
if language == 'English':
    clear()
    print('Tools pack')
    time.sleep(1)
    print('Detecting ip...')
    x = randint(1, 4)
    time.sleep(x)
    print(f'{ip_address} Has been detected')  # Done it is not the users ip it will defult to 127.0.0.1
    x = randint(1, 4)
    print('Detecting Hostname')
    time.sleep(x)
    print(f"Hostname: {hostname}")
    time.sleep(1)
    x = randint(1, 4)
    print('Checking OS...')
    time.sleep(x)
    zxc = platform.system()
    if zxc == 'Darwin':
        abcdef = 'Macosx'
        print(abcdef + ',' + (platform.release()) + ' ' + 'Detected')
    else:
        print(platform.system() + ',' + (platform.release()) + ' ' + 'Detected')

    time.sleep(1)
    if platform.system() == 'Linux':
        print('Linux OS is not a valid os for the tool pack and is getting worked on!')
        time.sleep(1)
        a = int(input('Type any number for a surprise! '))
        if a >= 1:
            for _ in range(a):
                webbrowser.open(url='https://www.youtube.com/watch?v=oHg5SJYRHA0', new=1)
            time.sleep(3)
            print("TERMINATING NOW!")
            time.sleep(5)
            exit()
    clear()
    inad = input('Have your paid/boost for the Program. Y:paid/Y:boosted/N: ')
    pop = 10
    while pop < 20:
        if inad == 'Y:paid':
            print('')
            print('Paid user login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/scPbt4D4')
            username = input('Username: ')
            time.sleep(1)
            print('')
            password = input('Password: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Correct password and username!')
                    time.sleep(1)
                    print('')
                    print('Sharing passwords are a bannable offence and will be removed from the list without refund!')
                    print('')
                    break
                else:
                    print('Invalid password or username!')
                    exita = input('Would like to re-try? Y/N: ')
                    if (exita.capitalize()) == 'Y':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Invalid Response!')
        elif inad == 'Y:boosted':
            print('')
            print('Booster user login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/c254wxqt')
            username = input('Username: ')
            time.sleep(1)
            print('')
            password = input('Password: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Correct password and username!')
                    time.sleep(1)
                    print('')
                    print('Sharing passwords are a bannable offence and will be removed from the list!')
                    print('')
                    break
                else:
                    print('Invalid password or username!')
                    exita = input('Would like to re-try? Y/N: ')
                    if (exita.capitalize()) == 'Y':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Invalid Response!')
        elif (inad.capitalize()) == 'N':
            time.sleep(1)
            i = input('Would you like a uuid? this is required to purchase the full version. Y/N: ')
            if (i.capitalize()) == 'Y':
                time.sleep(1)
                print(uuid.uuid1())
                time.sleep(1)
                print('')
                print('Keep this stored as it will be your password until you request it to get changed!')
                print('')
                time.sleep(5)
            print(
                'Would you like to join the discord server? You can buy the full version there and also boosters will get more tools!')
            discord = input('Y/N? ')
            if (discord.capitalize()) == 'Y':
                webbrowser.open(url='https://discord.gg/WWWhj9z')
            break
        else:
            time.sleep(1)
            print('Invalid response!')
            time.sleep(1)
            break

    print('N Selected!')
    time.sleep(1)
    clear()
    print('Free version, No booster or paid tools')
    time.sleep(1)
    print('')
    pastebin12 = ('https://pastebin.com/9qNWLYbb')
    kid = 1
    webbrowser.open_new(url='https://bit.ly/3lahict')
    print('Key Stop 1 & 2!')
    paswword = input('Key 1: ')
    passwwword = input('Key 2: ')
    key12 = requests.get(pastebin12).text
    for line in key12.split('\n'):
        if paswword and passwwword in line:
            print('Keys Are valid')
            time.sleep(1)
            print('')
            print('Thank you for helping support me!')
            print('Doing this is how you can access this for free!')
            break
    print('Loading')
    xa = randint(3, 10)
    time.sleep(xa)
    do_stuff = 0
    amount = 100

    for x in range(amount):
        done = (((x + .1) / amount))
       
        do_stuff += 0.1 # Process will be quick.
        if done == 0.1:
            clear()
            print(f'{Fore.GREEN}■{Fore.WHITE}■■■■■■■■■ ' + str(int(done * 100)) + '%')
        elif done == 0.2:
            clear()
            print(f'{Fore.GREEN}■■{Fore.WHITE}■■■■■■■■ ' + str(int(done * 100)) + '%')
        elif done == 0.3:
            clear()
            print(f'{Fore.GREEN}■■■{Fore.WHITE}■■■■■■■ ' + str(int(done * 100)) + '%')
        elif done == 0.4:
            clear()
            print(f'{Fore.GREEN}■■■■{Fore.WHITE}■■■■■■ ' + str(int(done * 100)) + '%')
        elif done == 0.5:
            clear()
            print(f'{Fore.GREEN}■■■■■{Fore.WHITE}■■■■■ ' + str(int(done * 100)) + '%')
        elif done == 0.6:
            clear()
            print(f'{Fore.GREEN}■■■■■■{Fore.WHITE}■■■■ ' + str(int(done * 100)) + '%')
        elif done == 0.7:
            clear()
            print(f'{Fore.GREEN}■■■■■■■{Fore.WHITE}■■■ ' + str(int(done * 100)) + '%')
        elif done == 0.8:
            clear()
            print(f'{Fore.GREEN}■■■■■■■■{Fore.WHITE}■■ ' + str(int(done * 100)) + '%')
        elif done == 0.9:
            clear()
            print(f'{Fore.GREEN}■■■■■■■■■{Fore.WHITE}■ ' + str(int(done * 100)) + '%')
        elif done == 1.0:
            clear()
            print(f'{Fore.GREEN}■■■■■■■■■■ ' + str(int(done * 100)) + '%')
      
    time.sleep(0.5)
    
    print(f'{Fore.WHITE}Complete!')


    while True:
        time.sleep(2)
        clear()

        print('  88888             8    888b.           8 ')
        print("    8   .d8b. .d8b. 8    8  .8 .d88 .d8b 8.dP ")
        print("    8   8' .8 8' .8 8    8wwP' 8  8 8    88b  ")
        print("    8   `Y8P' `Y8P' 8    8     `Y88 `Y8P 8 Yb ")
        time.sleep(2)
        print('By sɹǝƃƃod#5183')
        print('Credit to: zoony#1337 & Dropout#1337')
        print('')
        print("I am legaly not responsibile for anything that happens to you or your device! ")
        print('')
        time.sleep(1)
        print('1. Pinging tools: ')
        time.sleep(1)
        print('2. Browser history spammer: ')
        time.sleep(1)
        print('3. Computer destroyer: ')
        time.sleep(1)
        print('4. Discord spammer: ')
        time.sleep(1)
        print("5. 'Russian Rullette'")
        time.sleep(1)
        print('6. Other: ')
        time.sleep(1)
        print('7. Exit: ')
        time.sleep(2)
        a = int(input('Choose a Tool: '))
        if a == 1:
            print('1. Pinging tools selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            
            print(
            "██▓███   ██▓ ███▄    █   ▄████  ██▓ ███▄    █   ▄████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████")
            print(
            "▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▓██▒ ██ ▀█   █  ██▒ ▀█▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒")
            print(
                "▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄")
            print(
                "▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓░██░▓██▒  ▐▌██▒░▓█  ██▓   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒")
            print(
                 "▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒░██░▒██░   ▓██░░▒▓███▀▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒")
            print(
             "▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░")
            print(
               "░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░  ▒ ░░ ░░   ░ ▒░  ░   ░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░")
            print(
                "░░        ▒ ░   ░   ░ ░ ░ ░   ░  ▒ ░   ░   ░ ░ ░ ░   ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░")
            print("░           ░       ░  ░           ░       ░                 ░ ░      ░ ░      ░  ░      ░")
            print('')
            print('')
            print('')
            time.sleep(1)
            print('1. Ip/Sever tester')
            time.sleep(1)
            print('2. Ip Stresser')
            time.sleep(1)
            dos = int(input("Select a tool: "))
            if dos == 1:
                print('1. IP/Sever Tester selected!')
                print('.............................................................................................................')
                clear()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
                server_ip = input('Enter server IP : ')
                rep = os.system('ping ' + server_ip)
                if rep == 0:
                     print('The server is up')
                     clear()
                        
                else:
                    print('server/ip is down')
                    time.sleep(1)
                    print('Returning!')
                        

                

        elif a == 2:
            print('2. Browser history spammer selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(1)
            clear()
            time.sleep(3)
            print(
                '▄▄▄▄    ██▀███   ▒█████   █     █░  ██████ ▓█████  ██▀███      ██░ ██  ██▓  ██████ ▄▄▄█████▓ ▒█████   ██▀███ ▓██   ██▓     ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███ ')
            print(
                '▓█████▄ ▓██ ▒ ██▒▒██▒  ██▒▓█░ █ ░█░▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒   ▓██░ ██▒▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒   ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒')
            print(
                '▒██▒ ▄██▓██ ░▄█ ▒▒██░  ██▒▒█░ █ ░█ ░ ▓██▄   ▒███   ▓██ ░▄█ ▒   ▒██▀▀██░▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒')
            print(
                '▒██░█▀  ▒██▀▀█▄  ▒██   ██░░█░ █ ░█   ▒   ██▒▒▓█  ▄ ▒██▀▀█▄     ░▓█ ░██ ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░     ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  ')
            print(
                '░▓█  ▀█▓░██▓ ▒██▒░ ████▓▒░░░██▒██▓ ▒██████▒▒░▒████▒░██▓ ▒██▒   ░▓█▒░██▓░██░▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒')
            print(
                '░▒▓███▀▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▓░▒ ▒  ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░    ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░')
            print(
                '▒░▒   ░   ░▒ ░ ▒░  ░ ▒ ▒░   ▒ ░ ░  ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░    ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░')
            print(
                '░ ░ ░ ░ ▒    ░   ░  ░  ░  ░     ░     ░░   ░     ░  ░░ ░ ▒ ░░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░     ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ ')
            print(
                '  ░ ░      ░          ░     ░  ░   ░         ░  ░  ░ ░        ░               ░ ░     ░     ░ ░              ░                 ░  ░       ░          ░      ░  ░   ░     ')
            print(
                '     ░                                                                                                        ░ ░          ')
            for _ in range(3):
                time.sleep(0.2)
                print(' ')
            print(
                '.............................................................................................................................................................................................')
            print(' ')
            time.sleep(1)
            print('1. Random Google Page')
            time.sleep(1)
            print('2. Random Website')
            time.sleep(1)
            print('3. Selected Website')
            time.sleep(1)
            print('4. Exit Tool')
            time.sleep(1)
            c = int(input('Choose Tool: '))
            if c == 1:
                clear()
                
                print('1. Random google page selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    google_sites = ('search?q=nut&oq=nut&aqs=chrome.0.69i59.1970j0j7&sourceid=chrome&ie=UTF-8')
                elif select == 2:
                    google_sites = (
                        'search?q=history&oq=his&aqs=chrome.1.69i57j69i59l2j69i61j69i60.2720j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 3:
                    google_sites = (
                        'search?q=Yeet&oq=Yeet&aqs=chrome..69i57j69i60j69i65.1465j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 4:
                    google_sites = ('search?q=egg&oq=egg&aqs=chrome..69i57.686j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 5:
                    google_sites = (
                        'search?q=north+korea&oq=north+korea&aqs=chrome..69i57.2612j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 6:
                    google_sites = (
                        'search?q=computer&oq=computer&aqs=chrome..69i57j69i61l2j69i65l2j69i61.1695j0j9&sourceid=chrome&ie=UTF-8')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)

                for _ in range(pages):
                    webbrowser.open(url=('https://www.google.com/' + google_sites), new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 2:
                clear()
                print('2. Random website selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    random_sites = ('https://alwaysjudgeabookbyitscover.com/')
                elif select == 2:
                    random_sites = ('http://eelslap.com/')
                elif select == 3:
                    random_sites = ('https://smashthewalls.com/')
                elif select == 4:
                    random_sites = ('https://weirdorconfusing.com/')
                elif select == 5:
                    random_sites = ('https://trypap.com/')
                elif select == 6:
                    random_sites = ('http://www.republiquedesmangues.fr/')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)
                for _ in range(pages):
                    webbrowser.open(url=random_sites, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 3:
                clear()
                print('3. Selected website!')
                pages = int(input('How Many Tabs: '))
                website = input('Website, You dont need http/s: ')
                for _ in range(pages):
                    webbrowser.open(url='http://' + website, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 4:
                clear()
                print('Exitting!!!')
                time.sleep(1)
            else:
                print('Wrong, That option does not exist!')
                time.sleep(1)
                print('Returning to menu!')
                time.sleep(1)

        elif a == 3:
            print('3. Computer Destoryer Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            clear()
            zx = input('Are you sure Y/N: ')
            if (zx.capitalize()) == 'Y':
                time.sleep(1)
                print('Destroyer Starting in 3 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 2 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 1 seconds!')
                time.sleep(1)
                for _ in range(1000):
                    webbrowser.open(url='https://www.youtube.com/watch?v=i_2yNbIzwOI', new=2)
            else:
                print('')
                print('Returning to main menu!')
                time.sleep(1)

        elif a == 4:
            print('4. Discord Tools selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
            time.sleep(.1)
            print(
                    "              dddddddd                                                                                              dddddddd         ")
            print(
                    "              d::::::d  iiii                                                                                        d::::::d              tttt                                            lllllll  ")
            print(
                    "              d::::::d i::::i                                                                                       d::::::d           ttt:::t                                            l:::::l    ")
            print(
                    "              d::::::d  iiii                                                                                        d::::::d           t:::::t                                            l:::::l      ")
            print(
                    "              d:::::d                                                                                               d:::::d            t:::::t                                            l:::::l    ")
            print(
                    "      ddddddddd:::::d iiiiiii     ssssssssss       cccccccccccccccc   ooooooooooo   rrrrr   rrrrrrrrr       ddddddddd:::::d      ttttttt:::::ttttttt       ooooooooooo      ooooooooooo    l::::l     ssssssssss  ")
            print(
                    "     dd::::::::::::::d i:::::i   ss::::::::::s    cc:::::::::::::::c oo:::::::::::oo r::::rrr:::::::::r    dd::::::::::::::d      t:::::::::::::::::t     oo:::::::::::oo  oo:::::::::::oo  l::::l   ss::::::::::s  ")
            print(
                    "    d::::::::::::::::d  i::::i ss:::::::::::::s  c:::::::::::::::::co:::::::::::::::or:::::::::::::::::r  d::::::::::::::::d      t:::::::::::::::::t    o:::::::::::::::oo:::::::::::::::o l::::l ss:::::::::::::s ")
            print(
                    "   d:::::::ddddd:::::d  i::::i s::::::ssss:::::sc:::::::cccccc:::::co:::::ooooo:::::orr::::::rrrrr::::::rd:::::::ddddd:::::d      tttttt:::::::tttttt    o:::::ooooo:::::oo:::::ooooo:::::o l::::l s::::::ssss:::::s ")
            print(
                    "   d::::::d    d:::::d  i::::i  s:::::s  ssssss c::::::c     ccccccco::::o     o::::o r:::::r     r:::::rd::::::d    d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l  s:::::s  ssssss ")
            print(
                    "   d:::::d     d:::::d  i::::i    s::::::s      c:::::c             o::::o     o::::o r:::::r     rrrrrrrd:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l    s::::::s  ")
            print(
                    "   d:::::d     d:::::d  i::::i       s::::::s   c:::::c             o::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l       s::::::s  ")
            print(
                    "   d:::::d     d:::::d  i::::i ssssss   s:::::s c::::::c     ccccccco::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t    tttttto::::o     o::::oo::::o     o::::o l::::l ssssss   s:::::s ")
            print(
                    "   d::::::ddddd::::::ddi::::::is:::::ssss::::::sc:::::::cccccc:::::co:::::ooooo:::::o r:::::r            d::::::ddddd::::::dd           t::::::tttt:::::to:::::ooooo:::::oo:::::ooooo:::::ol::::::ls:::::ssss::::::s")
            print(
                    "    d:::::::::::::::::di::::::is::::::::::::::s  c:::::::::::::::::co:::::::::::::::o r:::::r             d:::::::::::::::::d           tt::::::::::::::to:::::::::::::::oo:::::::::::::::ol::::::ls::::::::::::::s ")
            print(
                    "     d:::::::::ddd::::di::::::i s:::::::::::ss    cc:::::::::::::::c oo:::::::::::oo  r:::::r              d:::::::::ddd::::d             tt:::::::::::tt oo:::::::::::oo  oo:::::::::::oo l::::::l s:::::::::::ss  ")
            print(
                    "     ddddddddd   dddddiiiiiiii  sssssssssss        cccccccccccccccc   ooooooooooo    rrrrrrr               ddddddddd   ddddd               ttttttttttt     ooooooooooo      ooooooooooo   llllllll  sssssssssss     ")
            for _ in range(2):
                print(' ')
            print('If You get banned on discord it is not my fault!')
            print('3 & 4  can result if caught in a ban!')
            for _ in range(2):
                print(' ')
            print('1. Custom discord status')
            print('2. Text spammer')
            print('3. Multi message delete')
            print('4. Token login')
            ex = int(input('Select A Tool:'))
            if ex == 1:
                print(
                        "....................................................................................................")
                clear()
            elif ex == 2:
                    print(
                        "....................................................................................................")
                    clear()
            elif ex == 3:
                print(
                        "....................................................................................................")
                clear()
            elif ex == 4:
                print('3. Multi message delete selected!')
                print(
                        "....................................................................................................")
                clear()
                    
                with open('token.txt', 'r', encoding='UTF-8') as f: token = f.read()
                num = 0

                words = ['http://discord.zoony.xyz', 'http://zoony.xyz', 'https://lnky.in/lifty']
                emoji_id = '704103059969671260'
                emoji_name = 'LiftyCommunity'

                headers = {
                    'Authorization': token,
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
                    'Content-Type': 'application/json',
                    'Accept': '*/*'
                    }

                while True:
                    for x in range(3):
                        try:
                            data = {'custom_status':{'text':words[x],'emoji_id':emoji_id,'emoji_name':emoji_name}}
                            r = requests.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, json=data)
                            if "'code': 0" in r.text: print(f'{Fore.RED}Invalid/outdated token{Fore.WHITE}.'); time.sleep(600); os._exit(0)
                            else: print(f'{Fore.GREEN}Edited status to{Fore.WHITE}: {words[x]}'); num += 1; ctypes.windll.kernel32.SetConsoleTitleW(f'Edited: {num} times'); time.sleep(5)
                        except:
                            pass
                print("If it does not work the either contact sɹǝƃƃod#5183 or zoony#1337")
                print('You need to put the token into the token.txt')
                time.sleep(1)

            else:
                time.sleep(1)
                print(
                        "....................................................................................................")
                time.sleep(1)
                print('Invalid command!')
                time.sleep(1)
                print('Returning home!')
                time.sleep(1)

        elif a == 5:
            print("5.'Russian Rullette' Selected ")  # gotto work on this
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            clear()
            print('Russian rullette is a game that you will select a number and something may happen to your device!')
            print('Choose the right number or you may destroy your device')
            time.sleep(1)
            zxfd = randint(1,9)
            abcsa = int(input('Select a number between 1-9: '))
            if abcsa == zxfd:
                if platform.system() == 'Windows':
                    os.system("cd c:\windows\system32")
                    os.system('del *')
                elif platform.system() == 'Darwin':
                    os.system('echo hello')

        elif a == 6:
            print('6. Other Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            clear()
        elif a == 7:
            print('7. Exit Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            clear()
            time.sleep(3)
            b = input('You sure? Y/N: ')
            if (b.capitalize()) == 'Y':
                print('Terminating in 10 seconds')
                time.sleep(5)
                print('Terminating in 5 seconds!')
                time.sleep(1)
                print('Terminating in 4 seconds!')
                time.sleep(1)
                print('Terminating in 3 seconds!')
                time.sleep(1)
                print('Terminating in 2 seconds!')
                time.sleep(1)
                print('Terminating in 1 seconds!')
                time.sleep(1)
                print('TERMINATED')
                exit()
elif language == 'Deutsche': #german may need to re do it 
    print('Werkzeugpaket')
    time.sleep(1)
    print('IP erkennen ...')
    x = randint(1, 4)
    time.sleep(x)
    print('---.---.---.-' + ' Wurde entdeckt')  # still working on it
    time.sleep(1)
    x = randint(1, 4)
    print('Betriebssystem überprüfen ...')
    time.sleep(x)
    zxc = platform.system()
    if zxc == 'Darwin':
        abcdef = 'Mac OS X'
        print(abcdef + ',' + (platform.release()) + ' ' + 'Erkannt')
    else:
        print(platform.system() + ',' + (platform.release()) + ' ' + 'Erkannt')

    time.sleep(1)
    for _ in range(3):
        print('')
        time.sleep(.1)
    if platform.system() == 'Linux':
        print('Linux OS ist kein gültiges Betriebssystem für das Tool Pack und wird gerade bearbeitet!')
        time.sleep(1)
        a = int(input('Geben Sie eine beliebige Zahl für eine Überraschung ein: '))
        if a >= 1:
            for _ in range(a):
                webbrowser.open(url='https://www.youtube.com/watch?v=oHg5SJYRHA0', new=1)
            time.sleep(3)
            print("TERMINATING NOW!")
            time.sleep(5)
            exit()
    inad = input('Lassen Sie sich für das Programm bezahlen / steigern. J:bezahlt/J:verstärkt/N: ')
    pop = 10
    while pop < 20:
        if inad == 'J:bezahlt':
            print('')
            print('Bezahlter Benutzer Login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/scPbt4D4')
            username = input('Nutzername: ')
            time.sleep(1)
            print('')
            password = input('Passwort: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Passwort und Benutzername korrigieren!')
                    time.sleep(1)
                    print('')
                    print('Das Teilen von Passwörtern ist strafbar und wird ohne Rückerstattung von der Liste gestrichen!')
                    print('')
                    break
                else:
                    print('Ungültiges Passwort oder Benutzername!')
                    exita = input('Möchten Sie es erneut versuchen? J / N:')
                    if (exita.capitalize()) == 'J':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Invalid Response!')
        elif inad == 'J:verstärkt':
            print('')
            print('Booster Benutzer Login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/c254wxqt')
            username = input('Nutzername: ')
            time.sleep(1)
            print('')
            password = input('Passwort: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Passwort und Benutzername korrigieren')
                    time.sleep(1)
                    print('') #dumb ass german
                    print('Das Teilen von Passwörtern ist strafbar und wird ohne Rückerstattung von der Liste gestrichen!')
                    print('')
                    break
                else:
                    print('Ungültiges Passwort oder Benutzername!')
                    exita = input('Möchten Sie es erneut versuchen? J / N:')
                    if (exita.capitalize()) == 'Y':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Ungültige Antwort!')
        elif (inad.capitalize()) == 'N':
            time.sleep(1)
            i = input('Möchten Sie eine UUID? Dies ist erforderlich, um die Vollversion zu erwerben. J / N:')
            if (i.capitalize()) == 'J':
                time.sleep(1)
                print(uuid.uuid1())
                time.sleep(1)
                print('')
                print('Bewahren Sie dieses auf, da es Ihr Passwort ist, bis Sie es auffordern, geändert zu werden!')
                print('')
                time.sleep(5)
            print(
                'Möchten Sie dem Discord-Server beitreten? Sie können dort die Vollversion kaufen und auch Booster erhalten mehr Werkzeuge!')
            discord = input('J/N? ')
            if (discord.capitalize()) == 'J':
                webbrowser.open(url='https://discord.gg/WWWhj9z')
            break
        else:
            time.sleep(1)
            print('Ungültige Antwort!')
            time.sleep(1)
            break

    print('N Ausgewählt!')
    time.sleep(1)
    print('Kostenlose Version, kein Booster oder kostenpflichtige Tools')
    time.sleep(1)
    print('')
    pastebin12 = ('https://pastebin.com/9qNWLYbb')
    kid = 1
    webbrowser.open_new(url='https://bit.ly/3lahict')
    print('Schlüsselstopp 1 & 2!')
    key1 = input('Schlüssel 1: ')
    key2 = input('Schlüssel 2: ')
    key12 = requests.get(pastebin12).text
    for line in key12.split('\n'):
        if key12 and key2 in line:
            print('Schlüssel sind gültig')
            time.sleep(1)
            print('')
            print('Vielen Dank für Ihre Unterstützung!')
            print('')
    print('Wird geladen!')
    x = randint(3, 10)
    time.sleep(x)
    print('(##########)100% KOMPLETT!')
    time.sleep(0.5)
    print('Complete!')

    while True:
        time.sleep(2)
        for _ in range(40):
            print(' ')
            time.sleep(.01)

        print('  88888             8    888b.           8 ')
        print("    8   .d8b. .d8b. 8    8  .8 .d88 .d8b 8.dP ")
        print("    8   8' .8 8' .8 8    8wwP' 8  8 8    88b  ")
        print("    8   `Y8P' `Y8P' 8    8     `Y88 `Y8P 8 Yb ")
        time.sleep(2)
        print('By sɹǝƃƃod#5183')
        print('Credit to: zoony#1337 & Dropout#1337')
        print('')
        print("I am legaly not responsibile for anything that happens to you or your device! ")
        print('')
        time.sleep(1)
        print('1. Pinging tools: ')
        time.sleep(1)
        print('2. Browser history spammer: ')
        time.sleep(1)
        print('3. Computer destroyer: ')
        time.sleep(1)
        print('4. Discord spammer: ')
        time.sleep(1)
        print('5. Something idk')
        time.sleep(1)
        print('6. Other: ')
        time.sleep(1)
        print('7. Exit: ')
        time.sleep(2)
        a = int(input('Choose a Tool: '))
        if a == 1:
            print('1. Pinging tools selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
                print(
                    "██▓███   ██▓ ███▄    █   ▄████  ██▓ ███▄    █   ▄████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████")
                print(
                    "▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▓██▒ ██ ▀█   █  ██▒ ▀█▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒")
                print(
                    "▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄")
                print(
                    "▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓░██░▓██▒  ▐▌██▒░▓█  ██▓   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒")
                print(
                    "▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒░██░▒██░   ▓██░░▒▓███▀▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒")
                print(
                    "▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░")
                print(
                    "░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░  ▒ ░░ ░░   ░ ▒░  ░   ░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░")
                print(
                    "░░        ▒ ░   ░   ░ ░ ░ ░   ░  ▒ ░   ░   ░ ░ ░ ░   ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░")
                print("░           ░       ░  ░           ░       ░                 ░ ░      ░ ░      ░  ░      ░")
                print('')
                print('')
                print('')
                time.sleep(1)
                print('1. Ip/Sever tester')
                print('2. Ip Stresser')

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
                server_ip = int(input('Enter server IP : '))
                rep = os.system('ping ' + server_ip)
                if rep == 0:
                    print
                    'n n server is up n n'
                else:
                    print
                'server is down'

        elif a == 2:
            print('2. Browser history spammer selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(1)
            for _ in range(15):
                print(' ')
            time.sleep(3)
            print(
                '▄▄▄▄    ██▀███   ▒█████   █     █░  ██████ ▓█████  ██▀███      ██░ ██  ██▓  ██████ ▄▄▄█████▓ ▒█████   ██▀███ ▓██   ██▓     ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███ ')
            print(
                '▓█████▄ ▓██ ▒ ██▒▒██▒  ██▒▓█░ █ ░█░▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒   ▓██░ ██▒▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒   ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒')
            print(
                '▒██▒ ▄██▓██ ░▄█ ▒▒██░  ██▒▒█░ █ ░█ ░ ▓██▄   ▒███   ▓██ ░▄█ ▒   ▒██▀▀██░▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒')
            print(
                '▒██░█▀  ▒██▀▀█▄  ▒██   ██░░█░ █ ░█   ▒   ██▒▒▓█  ▄ ▒██▀▀█▄     ░▓█ ░██ ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░     ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  ')
            print(
                '░▓█  ▀█▓░██▓ ▒██▒░ ████▓▒░░░██▒██▓ ▒██████▒▒░▒████▒░██▓ ▒██▒   ░▓█▒░██▓░██░▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒')
            print(
                '░▒▓███▀▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▓░▒ ▒  ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░    ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░')
            print(
                '▒░▒   ░   ░▒ ░ ▒░  ░ ▒ ▒░   ▒ ░ ░  ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░    ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░')
            print(
                '░ ░ ░ ░ ▒    ░   ░  ░  ░  ░     ░     ░░   ░     ░  ░░ ░ ▒ ░░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░     ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ ')
            print(
                '  ░ ░      ░          ░     ░  ░   ░         ░  ░  ░ ░        ░               ░ ░     ░     ░ ░              ░                 ░  ░       ░          ░      ░  ░   ░     ')
            print(
                '     ░                                                                                                        ░ ░          ')
            for _ in range(3):
                time.sleep(0.2)
                print(' ')
            print(
                '.............................................................................................................................................................................................')
            print(' ')
            time.sleep(1)
            print('1. Random Google Page')
            time.sleep(1)
            print('2. Random Website')
            time.sleep(1)
            print('3. Selected Website')
            time.sleep(1)
            print('4. Exit Tool')
            time.sleep(1)
            c = int(input('Choose Tool: '))
            if c == 1:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('1. Random google page selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    google_sites = ('search?q=nut&oq=nut&aqs=chrome.0.69i59.1970j0j7&sourceid=chrome&ie=UTF-8')
                elif select == 2:
                    google_sites = (
                        'search?q=history&oq=his&aqs=chrome.1.69i57j69i59l2j69i61j69i60.2720j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 3:
                    google_sites = (
                        'search?q=Yeet&oq=Yeet&aqs=chrome..69i57j69i60j69i65.1465j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 4:
                    google_sites = ('search?q=egg&oq=egg&aqs=chrome..69i57.686j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 5:
                    google_sites = (
                        'search?q=north+korea&oq=north+korea&aqs=chrome..69i57.2612j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 6:
                    google_sites = (
                        'search?q=computer&oq=computer&aqs=chrome..69i57j69i61l2j69i65l2j69i61.1695j0j9&sourceid=chrome&ie=UTF-8')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)

                for _ in range(pages):
                    webbrowser.open(url=('https://www.google.com/' + google_sites), new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 2:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('2. Random website selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    random_sites = ('https://alwaysjudgeabookbyitscover.com/')
                elif select == 2:
                    random_sites = ('http://eelslap.com/')
                elif select == 3:
                    random_sites = ('https://smashthewalls.com/')
                elif select == 4:
                    random_sites = ('https://weirdorconfusing.com/')
                elif select == 5:
                    random_sites = ('https://trypap.com/')
                elif select == 6:
                    random_sites = ('http://www.republiquedesmangues.fr/')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)
                for _ in range(pages):
                    webbrowser.open(url=random_sites, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 3:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('3. Selected website!')
                pages = int(input('How Many Tabs: '))
                website = input('Website, You dont need http/s: ')
                for _ in range(pages):
                    webbrowser.open(url='http://' + website, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 4:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('Exitting!!!')
                time.sleep(1)
            else:
                print('Wrong, That option does not exist!')
                time.sleep(1)
                print('Returning to menu!')
                time.sleep(1)

        elif a == 3:
            print('3. Computer Destoryer Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
            zx = input('Are you sure Y/N: ')
            if (zx.capitalize()) == 'Y':
                time.sleep(1)
                print('Destroyer Starting in 3 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 2 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 1 seconds!')
                time.sleep(1)
                for _ in range(1000):
                    webbrowser.open(url='https://www.youtube.com/watch?v=i_2yNbIzwOI', new=2)
            else:
                print('')
                print('Returning to main menu!')
                time.sleep(1)

        elif a == 4:
            print('4. Discord Tools selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
                time.sleep(.1)
                print(
                    "              dddddddd                                                                                              dddddddd         ")
                print(
                    "              d::::::d  iiii                                                                                        d::::::d              tttt                                            lllllll  ")
                print(
                    "              d::::::d i::::i                                                                                       d::::::d           ttt:::t                                            l:::::l    ")
                print(
                    "              d::::::d  iiii                                                                                        d::::::d           t:::::t                                            l:::::l      ")
                print(
                    "              d:::::d                                                                                               d:::::d            t:::::t                                            l:::::l    ")
                print(
                    "      ddddddddd:::::d iiiiiii     ssssssssss       cccccccccccccccc   ooooooooooo   rrrrr   rrrrrrrrr       ddddddddd:::::d      ttttttt:::::ttttttt       ooooooooooo      ooooooooooo    l::::l     ssssssssss  ")
                print(
                    "     dd::::::::::::::d i:::::i   ss::::::::::s    cc:::::::::::::::c oo:::::::::::oo r::::rrr:::::::::r    dd::::::::::::::d      t:::::::::::::::::t     oo:::::::::::oo  oo:::::::::::oo  l::::l   ss::::::::::s  ")
                print(
                    "    d::::::::::::::::d  i::::i ss:::::::::::::s  c:::::::::::::::::co:::::::::::::::or:::::::::::::::::r  d::::::::::::::::d      t:::::::::::::::::t    o:::::::::::::::oo:::::::::::::::o l::::l ss:::::::::::::s ")
                print(
                    "   d:::::::ddddd:::::d  i::::i s::::::ssss:::::sc:::::::cccccc:::::co:::::ooooo:::::orr::::::rrrrr::::::rd:::::::ddddd:::::d      tttttt:::::::tttttt    o:::::ooooo:::::oo:::::ooooo:::::o l::::l s::::::ssss:::::s ")
                print(
                    "   d::::::d    d:::::d  i::::i  s:::::s  ssssss c::::::c     ccccccco::::o     o::::o r:::::r     r:::::rd::::::d    d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l  s:::::s  ssssss ")
                print(
                    "   d:::::d     d:::::d  i::::i    s::::::s      c:::::c             o::::o     o::::o r:::::r     rrrrrrrd:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l    s::::::s  ")
                print(
                    "   d:::::d     d:::::d  i::::i       s::::::s   c:::::c             o::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l       s::::::s  ")
                print(
                    "   d:::::d     d:::::d  i::::i ssssss   s:::::s c::::::c     ccccccco::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t    tttttto::::o     o::::oo::::o     o::::o l::::l ssssss   s:::::s ")
                print(
                    "   d::::::ddddd::::::ddi::::::is:::::ssss::::::sc:::::::cccccc:::::co:::::ooooo:::::o r:::::r            d::::::ddddd::::::dd           t::::::tttt:::::to:::::ooooo:::::oo:::::ooooo:::::ol::::::ls:::::ssss::::::s")
                print(
                    "    d:::::::::::::::::di::::::is::::::::::::::s  c:::::::::::::::::co:::::::::::::::o r:::::r             d:::::::::::::::::d           tt::::::::::::::to:::::::::::::::oo:::::::::::::::ol::::::ls::::::::::::::s ")
                print(
                    "     d:::::::::ddd::::di::::::i s:::::::::::ss    cc:::::::::::::::c oo:::::::::::oo  r:::::r              d:::::::::ddd::::d             tt:::::::::::tt oo:::::::::::oo  oo:::::::::::oo l::::::l s:::::::::::ss  ")
                print(
                    "     ddddddddd   dddddiiiiiiii  sssssssssss        cccccccccccccccc   ooooooooooo    rrrrrrr               ddddddddd   ddddd               ttttttttttt     ooooooooooo      ooooooooooo   llllllll  sssssssssss     ")
                for _ in range(2):
                    print(' ')
                print('If You get banned on discord it is not my fault!')
                print('3 & 4  can result if caught in a ban!')
                for _ in range(2):
                    print(' ')
                print('1. Custom discord status')
                print('2. Text spammer')
                print('3. Multi message delete')
                print('4. Token login')
                ex = int(input('Select A Tool:'))
                if ex == 1:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 2:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 3:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 4:
                    print('3. Multi message delete selected!')
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')


                else:
                    time.sleep(1)
                    print(
                        "....................................................................................................")
                    time.sleep(1)
                    print('Invalid command!')
                    time.sleep(1)
                    print('Returning home!')
                    time.sleep(1)

        elif a == 5:
            print('1. Pinging tools selected!')  # gotto work on this
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
        elif a == 6:
            print('6. Other Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
        elif a == 7:
            print('7. Exit Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
            time.sleep(3)
            b = input('You sure? Y/N: ')
            if (b.capitalize()) == 'Y':
                print('Terminating in 10 seconds')
                time.sleep(5)
                print('Terminating in 5 seconds!')
                time.sleep(1)
                print('Terminating in 4 seconds!')
                time.sleep(1)
                print('Terminating in 3 seconds!')
                time.sleep(1)
                print('Terminating in 2 seconds!')
                time.sleep(1)
                print('Terminating in 1 seconds!')
                time.sleep(1)
                print('TERMINATED')
                exit()
elif language == '日本人':#japanses
    print('Tools pack')
    time.sleep(1)
    print('Detecting ip...')
    x = randint(1, 4)
    time.sleep(x)
    print('---.---.---.-' + ' Has been detected')  # still working on it
    time.sleep(1)
    x = randint(1, 4)
    print('Checking OS...')
    time.sleep(x)
    zxc = platform.system()
    if zxc == 'Darwin':
        abcdef = 'Macosx'
        print(abcdef + ',' + (platform.release()) + ' ' + 'Detected')
    else:
        print(platform.system() + ',' + (platform.release()) + ' ' + 'Detected')

    time.sleep(1)
    for _ in range(3):
        print('')
        time.sleep(.1)
    if platform.system() == 'Linux':
        print('Linux OS is not a valid os for the tool pack and is getting worked on!')
        time.sleep(1)
        a = int(input('Type any number for a surprise! '))
        if a >= 1:
            for _ in range(a):
                webbrowser.open(url='https://www.youtube.com/watch?v=oHg5SJYRHA0', new=1)
            time.sleep(3)
            print("TERMINATING NOW!")
            time.sleep(5)
            exit()
    inad = input('Have your paid/boost for the Program. Y:paid/Y:boosted/N: ')
    pop = 10
    while pop < 20:
        if inad == 'Y:paid':
            print('')
            print('Paid user login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/scPbt4D4')
            username = input('Username: ')
            time.sleep(1)
            print('')
            password = input('Password: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Correct password and username!')
                    time.sleep(1)
                    print('')
                    print('Sharing passwords are a bannable offence and will be removed from the list without refund!')
                    print('')
                    break
                else:
                    print('Invalid password or username!')
                    exita = input('Would like to re-try? Y/N: ')
                    if (exita.capitalize()) == 'Y':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Invalid Response!')
        elif inad == 'Y:boosted':
            print('')
            print('Booster user login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/c254wxqt')
            username = input('Username: ')
            time.sleep(1)
            print('')
            password = input('Password: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Correct password and username!')
                    time.sleep(1)
                    print('')
                    print('Sharing passwords are a bannable offence and will be removed from the list!')
                    print('')
                    break
                else:
                    print('Invalid password or username!')
                    exita = input('Would like to re-try? Y/N: ')
                    if (exita.capitalize()) == 'Y':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Invalid Response!')
        elif (inad.capitalize()) == 'N':
            time.sleep(1)
            i = input('Would you like a uuid? this is required to purchase the full version. Y/N: ')
            if (i.capitalize()) == 'Y':
                time.sleep(1)
                print(uuid.uuid1())
                time.sleep(1)
                print('')
                print('Keep this stored as it will be your password until you request it to get changed!')
                print('')
                time.sleep(5)
            print(
                'Would you like to join the discord server? You can buy the full version there and also boosters will get more tools!')
            discord = input('Y/N? ')
            if (discord.capitalize()) == 'Y':
                webbrowser.open(url='https://discord.gg/WWWhj9z')
            break
        else:
            time.sleep(1)
            print('Invalid response!')
            time.sleep(1)
            break

    print('N Selected!')
    time.sleep(1)
    print('Free version, No booster or paid tools')
    time.sleep(1)
    print('')
    pastebin12 = ('https://pastebin.com/9qNWLYbb')
    kid = 1
    webbrowser.open_new(url='https://bit.ly/3lahict')
    print('Key Stop 1 & 2!')
    key1 = input('Key 1: ')
    key2 = input('Key 2: ')
    key12 = requests.get(pastebin12).text
    for line in key12.split('\n'):
        if key12 and key2 in line:
            print('Keys Are valid')
            time.sleep(1)
            print('')
            print('Thank you for helping support me!')
            print('')
        else:
            print('invalid')

    print('Loading')
    x = randint(3, 10)
    time.sleep(x)
    print('(##########)100% COMPLETE')
    time.sleep(0.5)
    print('Complete!')

    while True:
        time.sleep(2)
        for _ in range(40):
            print(' ')
            time.sleep(.01)

        print('  88888             8    888b.           8 ')
        print("    8   .d8b. .d8b. 8    8  .8 .d88 .d8b 8.dP ")
        print("    8   8' .8 8' .8 8    8wwP' 8  8 8    88b  ")
        print("    8   `Y8P' `Y8P' 8    8     `Y88 `Y8P 8 Yb ")
        time.sleep(2)
        print('By sɹǝƃƃod#5183')
        print('Credit to: zoony#1337 & Dropout#1337')
        print('')
        print("I am legaly not responsibile for anything that happens to you or your device! ")
        print('')
        time.sleep(1)
        print('1. Pinging tools: ')
        time.sleep(1)
        print('2. Browser history spammer: ')
        time.sleep(1)
        print('3. Computer destroyer: ')
        time.sleep(1)
        print('4. Discord spammer: ')
        time.sleep(1)
        print('5. Something idk')
        time.sleep(1)
        print('6. Other: ')
        time.sleep(1)
        print('7. Exit: ')
        time.sleep(2)
        a = int(input('Choose a Tool: '))
        if a == 1:
            print('1. Pinging tools selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
                print(
                    "██▓███   ██▓ ███▄    █   ▄████  ██▓ ███▄    █   ▄████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████")
                print(
                    "▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▓██▒ ██ ▀█   █  ██▒ ▀█▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒")
                print(
                    "▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄")
                print(
                    "▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓░██░▓██▒  ▐▌██▒░▓█  ██▓   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒")
                print(
                    "▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒░██░▒██░   ▓██░░▒▓███▀▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒")
                print(
                    "▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░")
                print(
                    "░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░  ▒ ░░ ░░   ░ ▒░  ░   ░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░")
                print(
                    "░░        ▒ ░   ░   ░ ░ ░ ░   ░  ▒ ░   ░   ░ ░ ░ ░   ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░")
                print("░           ░       ░  ░           ░       ░                 ░ ░      ░ ░      ░  ░      ░")
                print('')
                print('')
                print('')
                time.sleep(1)
                print('1. Ip/Sever tester')
                print('2. Ip Stresser')

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
                server_ip = int(input('Enter server IP : '))
                rep = os.system('ping ' + server_ip)
                if rep == 0:
                    print
                    'n n server is up n n'
                else:
                    print
                'server is down'

        elif a == 2:
            print('2. Browser history spammer selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(1)
            for _ in range(15):
                print(' ')
            time.sleep(3)
            print(
                '▄▄▄▄    ██▀███   ▒█████   █     █░  ██████ ▓█████  ██▀███      ██░ ██  ██▓  ██████ ▄▄▄█████▓ ▒█████   ██▀███ ▓██   ██▓     ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███ ')
            print(
                '▓█████▄ ▓██ ▒ ██▒▒██▒  ██▒▓█░ █ ░█░▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒   ▓██░ ██▒▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒   ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒')
            print(
                '▒██▒ ▄██▓██ ░▄█ ▒▒██░  ██▒▒█░ █ ░█ ░ ▓██▄   ▒███   ▓██ ░▄█ ▒   ▒██▀▀██░▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒')
            print(
                '▒██░█▀  ▒██▀▀█▄  ▒██   ██░░█░ █ ░█   ▒   ██▒▒▓█  ▄ ▒██▀▀█▄     ░▓█ ░██ ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░     ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  ')
            print(
                '░▓█  ▀█▓░██▓ ▒██▒░ ████▓▒░░░██▒██▓ ▒██████▒▒░▒████▒░██▓ ▒██▒   ░▓█▒░██▓░██░▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒')
            print(
                '░▒▓███▀▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▓░▒ ▒  ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░    ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░')
            print(
                '▒░▒   ░   ░▒ ░ ▒░  ░ ▒ ▒░   ▒ ░ ░  ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░    ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░')
            print(
                '░ ░ ░ ░ ▒    ░   ░  ░  ░  ░     ░     ░░   ░     ░  ░░ ░ ▒ ░░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░     ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ ')
            print(
                '  ░ ░      ░          ░     ░  ░   ░         ░  ░  ░ ░        ░               ░ ░     ░     ░ ░              ░                 ░  ░       ░          ░      ░  ░   ░     ')
            print(
                '     ░                                                                                                        ░ ░          ')
            for _ in range(3):
                time.sleep(0.2)
                print(' ')
            print(
                '.............................................................................................................................................................................................')
            print(' ')
            time.sleep(1)
            print('1. Random Google Page')
            time.sleep(1)
            print('2. Random Website')
            time.sleep(1)
            print('3. Selected Website')
            time.sleep(1)
            print('4. Exit Tool')
            time.sleep(1)
            c = int(input('Choose Tool: '))
            if c == 1:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('1. Random google page selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    google_sites = ('search?q=nut&oq=nut&aqs=chrome.0.69i59.1970j0j7&sourceid=chrome&ie=UTF-8')
                elif select == 2:
                    google_sites = (
                        'search?q=history&oq=his&aqs=chrome.1.69i57j69i59l2j69i61j69i60.2720j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 3:
                    google_sites = (
                        'search?q=Yeet&oq=Yeet&aqs=chrome..69i57j69i60j69i65.1465j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 4:
                    google_sites = ('search?q=egg&oq=egg&aqs=chrome..69i57.686j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 5:
                    google_sites = (
                        'search?q=north+korea&oq=north+korea&aqs=chrome..69i57.2612j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 6:
                    google_sites = (
                        'search?q=computer&oq=computer&aqs=chrome..69i57j69i61l2j69i65l2j69i61.1695j0j9&sourceid=chrome&ie=UTF-8')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)

                for _ in range(pages):
                    webbrowser.open(url=('https://www.google.com/' + google_sites), new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 2:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('2. Random website selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    random_sites = ('https://alwaysjudgeabookbyitscover.com/')
                elif select == 2:
                    random_sites = ('http://eelslap.com/')
                elif select == 3:
                    random_sites = ('https://smashthewalls.com/')
                elif select == 4:
                    random_sites = ('https://weirdorconfusing.com/')
                elif select == 5:
                    random_sites = ('https://trypap.com/')
                elif select == 6:
                    random_sites = ('http://www.republiquedesmangues.fr/')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)
                for _ in range(pages):
                    webbrowser.open(url=random_sites, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 3:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('3. Selected website!')
                pages = int(input('How Many Tabs: '))
                website = input('Website, You dont need http/s: ')
                for _ in range(pages):
                    webbrowser.open(url='http://' + website, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 4:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('Exitting!!!')
                time.sleep(1)
            else:
                print('Wrong, That option does not exist!')
                time.sleep(1)
                print('Returning to menu!')
                time.sleep(1)

        elif a == 3:
            print('3. Computer Destoryer Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
            zx = input('Are you sure Y/N: ')
            if (zx.capitalize()) == 'Y':
                time.sleep(1)
                print('Destroyer Starting in 3 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 2 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 1 seconds!')
                time.sleep(1)
                for _ in range(1000):
                    webbrowser.open(url='https://www.youtube.com/watch?v=i_2yNbIzwOI', new=2)
            else:
                print('')
                print('Returning to main menu!')
                time.sleep(1)

        elif a == 4:
            print('4. Discord Tools selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
                time.sleep(.1)
                print(
                    "              dddddddd                                                                                              dddddddd         ")
                print(
                    "              d::::::d  iiii                                                                                        d::::::d              tttt                                            lllllll  ")
                print(
                    "              d::::::d i::::i                                                                                       d::::::d           ttt:::t                                            l:::::l    ")
                print(
                    "              d::::::d  iiii                                                                                        d::::::d           t:::::t                                            l:::::l      ")
                print(
                    "              d:::::d                                                                                               d:::::d            t:::::t                                            l:::::l    ")
                print(
                    "      ddddddddd:::::d iiiiiii     ssssssssss       cccccccccccccccc   ooooooooooo   rrrrr   rrrrrrrrr       ddddddddd:::::d      ttttttt:::::ttttttt       ooooooooooo      ooooooooooo    l::::l     ssssssssss  ")
                print(
                    "     dd::::::::::::::d i:::::i   ss::::::::::s    cc:::::::::::::::c oo:::::::::::oo r::::rrr:::::::::r    dd::::::::::::::d      t:::::::::::::::::t     oo:::::::::::oo  oo:::::::::::oo  l::::l   ss::::::::::s  ")
                print(
                    "    d::::::::::::::::d  i::::i ss:::::::::::::s  c:::::::::::::::::co:::::::::::::::or:::::::::::::::::r  d::::::::::::::::d      t:::::::::::::::::t    o:::::::::::::::oo:::::::::::::::o l::::l ss:::::::::::::s ")
                print(
                    "   d:::::::ddddd:::::d  i::::i s::::::ssss:::::sc:::::::cccccc:::::co:::::ooooo:::::orr::::::rrrrr::::::rd:::::::ddddd:::::d      tttttt:::::::tttttt    o:::::ooooo:::::oo:::::ooooo:::::o l::::l s::::::ssss:::::s ")
                print(
                    "   d::::::d    d:::::d  i::::i  s:::::s  ssssss c::::::c     ccccccco::::o     o::::o r:::::r     r:::::rd::::::d    d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l  s:::::s  ssssss ")
                print(
                    "   d:::::d     d:::::d  i::::i    s::::::s      c:::::c             o::::o     o::::o r:::::r     rrrrrrrd:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l    s::::::s  ")
                print(
                    "   d:::::d     d:::::d  i::::i       s::::::s   c:::::c             o::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l       s::::::s  ")
                print(
                    "   d:::::d     d:::::d  i::::i ssssss   s:::::s c::::::c     ccccccco::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t    tttttto::::o     o::::oo::::o     o::::o l::::l ssssss   s:::::s ")
                print(
                    "   d::::::ddddd::::::ddi::::::is:::::ssss::::::sc:::::::cccccc:::::co:::::ooooo:::::o r:::::r            d::::::ddddd::::::dd           t::::::tttt:::::to:::::ooooo:::::oo:::::ooooo:::::ol::::::ls:::::ssss::::::s")
                print(
                    "    d:::::::::::::::::di::::::is::::::::::::::s  c:::::::::::::::::co:::::::::::::::o r:::::r             d:::::::::::::::::d           tt::::::::::::::to:::::::::::::::oo:::::::::::::::ol::::::ls::::::::::::::s ")
                print(
                    "     d:::::::::ddd::::di::::::i s:::::::::::ss    cc:::::::::::::::c oo:::::::::::oo  r:::::r              d:::::::::ddd::::d             tt:::::::::::tt oo:::::::::::oo  oo:::::::::::oo l::::::l s:::::::::::ss  ")
                print(
                    "     ddddddddd   dddddiiiiiiii  sssssssssss        cccccccccccccccc   ooooooooooo    rrrrrrr               ddddddddd   ddddd               ttttttttttt     ooooooooooo      ooooooooooo   llllllll  sssssssssss     ")
                for _ in range(2):
                    print(' ')
                print('If You get banned on discord it is not my fault!')
                print('3 & 4  can result if caught in a ban!')
                for _ in range(2):
                    print(' ')
                print('1. Custom discord status')
                print('2. Text spammer')
                print('3. Multi message delete')
                print('4. Token login')
                ex = int(input('Select A Tool:'))
                if ex == 1:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 2:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 3:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 4:
                    print('3. Multi message delete selected!')
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')


                else:
                    time.sleep(1)
                    print(
                        "....................................................................................................")
                    time.sleep(1)
                    print('Invalid command!')
                    time.sleep(1)
                    print('Returning home!')
                    time.sleep(1)

        elif a == 5:
            print('1. Pinging tools selected!')  # gotto work on this
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
        elif a == 6:
            print('6. Other Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
        elif a == 7:
            print('7. Exit Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
            time.sleep(3)
            b = input('You sure? Y/N: ')
            if (b.capitalize()) == 'Y':
                print('Terminating in 10 seconds')
                time.sleep(5)
                print('Terminating in 5 seconds!')
                time.sleep(1)
                print('Terminating in 4 seconds!')
                time.sleep(1)
                print('Terminating in 3 seconds!')
                time.sleep(1)
                print('Terminating in 2 seconds!')
                time.sleep(1)
                print('Terminating in 1 seconds!')
                time.sleep(1)
                print('TERMINATED')
                exit()
elif language == '中文':#chinese(simplified)
    print('Tools pack')
    time.sleep(1)
    print('Detecting ip...')
    x = randint(1, 4)
    time.sleep(x)
    print('---.---.---.-' + ' Has been detected')  # still working on it
    time.sleep(1)
    x = randint(1, 4)
    print('Checking OS...')
    time.sleep(x)
    zxc = platform.system()
    if zxc == 'Darwin':
        abcdef = 'Macosx'
        print(abcdef + ',' + (platform.release()) + ' ' + 'Detected')
    else:
        print(platform.system() + ',' + (platform.release()) + ' ' + 'Detected')

    time.sleep(1)
    for _ in range(3):
        print('')
        time.sleep(.1)
    if platform.system() == 'Linux':
        print('Linux OS is not a valid os for the tool pack and is getting worked on!')
        time.sleep(1)
        a = int(input('Type any number for a surprise! '))
        if a >= 1:
            for _ in range(a):
                webbrowser.open(url='https://www.youtube.com/watch?v=oHg5SJYRHA0', new=1)
            time.sleep(3)
            print("TERMINATING NOW!")
            time.sleep(5)
            exit()
    inad = input('Have your paid/boost for the Program. Y:paid/Y:boosted/N: ')
    pop = 10
    while pop < 20:
        if inad == 'Y:paid':
            print('')
            print('Paid user login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/scPbt4D4')
            username = input('Username: ')
            time.sleep(1)
            print('')
            password = input('Password: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Correct password and username!')
                    time.sleep(1)
                    print('')
                    print('Sharing passwords are a bannable offence and will be removed from the list without refund!')
                    print('')
                    break
                else:
                    print('Invalid password or username!')
                    exita = input('Would like to re-try? Y/N: ')
                    if (exita.capitalize()) == 'Y':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Invalid Response!')
        elif inad == 'Y:boosted':
            print('')
            print('Booster user login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/c254wxqt')
            username = input('Username: ')
            time.sleep(1)
            print('')
            password = input('Password: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Correct password and username!')
                    time.sleep(1)
                    print('')
                    print('Sharing passwords are a bannable offence and will be removed from the list!')
                    print('')
                    break
                else:
                    print('Invalid password or username!')
                    exita = input('Would like to re-try? Y/N: ')
                    if (exita.capitalize()) == 'Y':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Invalid Response!')
        elif (inad.capitalize()) == 'N':
            time.sleep(1)
            i = input('Would you like a uuid? this is required to purchase the full version. Y/N: ')
            if (i.capitalize()) == 'Y':
                time.sleep(1)
                print(uuid.uuid1())
                time.sleep(1)
                print('')
                print('Keep this stored as it will be your password until you request it to get changed!')
                print('')
                time.sleep(5)
            print(
                'Would you like to join the discord server? You can buy the full version there and also boosters will get more tools!')
            discord = input('Y/N? ')
            if (discord.capitalize()) == 'Y':
                webbrowser.open(url='https://discord.gg/WWWhj9z')
            break
        else:
            time.sleep(1)
            print('Invalid response!')
            time.sleep(1)
            break

    print('N Selected!')
    time.sleep(1)
    print('Free version, No booster or paid tools')
    time.sleep(1)
    print('')
    pastebin12 = ('https://pastebin.com/9qNWLYbb')
    kid = 1
    webbrowser.open_new(url='https://bit.ly/3lahict')
    print('Key Stop 1 & 2!')
    key1 = input('Key 1: ')
    key2 = input('Key 2: ')
    key12 = requests.get(pastebin12).text
    for line in key12.split('\n'):
        if key12 and key2 in line:
            print('Keys Are valid')
            time.sleep(1)
            print('')
            print('Thank you for helping support me!')
            print('')
        else:
            print('invalid')

    print('Loading')
    x = randint(3, 10)
    time.sleep(x)
    print('(##########)100% COMPLETE')
    time.sleep(0.5)
    print('Complete!')

    while True:
        time.sleep(2)
        for _ in range(40):
            print(' ')
            time.sleep(.01)

        print('  88888             8    888b.           8 ')
        print("    8   .d8b. .d8b. 8    8  .8 .d88 .d8b 8.dP ")
        print("    8   8' .8 8' .8 8    8wwP' 8  8 8    88b  ")
        print("    8   `Y8P' `Y8P' 8    8     `Y88 `Y8P 8 Yb ")
        time.sleep(2)
        print('By sɹǝƃƃod#5183')
        print('Credit to: zoony#1337 & Dropout#1337')
        print('')
        print("I am legaly not responsibile for anything that happens to you or your device! ")
        print('')
        time.sleep(1)
        print('1. Pinging tools: ')
        time.sleep(1)
        print('2. Browser history spammer: ')
        time.sleep(1)
        print('3. Computer destroyer: ')
        time.sleep(1)
        print('4. Discord spammer: ')
        time.sleep(1)
        print('5. Something idk')
        time.sleep(1)
        print('6. Other: ')
        time.sleep(1)
        print('7. Exit: ')
        time.sleep(2)
        a = int(input('Choose a Tool: '))
        if a == 1:
            print('1. Pinging tools selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
                print(
                    "██▓███   ██▓ ███▄    █   ▄████  ██▓ ███▄    █   ▄████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████")
                print(
                    "▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▓██▒ ██ ▀█   █  ██▒ ▀█▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒")
                print(
                    "▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄")
                print(
                    "▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓░██░▓██▒  ▐▌██▒░▓█  ██▓   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒")
                print(
                    "▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒░██░▒██░   ▓██░░▒▓███▀▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒")
                print(
                    "▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░")
                print(
                    "░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░  ▒ ░░ ░░   ░ ▒░  ░   ░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░")
                print(
                    "░░        ▒ ░   ░   ░ ░ ░ ░   ░  ▒ ░   ░   ░ ░ ░ ░   ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░")
                print("░           ░       ░  ░           ░       ░                 ░ ░      ░ ░      ░  ░      ░")
                print('')
                print('')
                print('')
                time.sleep(1)
                print('1. Ip/Sever tester')
                print('2. Ip Stresser')

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
                server_ip = int(input('Enter server IP : '))
                rep = os.system('ping ' + server_ip)
                if rep == 0:
                    print
                    'n n server is up n n'
                else:
                    print
                'server is down'

        elif a == 2:
            print('2. Browser history spammer selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(1)
            for _ in range(15):
                print(' ')
            time.sleep(3)
            print(
                '▄▄▄▄    ██▀███   ▒█████   █     █░  ██████ ▓█████  ██▀███      ██░ ██  ██▓  ██████ ▄▄▄█████▓ ▒█████   ██▀███ ▓██   ██▓     ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███ ')
            print(
                '▓█████▄ ▓██ ▒ ██▒▒██▒  ██▒▓█░ █ ░█░▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒   ▓██░ ██▒▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒   ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒')
            print(
                '▒██▒ ▄██▓██ ░▄█ ▒▒██░  ██▒▒█░ █ ░█ ░ ▓██▄   ▒███   ▓██ ░▄█ ▒   ▒██▀▀██░▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒')
            print(
                '▒██░█▀  ▒██▀▀█▄  ▒██   ██░░█░ █ ░█   ▒   ██▒▒▓█  ▄ ▒██▀▀█▄     ░▓█ ░██ ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░     ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  ')
            print(
                '░▓█  ▀█▓░██▓ ▒██▒░ ████▓▒░░░██▒██▓ ▒██████▒▒░▒████▒░██▓ ▒██▒   ░▓█▒░██▓░██░▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒')
            print(
                '░▒▓███▀▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▓░▒ ▒  ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░    ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░')
            print(
                '▒░▒   ░   ░▒ ░ ▒░  ░ ▒ ▒░   ▒ ░ ░  ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░    ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░')
            print(
                '░ ░ ░ ░ ▒    ░   ░  ░  ░  ░     ░     ░░   ░     ░  ░░ ░ ▒ ░░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░     ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ ')
            print(
                '  ░ ░      ░          ░     ░  ░   ░         ░  ░  ░ ░        ░               ░ ░     ░     ░ ░              ░                 ░  ░       ░          ░      ░  ░   ░     ')
            print(
                '     ░                                                                                                        ░ ░          ')
            for _ in range(3):
                time.sleep(0.2)
                print(' ')
            print(
                '.............................................................................................................................................................................................')
            print(' ')
            time.sleep(1)
            print('1. Random Google Page')
            time.sleep(1)
            print('2. Random Website')
            time.sleep(1)
            print('3. Selected Website')
            time.sleep(1)
            print('4. Exit Tool')
            time.sleep(1)
            c = int(input('Choose Tool: '))
            if c == 1:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('1. Random google page selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    google_sites = ('search?q=nut&oq=nut&aqs=chrome.0.69i59.1970j0j7&sourceid=chrome&ie=UTF-8')
                elif select == 2:
                    google_sites = (
                        'search?q=history&oq=his&aqs=chrome.1.69i57j69i59l2j69i61j69i60.2720j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 3:
                    google_sites = (
                        'search?q=Yeet&oq=Yeet&aqs=chrome..69i57j69i60j69i65.1465j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 4:
                    google_sites = ('search?q=egg&oq=egg&aqs=chrome..69i57.686j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 5:
                    google_sites = (
                        'search?q=north+korea&oq=north+korea&aqs=chrome..69i57.2612j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 6:
                    google_sites = (
                        'search?q=computer&oq=computer&aqs=chrome..69i57j69i61l2j69i65l2j69i61.1695j0j9&sourceid=chrome&ie=UTF-8')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)

                for _ in range(pages):
                    webbrowser.open(url=('https://www.google.com/' + google_sites), new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 2:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('2. Random website selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    random_sites = ('https://alwaysjudgeabookbyitscover.com/')
                elif select == 2:
                    random_sites = ('http://eelslap.com/')
                elif select == 3:
                    random_sites = ('https://smashthewalls.com/')
                elif select == 4:
                    random_sites = ('https://weirdorconfusing.com/')
                elif select == 5:
                    random_sites = ('https://trypap.com/')
                elif select == 6:
                    random_sites = ('http://www.republiquedesmangues.fr/')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)
                for _ in range(pages):
                    webbrowser.open(url=random_sites, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 3:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('3. Selected website!')
                pages = int(input('How Many Tabs: '))
                website = input('Website, You dont need http/s: ')
                for _ in range(pages):
                    webbrowser.open(url='http://' + website, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 4:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('Exitting!!!')
                time.sleep(1)
            else:
                print('Wrong, That option does not exist!')
                time.sleep(1)
                print('Returning to menu!')
                time.sleep(1)

        elif a == 3:
            print('3. Computer Destoryer Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
            zx = input('Are you sure Y/N: ')
            if (zx.capitalize()) == 'Y':
                time.sleep(1)
                print('Destroyer Starting in 3 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 2 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 1 seconds!')
                time.sleep(1)
                for _ in range(1000):
                    webbrowser.open(url='https://www.youtube.com/watch?v=i_2yNbIzwOI', new=2)
            else:
                print('')
                print('Returning to main menu!')
                time.sleep(1)

        elif a == 4:
            print('4. Discord Tools selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
                time.sleep(.1)
                print(
                    "              dddddddd                                                                                              dddddddd         ")
                print(
                    "              d::::::d  iiii                                                                                        d::::::d              tttt                                            lllllll  ")
                print(
                    "              d::::::d i::::i                                                                                       d::::::d           ttt:::t                                            l:::::l    ")
                print(
                    "              d::::::d  iiii                                                                                        d::::::d           t:::::t                                            l:::::l      ")
                print(
                    "              d:::::d                                                                                               d:::::d            t:::::t                                            l:::::l    ")
                print(
                    "      ddddddddd:::::d iiiiiii     ssssssssss       cccccccccccccccc   ooooooooooo   rrrrr   rrrrrrrrr       ddddddddd:::::d      ttttttt:::::ttttttt       ooooooooooo      ooooooooooo    l::::l     ssssssssss  ")
                print(
                    "     dd::::::::::::::d i:::::i   ss::::::::::s    cc:::::::::::::::c oo:::::::::::oo r::::rrr:::::::::r    dd::::::::::::::d      t:::::::::::::::::t     oo:::::::::::oo  oo:::::::::::oo  l::::l   ss::::::::::s  ")
                print(
                    "    d::::::::::::::::d  i::::i ss:::::::::::::s  c:::::::::::::::::co:::::::::::::::or:::::::::::::::::r  d::::::::::::::::d      t:::::::::::::::::t    o:::::::::::::::oo:::::::::::::::o l::::l ss:::::::::::::s ")
                print(
                    "   d:::::::ddddd:::::d  i::::i s::::::ssss:::::sc:::::::cccccc:::::co:::::ooooo:::::orr::::::rrrrr::::::rd:::::::ddddd:::::d      tttttt:::::::tttttt    o:::::ooooo:::::oo:::::ooooo:::::o l::::l s::::::ssss:::::s ")
                print(
                    "   d::::::d    d:::::d  i::::i  s:::::s  ssssss c::::::c     ccccccco::::o     o::::o r:::::r     r:::::rd::::::d    d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l  s:::::s  ssssss ")
                print(
                    "   d:::::d     d:::::d  i::::i    s::::::s      c:::::c             o::::o     o::::o r:::::r     rrrrrrrd:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l    s::::::s  ")
                print(
                    "   d:::::d     d:::::d  i::::i       s::::::s   c:::::c             o::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l       s::::::s  ")
                print(
                    "   d:::::d     d:::::d  i::::i ssssss   s:::::s c::::::c     ccccccco::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t    tttttto::::o     o::::oo::::o     o::::o l::::l ssssss   s:::::s ")
                print(
                    "   d::::::ddddd::::::ddi::::::is:::::ssss::::::sc:::::::cccccc:::::co:::::ooooo:::::o r:::::r            d::::::ddddd::::::dd           t::::::tttt:::::to:::::ooooo:::::oo:::::ooooo:::::ol::::::ls:::::ssss::::::s")
                print(
                    "    d:::::::::::::::::di::::::is::::::::::::::s  c:::::::::::::::::co:::::::::::::::o r:::::r             d:::::::::::::::::d           tt::::::::::::::to:::::::::::::::oo:::::::::::::::ol::::::ls::::::::::::::s ")
                print(
                    "     d:::::::::ddd::::di::::::i s:::::::::::ss    cc:::::::::::::::c oo:::::::::::oo  r:::::r              d:::::::::ddd::::d             tt:::::::::::tt oo:::::::::::oo  oo:::::::::::oo l::::::l s:::::::::::ss  ")
                print(
                    "     ddddddddd   dddddiiiiiiii  sssssssssss        cccccccccccccccc   ooooooooooo    rrrrrrr               ddddddddd   ddddd               ttttttttttt     ooooooooooo      ooooooooooo   llllllll  sssssssssss     ")
                for _ in range(2):
                    print(' ')
                print('If You get banned on discord it is not my fault!')
                print('3 & 4  can result if caught in a ban!')
                for _ in range(2):
                    print(' ')
                print('1. Custom discord status')
                print('2. Text spammer')
                print('3. Multi message delete')
                print('4. Token login')
                ex = int(input('Select A Tool:'))
                if ex == 1:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 2:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 3:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 4:
                    print('3. Multi message delete selected!')
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')


                else:
                    time.sleep(1)
                    print(
                        "....................................................................................................")
                    time.sleep(1)
                    print('Invalid command!')
                    time.sleep(1)
                    print('Returning home!')
                    time.sleep(1)

        elif a == 5:
            print('1. Pinging tools selected!')  # gotto work on this
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
        elif a == 6:
            print('6. Other Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
        elif a == 7:
            print('7. Exit Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
            time.sleep(3)
            b = input('You sure? Y/N: ')
            if (b.capitalize()) == 'Y':
                print('Terminating in 10 seconds')
                time.sleep(5)
                print('Terminating in 5 seconds!')
                time.sleep(1)
                print('Terminating in 4 seconds!')
                time.sleep(1)
                print('Terminating in 3 seconds!')
                time.sleep(1)
                print('Terminating in 2 seconds!')
                time.sleep(1)
                print('Terminating in 1 seconds!')
                time.sleep(1)
                print('TERMINATED')
                exit()
elif language == 'русский':#Russian
    print('Tools pack')
    time.sleep(1)
    print('Detecting ip...')
    x = randint(1, 4)
    time.sleep(x)
    print('---.---.---.-' + ' Has been detected')  # still working on it
    time.sleep(1)
    x = randint(1, 4)
    print('Checking OS...')
    time.sleep(x)
    zxc = platform.system()
    if zxc == 'Darwin':
        abcdef = 'Macosx'
        print(abcdef + ',' + (platform.release()) + ' ' + 'Detected')
    else:
        print(platform.system() + ',' + (platform.release()) + ' ' + 'Detected')

    time.sleep(1)
    for _ in range(3):
        print('')
        time.sleep(.1)
    if platform.system() == 'Linux':
        print('Linux OS is not a valid os for the tool pack and is getting worked on!')
        time.sleep(1)
        a = int(input('Type any number for a surprise! '))
        if a >= 1:
            for _ in range(a):
                webbrowser.open(url='https://www.youtube.com/watch?v=oHg5SJYRHA0', new=1)
            time.sleep(3)
            print("TERMINATING NOW!")
            time.sleep(5)
            exit()
    inad = input('Have your paid/boost for the Program. Y:paid/Y:boosted/N: ')
    pop = 10
    while pop < 20:
        if inad == 'Y:paid':
            print('')
            print('Paid user login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/scPbt4D4')
            username = input('Username: ')
            time.sleep(1)
            print('')
            password = input('Password: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Correct password and username!')
                    time.sleep(1)
                    print('')
                    print('Sharing passwords are a bannable offence and will be removed from the list without refund!')
                    print('')
                    break
                else:
                    print('Invalid password or username!')
                    exita = input('Would like to re-try? Y/N: ')
                    if (exita.capitalize()) == 'Y':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Invalid Response!')
        elif inad == 'Y:boosted':
            print('')
            print('Booster user login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/c254wxqt')
            username = input('Username: ')
            time.sleep(1)
            print('')
            password = input('Password: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Correct password and username!')
                    time.sleep(1)
                    print('')
                    print('Sharing passwords are a bannable offence and will be removed from the list!')
                    print('')
                    break
                else:
                    print('Invalid password or username!')
                    exita = input('Would like to re-try? Y/N: ')
                    if (exita.capitalize()) == 'Y':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Invalid Response!')
        elif (inad.capitalize()) == 'N':
            time.sleep(1)
            i = input('Would you like a uuid? this is required to purchase the full version. Y/N: ')
            if (i.capitalize()) == 'Y':
                time.sleep(1)
                print(uuid.uuid1())
                time.sleep(1)
                print('')
                print('Keep this stored as it will be your password until you request it to get changed!')
                print('')
                time.sleep(5)
            print(
                'Would you like to join the discord server? You can buy the full version there and also boosters will get more tools!')
            discord = input('Y/N? ')
            if (discord.capitalize()) == 'Y':
                webbrowser.open(url='https://discord.gg/WWWhj9z')
            break
        else:
            time.sleep(1)
            print('Invalid response!')
            time.sleep(1)
            break

    print('N Selected!')
    time.sleep(1)
    print('Free version, No booster or paid tools')
    time.sleep(1)
    print('')
    pastebin12 = ('https://pastebin.com/9qNWLYbb')
    kid = 1
    webbrowser.open_new(url='https://bit.ly/3lahict')
    print('Key Stop 1 & 2!')
    key1 = input('Key 1: ')
    key2 = input('Key 2: ')
    key12 = requests.get(pastebin12).text
    for line in key12.split('\n'):
        if key12 and key2 in line:
            print('Keys Are valid')
            time.sleep(1)
            print('')
            print('Thank you for helping support me!')
            print('')
        else:
            print('invalid')

    print('Loading')
    x = randint(3, 10)
    time.sleep(x)
    print('(##########)100% COMPLETE')
    time.sleep(0.5)
    print('Complete!')

    while True:
        time.sleep(2)
        for _ in range(40):
            print(' ')
            time.sleep(.01)

        print('  88888             8    888b.           8 ')
        print("    8   .d8b. .d8b. 8    8  .8 .d88 .d8b 8.dP ")
        print("    8   8' .8 8' .8 8    8wwP' 8  8 8    88b  ")
        print("    8   `Y8P' `Y8P' 8    8     `Y88 `Y8P 8 Yb ")
        time.sleep(2)
        print('By sɹǝƃƃod#5183')
        print('Credit to: zoony#1337 & Dropout#1337')
        print('')
        print("I am legaly not responsibile for anything that happens to you or your device! ")
        print('')
        time.sleep(1)
        print('1. Pinging tools: ')
        time.sleep(1)
        print('2. Browser history spammer: ')
        time.sleep(1)
        print('3. Computer destroyer: ')
        time.sleep(1)
        print('4. Discord spammer: ')
        time.sleep(1)
        print('5. Something idk')
        time.sleep(1)
        print('6. Other: ')
        time.sleep(1)
        print('7. Exit: ')
        time.sleep(2)
        a = int(input('Choose a Tool: '))
        if a == 1:
            print('1. Pinging tools selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
                print(
                    "██▓███   ██▓ ███▄    █   ▄████  ██▓ ███▄    █   ▄████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████")
                print(
                    "▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▓██▒ ██ ▀█   █  ██▒ ▀█▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒")
                print(
                    "▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄")
                print(
                    "▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓░██░▓██▒  ▐▌██▒░▓█  ██▓   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒")
                print(
                    "▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒░██░▒██░   ▓██░░▒▓███▀▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒")
                print(
                    "▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░")
                print(
                    "░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░  ▒ ░░ ░░   ░ ▒░  ░   ░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░")
                print(
                    "░░        ▒ ░   ░   ░ ░ ░ ░   ░  ▒ ░   ░   ░ ░ ░ ░   ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░")
                print("░           ░       ░  ░           ░       ░                 ░ ░      ░ ░      ░  ░      ░")
                print('')
                print('')
                print('')
                time.sleep(1)
                print('1. Ip/Sever tester')
                print('2. Ip Stresser')

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
                server_ip = int(input('Enter server IP : '))
                rep = os.system('ping ' + server_ip)
                if rep == 0:
                    print
                    'n n server is up n n'
                else:
                    print
                'server is down'

        elif a == 2:
            print('2. Browser history spammer selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(1)
            for _ in range(15):
                print(' ')
            time.sleep(3)
            print(
                '▄▄▄▄    ██▀███   ▒█████   █     █░  ██████ ▓█████  ██▀███      ██░ ██  ██▓  ██████ ▄▄▄█████▓ ▒█████   ██▀███ ▓██   ██▓     ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███ ')
            print(
                '▓█████▄ ▓██ ▒ ██▒▒██▒  ██▒▓█░ █ ░█░▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒   ▓██░ ██▒▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒   ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒')
            print(
                '▒██▒ ▄██▓██ ░▄█ ▒▒██░  ██▒▒█░ █ ░█ ░ ▓██▄   ▒███   ▓██ ░▄█ ▒   ▒██▀▀██░▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒')
            print(
                '▒██░█▀  ▒██▀▀█▄  ▒██   ██░░█░ █ ░█   ▒   ██▒▒▓█  ▄ ▒██▀▀█▄     ░▓█ ░██ ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░     ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  ')
            print(
                '░▓█  ▀█▓░██▓ ▒██▒░ ████▓▒░░░██▒██▓ ▒██████▒▒░▒████▒░██▓ ▒██▒   ░▓█▒░██▓░██░▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒')
            print(
                '░▒▓███▀▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▓░▒ ▒  ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░    ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░')
            print(
                '▒░▒   ░   ░▒ ░ ▒░  ░ ▒ ▒░   ▒ ░ ░  ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░    ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░')
            print(
                '░ ░ ░ ░ ▒    ░   ░  ░  ░  ░     ░     ░░   ░     ░  ░░ ░ ▒ ░░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░     ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ ')
            print(
                '  ░ ░      ░          ░     ░  ░   ░         ░  ░  ░ ░        ░               ░ ░     ░     ░ ░              ░                 ░  ░       ░          ░      ░  ░   ░     ')
            print(
                '     ░                                                                                                        ░ ░          ')
            for _ in range(3):
                time.sleep(0.2)
                print(' ')
            print(
                '.............................................................................................................................................................................................')
            print(' ')
            time.sleep(1)
            print('1. Random Google Page')
            time.sleep(1)
            print('2. Random Website')
            time.sleep(1)
            print('3. Selected Website')
            time.sleep(1)
            print('4. Exit Tool')
            time.sleep(1)
            c = int(input('Choose Tool: '))
            if c == 1:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('1. Random google page selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    google_sites = ('search?q=nut&oq=nut&aqs=chrome.0.69i59.1970j0j7&sourceid=chrome&ie=UTF-8')
                elif select == 2:
                    google_sites = (
                        'search?q=history&oq=his&aqs=chrome.1.69i57j69i59l2j69i61j69i60.2720j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 3:
                    google_sites = (
                        'search?q=Yeet&oq=Yeet&aqs=chrome..69i57j69i60j69i65.1465j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 4:
                    google_sites = ('search?q=egg&oq=egg&aqs=chrome..69i57.686j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 5:
                    google_sites = (
                        'search?q=north+korea&oq=north+korea&aqs=chrome..69i57.2612j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 6:
                    google_sites = (
                        'search?q=computer&oq=computer&aqs=chrome..69i57j69i61l2j69i65l2j69i61.1695j0j9&sourceid=chrome&ie=UTF-8')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)

                for _ in range(pages):
                    webbrowser.open(url=('https://www.google.com/' + google_sites), new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 2:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('2. Random website selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    random_sites = ('https://alwaysjudgeabookbyitscover.com/')
                elif select == 2:
                    random_sites = ('http://eelslap.com/')
                elif select == 3:
                    random_sites = ('https://smashthewalls.com/')
                elif select == 4:
                    random_sites = ('https://weirdorconfusing.com/')
                elif select == 5:
                    random_sites = ('https://trypap.com/')
                elif select == 6:
                    random_sites = ('http://www.republiquedesmangues.fr/')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)
                for _ in range(pages):
                    webbrowser.open(url=random_sites, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 3:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('3. Selected website!')
                pages = int(input('How Many Tabs: '))
                website = input('Website, You dont need http/s: ')
                for _ in range(pages):
                    webbrowser.open(url='http://' + website, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 4:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('Exitting!!!')
                time.sleep(1)
            else:
                print('Wrong, That option does not exist!')
                time.sleep(1)
                print('Returning to menu!')
                time.sleep(1)

        elif a == 3:
            print('3. Computer Destoryer Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
            zx = input('Are you sure Y/N: ')
            if (zx.capitalize()) == 'Y':
                time.sleep(1)
                print('Destroyer Starting in 3 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 2 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 1 seconds!')
                time.sleep(1)
                for _ in range(1000):
                    webbrowser.open(url='https://www.youtube.com/watch?v=i_2yNbIzwOI', new=2)
            else:
                print('')
                print('Returning to main menu!')
                time.sleep(1)

        elif a == 4:
            print('4. Discord Tools selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
                time.sleep(.1)
                print(
                    "              dddddddd                                                                                              dddddddd         ")
                print(
                    "              d::::::d  iiii                                                                                        d::::::d              tttt                                            lllllll  ")
                print(
                    "              d::::::d i::::i                                                                                       d::::::d           ttt:::t                                            l:::::l    ")
                print(
                    "              d::::::d  iiii                                                                                        d::::::d           t:::::t                                            l:::::l      ")
                print(
                    "              d:::::d                                                                                               d:::::d            t:::::t                                            l:::::l    ")
                print(
                    "      ddddddddd:::::d iiiiiii     ssssssssss       cccccccccccccccc   ooooooooooo   rrrrr   rrrrrrrrr       ddddddddd:::::d      ttttttt:::::ttttttt       ooooooooooo      ooooooooooo    l::::l     ssssssssss  ")
                print(
                    "     dd::::::::::::::d i:::::i   ss::::::::::s    cc:::::::::::::::c oo:::::::::::oo r::::rrr:::::::::r    dd::::::::::::::d      t:::::::::::::::::t     oo:::::::::::oo  oo:::::::::::oo  l::::l   ss::::::::::s  ")
                print(
                    "    d::::::::::::::::d  i::::i ss:::::::::::::s  c:::::::::::::::::co:::::::::::::::or:::::::::::::::::r  d::::::::::::::::d      t:::::::::::::::::t    o:::::::::::::::oo:::::::::::::::o l::::l ss:::::::::::::s ")
                print(
                    "   d:::::::ddddd:::::d  i::::i s::::::ssss:::::sc:::::::cccccc:::::co:::::ooooo:::::orr::::::rrrrr::::::rd:::::::ddddd:::::d      tttttt:::::::tttttt    o:::::ooooo:::::oo:::::ooooo:::::o l::::l s::::::ssss:::::s ")
                print(
                    "   d::::::d    d:::::d  i::::i  s:::::s  ssssss c::::::c     ccccccco::::o     o::::o r:::::r     r:::::rd::::::d    d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l  s:::::s  ssssss ")
                print(
                    "   d:::::d     d:::::d  i::::i    s::::::s      c:::::c             o::::o     o::::o r:::::r     rrrrrrrd:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l    s::::::s  ")
                print(
                    "   d:::::d     d:::::d  i::::i       s::::::s   c:::::c             o::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l       s::::::s  ")
                print(
                    "   d:::::d     d:::::d  i::::i ssssss   s:::::s c::::::c     ccccccco::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t    tttttto::::o     o::::oo::::o     o::::o l::::l ssssss   s:::::s ")
                print(
                    "   d::::::ddddd::::::ddi::::::is:::::ssss::::::sc:::::::cccccc:::::co:::::ooooo:::::o r:::::r            d::::::ddddd::::::dd           t::::::tttt:::::to:::::ooooo:::::oo:::::ooooo:::::ol::::::ls:::::ssss::::::s")
                print(
                    "    d:::::::::::::::::di::::::is::::::::::::::s  c:::::::::::::::::co:::::::::::::::o r:::::r             d:::::::::::::::::d           tt::::::::::::::to:::::::::::::::oo:::::::::::::::ol::::::ls::::::::::::::s ")
                print(
                    "     d:::::::::ddd::::di::::::i s:::::::::::ss    cc:::::::::::::::c oo:::::::::::oo  r:::::r              d:::::::::ddd::::d             tt:::::::::::tt oo:::::::::::oo  oo:::::::::::oo l::::::l s:::::::::::ss  ")
                print(
                    "     ddddddddd   dddddiiiiiiii  sssssssssss        cccccccccccccccc   ooooooooooo    rrrrrrr               ddddddddd   ddddd               ttttttttttt     ooooooooooo      ooooooooooo   llllllll  sssssssssss     ")
                for _ in range(2):
                    print(' ')
                print('If You get banned on discord it is not my fault!')
                print('3 & 4  can result if caught in a ban!')
                for _ in range(2):
                    print(' ')
                print('1. Custom discord status')
                print('2. Text spammer')
                print('3. Multi message delete')
                print('4. Token login')
                ex = int(input('Select A Tool:'))
                if ex == 1:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 2:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 3:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 4:
                    print('3. Multi message delete selected!')
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')


                else:
                    time.sleep(1)
                    print(
                        "....................................................................................................")
                    time.sleep(1)
                    print('Invalid command!')
                    time.sleep(1)
                    print('Returning home!')
                    time.sleep(1)

        elif a == 5:
            print('1. Pinging tools selected!')  # gotto work on this
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
        elif a == 6:
            print('6. Other Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
        elif a == 7:
            print('7. Exit Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
            time.sleep(3)
            b = input('You sure? Y/N: ')
            if (b.capitalize()) == 'Y':
                print('Terminating in 10 seconds')
                time.sleep(5)
                print('Terminating in 5 seconds!')
                time.sleep(1)
                print('Terminating in 4 seconds!')
                time.sleep(1)
                print('Terminating in 3 seconds!')
                time.sleep(1)
                print('Terminating in 2 seconds!')
                time.sleep(1)
                print('Terminating in 1 seconds!')
                time.sleep(1)
                print('TERMINATED')
                exit()
elif language == 'svenska':#sweedish

    print('Tools pack')
    time.sleep(1)
    print('Detecting ip...')
    x = randint(1, 4)
    time.sleep(x)
    print('---.---.---.-' + ' Has been detected')  # still working on it
    time.sleep(1)
    x = randint(1, 4)
    print('Checking OS...')
    time.sleep(x)
    zxc = platform.system()
    if zxc == 'Darwin':
        abcdef = 'Macosx'
        print(abcdef + ',' + (platform.release()) + ' ' + 'Detected')
    else:
        print(platform.system() + ',' + (platform.release()) + ' ' + 'Detected')

    time.sleep(1)
    for _ in range(3):
        print('')
        time.sleep(.1)
    if platform.system() == 'Linux':
        print('Linux OS is not a valid os for the tool pack and is getting worked on!')
        time.sleep(1)
        a = int(input('Type any number for a surprise! '))
        if a >= 1:
            for _ in range(a):
                webbrowser.open(url='https://www.youtube.com/watch?v=oHg5SJYRHA0', new=1)
            time.sleep(3)
            print("TERMINATING NOW!")
            time.sleep(5)
            exit()
    inad = input('Have your paid/boost for the Program. Y:paid/Y:boosted/N: ')
    pop = 10
    while pop < 20:
        if inad == 'Y:paid':
            print('')
            print('Paid user login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/scPbt4D4')
            username = input('Username: ')
            time.sleep(1)
            print('')
            password = input('Password: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Correct password and username!')
                    time.sleep(1)
                    print('')
                    print('Sharing passwords are a bannable offence and will be removed from the list without refund!')
                    print('')
                    break
                else:
                    print('Invalid password or username!')
                    exita = input('Would like to re-try? Y/N: ')
                    if (exita.capitalize()) == 'Y':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Invalid Response!')
        elif inad == 'Y:boosted':
            print('')
            print('Booster user login!')
            print('')
            time.sleep(1)
            pastebin = ('https://pastebin.com/raw/c254wxqt')
            username = input('Username: ')
            time.sleep(1)
            print('')
            password = input('Password: ')
            response = requests.get(pastebin).text
            for line in response.split('\n'):
                if username and password in line:
                    print('Correct password and username!')
                    time.sleep(1)
                    print('')
                    print('Sharing passwords are a bannable offence and will be removed from the list!')
                    print('')
                    break
                else:
                    print('Invalid password or username!')
                    exita = input('Would like to re-try? Y/N: ')
                    if (exita.capitalize()) == 'Y':
                        print('Returning to start!')
                        time.sleep(1)
                    elif (exita.capitalize()) == 'N':
                        time.sleep(1)
                        print('N Selected!')
                        time.sleep(1)
                    else:
                        print('Invalid Response!')
        elif (inad.capitalize()) == 'N':
            time.sleep(1)
            i = input('Would you like a uuid? this is required to purchase the full version. Y/N: ')
            if (i.capitalize()) == 'Y':
                time.sleep(1)
                print(uuid.uuid1())
                time.sleep(1)
                print('')
                print('Keep this stored as it will be your password until you request it to get changed!')
                print('')
                time.sleep(5)
            print(
                'Would you like to join the discord server? You can buy the full version there and also boosters will get more tools!')
            discord = input('Y/N? ')
            if (discord.capitalize()) == 'Y':
                webbrowser.open(url='https://discord.gg/WWWhj9z')
            break
        else:
            time.sleep(1)
            print('Invalid response!')
            time.sleep(1)
            break

    print('N Selected!')
    time.sleep(1)
    print('Free version, No booster or paid tools')
    time.sleep(1)
    print('')
    pastebin12 = ('https://pastebin.com/9qNWLYbb')
    kid = 1
    webbrowser.open_new(url='https://bit.ly/3lahict')
    print('Key Stop 1 & 2!')
    key1 = input('Key 1: ')
    key2 = input('Key 2: ')
    key12 = requests.get(pastebin12).text
    for line in key12.split('\n'):
        if key12 and key2 in line:
            print('Keys Are valid')
            time.sleep(1)
            print('')
            print('Thank you for helping support me!')
            print('')
        else:
            print('invalid')

    print('Loading')
    x = randint(3, 10)
    time.sleep(x)
    print('(##########)100% COMPLETE')
    time.sleep(0.5)
    print('Complete!')

    while True:
        time.sleep(2)
        for _ in range(40):
            print(' ')
            time.sleep(.01)

        print('  88888             8    888b.           8 ')
        print("    8   .d8b. .d8b. 8    8  .8 .d88 .d8b 8.dP ")
        print("    8   8' .8 8' .8 8    8wwP' 8  8 8    88b  ")
        print("    8   `Y8P' `Y8P' 8    8     `Y88 `Y8P 8 Yb ")
        time.sleep(2)
        print('By sɹǝƃƃod#5183')
        print('Credit to: zoony#1337 & Dropout#1337')
        print('')
        print("I am legaly not responsibile for anything that happens to you or your device! ")
        print('')
        time.sleep(1)
        print('1. Pinging tools: ')
        time.sleep(1)
        print('2. Browser history spammer: ')
        time.sleep(1)
        print('3. Computer destroyer: ')
        time.sleep(1)
        print('4. Discord spammer: ')
        time.sleep(1)
        print('5. Something idk')
        time.sleep(1)
        print('6. Other: ')
        time.sleep(1)
        print('7. Exit: ')
        time.sleep(2)
        a = int(input('Choose a Tool: '))
        if a == 1:
            print('1. Pinging tools selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
                print(
                    "██▓███   ██▓ ███▄    █   ▄████  ██▓ ███▄    █   ▄████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████")
                print(
                    "▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▓██▒ ██ ▀█   █  ██▒ ▀█▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒")
                print(
                    "▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄")
                print(
                    "▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓░██░▓██▒  ▐▌██▒░▓█  ██▓   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒")
                print(
                    "▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒░██░▒██░   ▓██░░▒▓███▀▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒")
                print(
                    "▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░")
                print(
                    "░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░  ▒ ░░ ░░   ░ ▒░  ░   ░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░")
                print(
                    "░░        ▒ ░   ░   ░ ░ ░ ░   ░  ▒ ░   ░   ░ ░ ░ ░   ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░")
                print("░           ░       ░  ░           ░       ░                 ░ ░      ░ ░      ░  ░      ░")
                print('')
                print('')
                print('')
                time.sleep(1)
                print('1. Ip/Sever tester')
                print('2. Ip Stresser')

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
                server_ip = int(input('Enter server IP : '))
                rep = os.system('ping ' + server_ip)
                if rep == 0:
                    print
                    'n n server is up n n'
                else:
                    print
                'server is down'

        elif a == 2:
            print('2. Browser history spammer selected!')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(1)
            for _ in range(15):
                print(' ')
            time.sleep(3)
            print(
                '▄▄▄▄    ██▀███   ▒█████   █     █░  ██████ ▓█████  ██▀███      ██░ ██  ██▓  ██████ ▄▄▄█████▓ ▒█████   ██▀███ ▓██   ██▓     ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███ ')
            print(
                '▓█████▄ ▓██ ▒ ██▒▒██▒  ██▒▓█░ █ ░█░▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒   ▓██░ ██▒▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒   ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒')
            print(
                '▒██▒ ▄██▓██ ░▄█ ▒▒██░  ██▒▒█░ █ ░█ ░ ▓██▄   ▒███   ▓██ ░▄█ ▒   ▒██▀▀██░▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒')
            print(
                '▒██░█▀  ▒██▀▀█▄  ▒██   ██░░█░ █ ░█   ▒   ██▒▒▓█  ▄ ▒██▀▀█▄     ░▓█ ░██ ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░     ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  ')
            print(
                '░▓█  ▀█▓░██▓ ▒██▒░ ████▓▒░░░██▒██▓ ▒██████▒▒░▒████▒░██▓ ▒██▒   ░▓█▒░██▓░██░▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒')
            print(
                '░▒▓███▀▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▓░▒ ▒  ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░    ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░')
            print(
                '▒░▒   ░   ░▒ ░ ▒░  ░ ▒ ▒░   ▒ ░ ░  ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░    ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░')
            print(
                '░ ░ ░ ░ ▒    ░   ░  ░  ░  ░     ░     ░░   ░     ░  ░░ ░ ▒ ░░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░     ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ ')
            print(
                '  ░ ░      ░          ░     ░  ░   ░         ░  ░  ░ ░        ░               ░ ░     ░     ░ ░              ░                 ░  ░       ░          ░      ░  ░   ░     ')
            print(
                '     ░                                                                                                        ░ ░          ')
            for _ in range(3):
                time.sleep(0.2)
                print(' ')
            print(
                '.............................................................................................................................................................................................')
            print(' ')
            time.sleep(1)
            print('1. Random Google Page')
            time.sleep(1)
            print('2. Random Website')
            time.sleep(1)
            print('3. Selected Website')
            time.sleep(1)
            print('4. Exit Tool')
            time.sleep(1)
            c = int(input('Choose Tool: '))
            if c == 1:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('1. Random google page selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    google_sites = ('search?q=nut&oq=nut&aqs=chrome.0.69i59.1970j0j7&sourceid=chrome&ie=UTF-8')
                elif select == 2:
                    google_sites = (
                        'search?q=history&oq=his&aqs=chrome.1.69i57j69i59l2j69i61j69i60.2720j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 3:
                    google_sites = (
                        'search?q=Yeet&oq=Yeet&aqs=chrome..69i57j69i60j69i65.1465j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 4:
                    google_sites = ('search?q=egg&oq=egg&aqs=chrome..69i57.686j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 5:
                    google_sites = (
                        'search?q=north+korea&oq=north+korea&aqs=chrome..69i57.2612j0j9&sourceid=chrome&ie=UTF-8')
                elif select == 6:
                    google_sites = (
                        'search?q=computer&oq=computer&aqs=chrome..69i57j69i61l2j69i65l2j69i61.1695j0j9&sourceid=chrome&ie=UTF-8')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)

                for _ in range(pages):
                    webbrowser.open(url=('https://www.google.com/' + google_sites), new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 2:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('2. Random website selected!')
                select = int(input('Select a number between 1-6: '))  # You can change this and add as many as you want!
                print('')
                pages = int(input('How Many Tabs: '))
                if select == 1:
                    random_sites = ('https://alwaysjudgeabookbyitscover.com/')
                elif select == 2:
                    random_sites = ('http://eelslap.com/')
                elif select == 3:
                    random_sites = ('https://smashthewalls.com/')
                elif select == 4:
                    random_sites = ('https://weirdorconfusing.com/')
                elif select == 5:
                    random_sites = ('https://trypap.com/')
                elif select == 6:
                    random_sites = ('http://www.republiquedesmangues.fr/')
                else:
                    time.sleep(1)
                    print('Wrong Option selected!')
                    time.sleep(1)
                    print('Returning to menu!')
                    time.sleep(1)
                for _ in range(pages):
                    webbrowser.open(url=random_sites, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 3:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('3. Selected website!')
                pages = int(input('How Many Tabs: '))
                website = input('Website, You dont need http/s: ')
                for _ in range(pages):
                    webbrowser.open(url='http://' + website, new=1)
                    time.sleep(1)
                print('Completed task!')
                time.sleep(2)
                print('Returning to menu!')
                time.sleep(1)

            elif c == 4:
                for _ in range(4):
                    print(' ')
                    time.sleep(.5)
                print('Exitting!!!')
                time.sleep(1)
            else:
                print('Wrong, That option does not exist!')
                time.sleep(1)
                print('Returning to menu!')
                time.sleep(1)

        elif a == 3:
            print('3. Computer Destoryer Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
            zx = input('Are you sure Y/N: ')
            if (zx.capitalize()) == 'Y':
                time.sleep(1)
                print('Destroyer Starting in 3 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 2 seconds!')
                time.sleep(1)
                print('Destroyer Starting in 1 seconds!')
                time.sleep(1)
                for _ in range(1000):
                    webbrowser.open(url='https://www.youtube.com/watch?v=i_2yNbIzwOI', new=2)
            else:
                print('')
                print('Returning to main menu!')
                time.sleep(1)

        elif a == 4:
            print('4. Discord Tools selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
                time.sleep(.1)
                print(
                    "              dddddddd                                                                                              dddddddd         ")
                print(
                    "              d::::::d  iiii                                                                                        d::::::d              tttt                                            lllllll  ")
                print(
                    "              d::::::d i::::i                                                                                       d::::::d           ttt:::t                                            l:::::l    ")
                print(
                    "              d::::::d  iiii                                                                                        d::::::d           t:::::t                                            l:::::l      ")
                print(
                    "              d:::::d                                                                                               d:::::d            t:::::t                                            l:::::l    ")
                print(
                    "      ddddddddd:::::d iiiiiii     ssssssssss       cccccccccccccccc   ooooooooooo   rrrrr   rrrrrrrrr       ddddddddd:::::d      ttttttt:::::ttttttt       ooooooooooo      ooooooooooo    l::::l     ssssssssss  ")
                print(
                    "     dd::::::::::::::d i:::::i   ss::::::::::s    cc:::::::::::::::c oo:::::::::::oo r::::rrr:::::::::r    dd::::::::::::::d      t:::::::::::::::::t     oo:::::::::::oo  oo:::::::::::oo  l::::l   ss::::::::::s  ")
                print(
                    "    d::::::::::::::::d  i::::i ss:::::::::::::s  c:::::::::::::::::co:::::::::::::::or:::::::::::::::::r  d::::::::::::::::d      t:::::::::::::::::t    o:::::::::::::::oo:::::::::::::::o l::::l ss:::::::::::::s ")
                print(
                    "   d:::::::ddddd:::::d  i::::i s::::::ssss:::::sc:::::::cccccc:::::co:::::ooooo:::::orr::::::rrrrr::::::rd:::::::ddddd:::::d      tttttt:::::::tttttt    o:::::ooooo:::::oo:::::ooooo:::::o l::::l s::::::ssss:::::s ")
                print(
                    "   d::::::d    d:::::d  i::::i  s:::::s  ssssss c::::::c     ccccccco::::o     o::::o r:::::r     r:::::rd::::::d    d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l  s:::::s  ssssss ")
                print(
                    "   d:::::d     d:::::d  i::::i    s::::::s      c:::::c             o::::o     o::::o r:::::r     rrrrrrrd:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l    s::::::s  ")
                print(
                    "   d:::::d     d:::::d  i::::i       s::::::s   c:::::c             o::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t          o::::o     o::::oo::::o     o::::o l::::l       s::::::s  ")
                print(
                    "   d:::::d     d:::::d  i::::i ssssss   s:::::s c::::::c     ccccccco::::o     o::::o r:::::r            d:::::d     d:::::d            t:::::t    tttttto::::o     o::::oo::::o     o::::o l::::l ssssss   s:::::s ")
                print(
                    "   d::::::ddddd::::::ddi::::::is:::::ssss::::::sc:::::::cccccc:::::co:::::ooooo:::::o r:::::r            d::::::ddddd::::::dd           t::::::tttt:::::to:::::ooooo:::::oo:::::ooooo:::::ol::::::ls:::::ssss::::::s")
                print(
                    "    d:::::::::::::::::di::::::is::::::::::::::s  c:::::::::::::::::co:::::::::::::::o r:::::r             d:::::::::::::::::d           tt::::::::::::::to:::::::::::::::oo:::::::::::::::ol::::::ls::::::::::::::s ")
                print(
                    "     d:::::::::ddd::::di::::::i s:::::::::::ss    cc:::::::::::::::c oo:::::::::::oo  r:::::r              d:::::::::ddd::::d             tt:::::::::::tt oo:::::::::::oo  oo:::::::::::oo l::::::l s:::::::::::ss  ")
                print(
                    "     ddddddddd   dddddiiiiiiii  sssssssssss        cccccccccccccccc   ooooooooooo    rrrrrrr               ddddddddd   ddddd               ttttttttttt     ooooooooooo      ooooooooooo   llllllll  sssssssssss     ")
                for _ in range(2):
                    print(' ')
                print('If You get banned on discord it is not my fault!')
                print('3 & 4  can result if caught in a ban!')
                for _ in range(2):
                    print(' ')
                print('1. Custom discord status')
                print('2. Text spammer')
                print('3. Multi message delete')
                print('4. Token login')
                ex = int(input('Select A Tool:'))
                if ex == 1:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 2:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 3:
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')
                elif ex == 4:
                    print('3. Multi message delete selected!')
                    print(
                        "....................................................................................................")
                    for _ in range(15):
                        print(' ')


                else:
                    time.sleep(1)
                    print(
                        "....................................................................................................")
                    time.sleep(1)
                    print('Invalid command!')
                    time.sleep(1)
                    print('Returning home!')
                    time.sleep(1)

        elif a == 5:
            print('1. Pinging tools selected!')  # gotto work on this
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
        elif a == 6:
            print('6. Other Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
        elif a == 7:
            print('7. Exit Selected')
            time.sleep(1)
            print(
                "....................................................................................................")
            time.sleep(0.1)
            for _ in range(15):
                print(' ')
            time.sleep(3)
            b = input('You sure? Y/N: ')
            if (b.capitalize()) == 'Y':
                print('Terminating in 10 seconds')
                time.sleep(5)
                print('Terminating in 5 seconds!')
                time.sleep(1)
                print('Terminating in 4 seconds!')
                time.sleep(1)
                print('Terminating in 3 seconds!')
                time.sleep(1)
                print('Terminating in 2 seconds!')
                time.sleep(1)
                print('Terminating in 1 seconds!')
                time.sleep(1)
                print('TERMINATED')
                exit()
else:
    print('Incorrect answer: If you have a language that you want to be supported please dm sɹǝƃƃod#5183')
