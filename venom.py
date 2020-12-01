#!/usr/bin/python
import requests
from colorama import Fore
from bs4 import BeautifulSoup
import random
import os 
from faker import Faker

fake = Faker('hi_IN')

os.system('clear')
w = Fore.WHITE
g = Fore.GREEN
r = Fore.RED
c = Fore.CYAN
y = Fore.YELLOW
b = Fore.BLUE

colors = (w, g, r, c, y, b)
color = random.choice(colors)

banner = '''

██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗       ██████╗ ██████╗        ██████╗ ███████╗███╗   ██╗
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║      ██╔════╝██╔════╝       ██╔════╝ ██╔════╝████╗  ██║
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗██║     ██║     █████╗ ██║  ███╗█████╗  ██╔██╗ ██║
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██║     ██║     ╚════╝ ██║   ██║██╔══╝  ██║╚██╗██║
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ╚██████╗╚██████╗       ╚██████╔╝███████╗██║ ╚████║
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝       ╚═════╝ ╚═════╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝

     [+] Created By Venom
     [+] Instagram: i.m.gauravchaudhary
     [+] Whatsapp: +91 9910332273

     [+] -----------------------------------------------[+]
  
    
     [1] Visa
     [2] MasterCard
     [3] American Express
     [4] Discover

'''
print(color + banner + color)
card = input(w + '     [+] ' + w + color + 'Enter the Card No. You want to continue with: ' + color)
quantity = int(input(w + '     [+] ' + w + color + 'Enter the Number of card You want (should be equal to or less than 15): ' + color))
_card = []
if card == '1':
    _card.append('VISA')
elif card == '2':
    _card.append('MASTERCARD')
elif card == '3':
    _card.append('AMERICAN+EXPRESS')
elif card == '4':
    _card.append('DISCOVER')
else:
    print(w + '     [+] ' + w + r + ' I do not understand you' + r)
url = 'https://www.coolgenerator.com/credit-card-generator-india'
headers = {'Referer': 'https://www.coolgenerator.com/credit-card-generator-india'}
data = 'cardbrand=' + str(_card[0]) + '&quantity=' + str(quantity) + '&name=on'
response = requests.post(url, headers=headers, data=data)
soup = BeautifulSoup(response.content, 'html.parser')
number = soup.findAll('p', class_="text-center font-18")
info = soup.findAll('p', class_="text-center grey")
_info = []
issuer = []
expiry = []
expiry_date = []
cvv_number = []
bank = []
#card numbers####################
card_numbers = []		#
for i in number:		#
    i = str(i)			#
    _i = i[71:-15]              #
    card_numbers.append(_i)	#	
#################################
#info 28
#expiry #42:
#cvv 43:11
for i in info:
    venom = str(i)
    ok = venom[28:]
    _info.append(ok)
for i in _info:
    _i = str(i)
    if _i.startswith('Expiry:') is True:
    	expiry.append(_i)
    else:
    	issuer.append(_i)
#expiry date
for i in expiry:
    _i = str(i)
    date = _i[14:-36]
    expiry_date.append(date)
#################
#cvv
for i in expiry:
    _i = str(i)
    cvv = _i[43:-11]
    cvv_number.append(cvv)
##################
#bank -> 14:25
for i in issuer:
    devil = str(i)
    _bank = devil[14:-25]
    bank.append(_bank)
x = 0
print(' ')
while x < quantity:
      print(w + '     [+] ' + w + color + 'Card Number: ' + color + g + card_numbers[x] + g)
      print(w + '     [+] ' + w + color + 'Expiry: ' + color + g + expiry_date[x] + g)
      print(w + '     [+] ' + w + color + 'CVV: ' + color + g + cvv_number[x] + g)
      print(w + '     [+] ' + w + color + 'Issuer: ' + color + g + bank[x] + g)
      print(w + '     [+] ' + w + color + 'Card Holder Name: ' + color + g + str(fake.name()) + g)
      print(' ')
      x += 1

