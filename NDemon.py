import os
import sys
import requests
import json
from time import sleep

demon = """
══════════════════█════════════════█ 
═════════════════██════════════════██
═══════════════███══════════════════███
═════════════████════════════════════████
════════════█████════════════════════█████
═══════════█████══════════════════════█████
══════════██████══════════════════════██████
══════════███████══████████████████══███████
══════════██████████████████████████████████
═══════════████████████████████████████████
════════════████████════██████════████████ 
═══█════════███████══════████══════███████
═══█═══════████████═══▓═█████══▓══████████ 
══███══════█████████════██████════█████████ 
══███═════██████████████████████████████████ 
═█████════██████████████████████████████══██ 
═█████════███══████████████████████████══███ 
═══██═════███══████████████████████████══███ 
═══██══════███═════████████████████═════██ 
════██══════██════════██████████═══════██ 
═════██══════███═══════════════════════█ 
═════██════════██════███████████══════█ 
══════██════════███═════███████████══█ 
═══════██══════════███═════██████████ 
═════════██═══════════█████══█████████ 
═════════════════════════════██████████ 
══════════════════════════════█████████ 
═══════════════════════════════███████ 

═══════ WELCOME TO NIGTHTS DEMONS ═══════

"""

intro = r"""
 _   _ _____
| \ | |  __ \                            
|  \| | |  | | ___ _ __ ___   ___  _ __  
| . ` | |  | |/ _ \ '_ ` _ \ / _ \| '_ \ 
| |\  | |__| |  __/ | | | | | (_) | | | |
|_| \_|_____/ \___|_| |_| |_|\___/|_| |_|
      
"""

menu = """
[1] IP info
[2] Number Phone Info
"""
def ipinfo():
	print(	"Введите айпи!"	)
	ip = input("[IP] : ")
	response = requests.get(	"https://ipinfo.io/" + ip + "/json"	)
	r = response.json()	
	try:
	  try:   
	    print(	"[country] : " + r['country']	)
	  except:
	    pass
	  try:  
	    print(	"[region] : " + r['region']	)
	  except:
	    pass
	  try:   
	    print(	"[city] : " + r['city']	)
	  except:
	    pass
	  try:   
	    print(	"[hostname] : " + r['hostname']	)
	  except:
	    pass
	  try:   
	    print(	"[loc] : " + r['loc']	)
	  except:
	    pass
	  try:   
	    print(	"[org] : " + r['org']	)
	  except:
	    pass
	  try:   
	    print(	"[timezone] : " + r['timezone']	)
	  except:
	    pass
	  try:   
	    print(	"[postal] : " + r['postal']	)
	  except:
	    pass
	except Exeption as er:
	  print(er)

def numberinfo():
	number = input("[PHONE] +")
	response = requests.get("https://htmlweb.ru/geo/api.php?json&telcod=" + number)
	infoPhone = response.json()
	try:
		print(	"[Номер] +" + number )
		print(	"[Часть света] : " + infoPhone["country"]["location"] )
		print(  "[Страна] : " + infoPhone["country"]["name"] )
		print(  "[Регион] : " + infoPhone["region"]["name"] )
		print(  "[Округ] : " + infoPhone["region"]["okrug"] )
		print(  "[Оператор] : " + infoPhone["0"]["oper"] )
		
	except:
		print('Номер не существует!')
    
def menu1():
	os.system('clear')
	print(intro)
	print(menu)
	num = input(	"[!] > "	)
	if num == "1":
		ipinfo()
	if num == "2":
		numberinfo()
	else:
		menu()

os.system("clear")
print(demon)
os.system('play-audio dem.mp3')
menu1()
