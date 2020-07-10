import random
import sys
import os
import time

os.system("rm NumberIQ.txt")
os.system("clear")
print("      Author | arhaby")
time.sleep(1)
print('')
print("         Telegram | @rhaby")
time.sleep(1)
print('')
print("            ChannelTelegram | @ciku370")
time.sleep(1)
print('')
print("                List-Maker ArHaBy v2")
time.sleep(1)
print('================ letsgo ================')
#================================================
uesr = '077' 
uesr2 = '079'
uesr3 = '078'
uesr4 = '075'
rhaby4 = '1234567890'

rhaby = input('What is a number List: ')
rhaby = int(rhaby)
rhaby2 = '8'
rhaby2 = int(rhaby2)

print('==================================')

for rhaby3 in range(rhaby):
    rhaby3 = ''


    for item in range(rhaby2):
         rhaby3 = ''
    for item in range(rhaby2):
        rhaby3 += random.choice(rhaby4)



    print (uesr+rhaby3)
    print (uesr2+rhaby3)
    print (uesr3+rhaby3)
    print (uesr4+rhaby3)
    with open('NumberIQ.txt', 'a') as x:
     x.write(uesr + rhaby3 + '\n')
     x.write(uesr2 + rhaby3 + '\n')
     x.write(uesr3 + rhaby3 + '\n')
     x.write(uesr4 + rhaby3 + '\n')