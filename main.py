import uuid, socket, ipaddress, webbrowser, platform, os, time, requests, random, sys
from clear_screen import clear
from random import *
#my_ip = ipaddress.ip_address('--0.--0.--0.-0') #Random choices and other shit goes here since it is just cleaner
print('Tools pack')
time.sleep(1)
print('Detecting ip...')
x = randint(1,4)
time.sleep(x)
print('---.---.---.-' + ' Has been detected') #still working on it
time.sleep(1)
x = randint(1,4)
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
while kid < 2:
    print('Key Stop 1 & 2!')
    key1 = input('Key 1: ')
    key2 = input('Key 2: ')
    key12 = requests.get(pastebin12).text
    for line in response.split('\n'):
        if key12 and key2 in line:
            print('Keys Are valid')
            time.sleep(1)
            print('')
            print('Thank you for helping support me!')
            print('')
            break
        else:
            print('Incorrect')
print('Loading')
x = randint(3,10)
time.sleep(x)
print('(##########)100% COMPLETE')
time.sleep(0.5)
print('Complete!')

while True:
    time.sleep(2)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print('')
    time.sleep(.1)

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
            print("██▓███   ██▓ ███▄    █   ▄████  ██▓ ███▄    █   ▄████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████")
            print("▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▓██▒ ██ ▀█   █  ██▒ ▀█▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒")
            print("▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄")
            print("▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓░██░▓██▒  ▐▌██▒░▓█  ██▓   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒")
            print("▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒░██░▒██░   ▓██░░▒▓███▀▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒")
            print("▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░")
            print("░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░  ▒ ░░ ░░   ░ ▒░  ░   ░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░")
            print("░░        ▒ ░   ░   ░ ░ ░ ░   ░  ▒ ░   ░   ░ ░ ░ ░   ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░")
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
            select = int(input('Select a number between 1-6: ')) # You can change this and add as many as you want!
            print('')
            pages = int(input('How Many Tabs: '))
            if select == 1:
                google_sites = ('search?q=nut&oq=nut&aqs=chrome.0.69i59.1970j0j7&sourceid=chrome&ie=UTF-8')
            elif select == 2:
                google_sites = ('search?q=history&oq=his&aqs=chrome.1.69i57j69i59l2j69i61j69i60.2720j0j9&sourceid=chrome&ie=UTF-8')
            elif select == 3:
                google_sites = ('search?q=Yeet&oq=Yeet&aqs=chrome..69i57j69i60j69i65.1465j0j9&sourceid=chrome&ie=UTF-8')
            elif select == 4:
                google_sites = ('search?q=egg&oq=egg&aqs=chrome..69i57.686j0j9&sourceid=chrome&ie=UTF-8')
            elif select == 5:
                google_sites = ('search?q=north+korea&oq=north+korea&aqs=chrome..69i57.2612j0j9&sourceid=chrome&ie=UTF-8')
            elif select == 6:
                google_sites = ('search?q=computer&oq=computer&aqs=chrome..69i57j69i61l2j69i65l2j69i61.1695j0j9&sourceid=chrome&ie=UTF-8')
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
        print('4. Discord spammer selected')
        time.sleep(1)
        print(
            "....................................................................................................")
        time.sleep(0.1)
        for _ in range(15):
            print(' ')
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