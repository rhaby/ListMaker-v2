import random
import sys
import os
import time

os.system("rm number.txt")
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
print('================ letsgo ================')
#================================================
uesr = input('Domain number =》》 ')
rhaby1 = '1234567890'
print('=========================================')
rhaby2 = input('Number of mattresses=》》 ')
rhaby2 = int(rhaby2)
rhaby = input('What is a number List=》》 ')
rhaby = int(rhaby)
print('==================================')

for password in range(rhaby):
    password = ''


    for item in range(rhaby2):
         rhaby3 = ''
    for item in range(rhaby2):
        rhaby3 += random.choice(rhaby1)



    print (uesr+rhaby3)
    with open('number.txt', 'a') as x:
     x.write(uesr + rhaby3 + '\n')
    