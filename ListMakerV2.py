import random
import sys
import os
import time

os.system("rm list.txt")
os.system("clear")
print("                Author | arhaby")
time.sleep(1)
print('')
print("                Telegram | @rhaby")
time.sleep(1)
print('')
print("                ChannelTelegram | @ciku370")
time.sleep(1)
print('')
print("                List-Maker ArHaBy v2")
time.sleep(1)
print('=========================================')
print('$Example Domain email')
print('1-   @gmail.com')
print('1-   @hotmail.com')
print('1-   @yahoo.com')
print('1-   @outlook.com')
print('================ letsgo ================')
#================================================
uesr = input('username =》》 ')
rhaby1 = '1234567890qwertyuiopasdfghjklzxcvbnm._'
email = input('Domain email =》》 ')
print('=========================================')
rhaby = input('What is a number List=》》 ')
rhaby = int(rhaby)
rhaby2 = input('Number of mattresses=》》 ')
rhaby2 = int(rhaby2)
print('==================================')

for password in range(rhaby):
    password = ''


    for item in range(rhaby2):
         rhaby3 = ''
    for item in range(rhaby2):
        rhaby3 += random.choice(rhaby1)



    print (uesr+rhaby3+email)
    with open('list.txt', 'a') as x:
     x.write(uesr + rhaby3 + email + '\n')
