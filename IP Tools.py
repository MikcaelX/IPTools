#coding:utf-8

import os
import time
import webbrowser
from requests import get
import sys


print("                                IP TOOLS                                  ")
print("_|_|_|  _|_|_|        _|_|_|_|_|    _|_|      _|_|    _|          _|_|_|  ")
print("  _|    _|    _|          _|      _|    _|  _|    _|  _|        _|        ")
print("  _|    _|_|_|            _|      _|    _|  _|    _|  _|          _|_|    ")
print("  _|    _|                _|      _|    _|  _|    _|  _|              _|  ")
print("_|_|_|  _|                _|        _|_|      _|_|    _|_|_|_|  _|_|_|    ")
print("                                                       by Mikcael.exe#8186\n")

time.sleep(1)

try:
	os.system("echo Vérification de l'OS...")
except:
	print("\n /!\ CRITICAL ERROR /!\ ")
	print("Veuillez utiliser Windows (CE = ExOS1")
	sys.exit()
os.system("color 0C")
os.system("title IP TOOLS - Dev by Mikcael")
print("[+] OS OK !")


print("Gestion des APIs...")
try:
	ipv4 = get('https://api.ipify.org').text
	ipv6 = get('https://api6.ipify.org').text
	discordStat = get('https://srhpyqt94yxb.statuspage.io/api/v2/summary.json')
except:
	os.system("color 40")
	print("\n /!\ CRITICAL ERROR /!\ ")
	print("Recherche du problème en cours...")
	os.system("ping api.ipify.org -n 1")
	print("\n\nUne erreur est survenu, vous connectez a internet ou relancer le programme peux régler le problème (CE = Ex1N)")
	input("Press Enter to continue...")
	os.system("color 0F")
	sys.exit()
print("[+] APIs OK !")

cmd = 0


while cmd == 0:	
	print("             ____________________________________________________")
	print("            /                                                    \"")
	print("           |    _____________________________________________     |")
	print("           |   |                                             |    |")
	print("           |   |  C:\> _                                     |    |")
	print("           |   |                                             |    |")
	print("           |   |  1 - IP Ping                                |    |")
	print("           |   |                                             |    |")
	print("           |   |  2 - Port Scan                              |    |")
	print("           |   |                                             |    |")
	print("           |   |  3 - Quelle est mon ip Publique ?           |    |")
	print("           |   |                                             |    |")
	print("           |   |  4 - Discord                                |    |")
	print("           |   |                                             |    |")
	print("           |   |  5 - Quitter                                |    |")
	print("           |   |                                             |    |")
	print("           |   |_____________________________________________|    |")
	print("           |                                                      |")
	print("            \_____________________________________________________/")
	print("                   \_______________________________________/")
	print("                _______________________________________________")
	print("             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_")
	print("          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_")
	print("       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_")
	print("    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_")
	print(" _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_")
	print(":-----------------------------------------------------------------------------:")
	print("`---._.-----------------------------------------------------------------._.---'")

	cmd = input("\n 	=> ")
	try: 
		cmd = int(cmd)
	except:
		if cmd != "debug":
			print("Argument non valide ! (CE = Ex1V)")
	if cmd == 1:
		pinghost = input("IP ou address à ping => ")
		pingnb = input("Nombre de ping a envoyer => ")
		os.system("ping {} -n {}".format(pinghost, pingnb))
		input("Press Enter to continue...")
		cmd = 0
	elif cmd == 2:
		os.system("netstat -ano")
		input("Press Enter to continue...")
		cmd = 0
	elif cmd == 3:
		if ipv4 != "":
			print("IPV4 = {}".format(ipv4))
		else:
			print("IPV4 = Invalide (indisponible ou inexistante)")
		if ipv6 != "":
			print("IPV6 = {}".format(ipv6))
		else:
			print("IPV6 = Invalide (indisponible ou inexistante)")
		input("Press Enter to continue...")
		cmd = 0
	elif cmd == 4:
		try:	
			webbrowser.open('https://discord.gg/jjdc6AK')
		except:
			print(discordStat)
			print("Impossible d'ouvrir discord.gg (CE = Ex2N)") 
		cmd = 0
	elif cmd == 5:
		cmd == 0.1
	elif cmd == "debug":
		print("CE = Ex@V = Erreur de variable")
		print("CE = Ex@N = Erreur du réseau")
		print("CE = ExOS@ = Erreur du system")
		print("@ = Numéro de l'erreur")
		time.sleep(4)
		input("Press Enter to continue...")
		cmd = 0
	else:
		print("Argument Inconnu ! (CE = Ex2V")
		cmd = 0
	os.system("cls")

print("                    _________________________________________________")
print("            /|     |     _______    __________  ____  __   ____      |")
print("            ||     |    /  _/ _ \  /_  __/ __ \/ __ \/ /  / __/      |")
print("       .----|-----,|   _/ // ___/   / / / /_/ / /_/ / /___\ \        |")
print("       ||  ||   ==||  /___/_/      /_/  \____/\____/____/___/        |")
print("  .-----'--'|   ==||                                      by Mikcael |")
print("  |)-      ~|     ||_________________________________________________|")
print("  | ___     |     |____...==..._  >\______________________________|")
print(" [_/.-.\"--\"-------- //.-.  .-.\\/   |/            \\ .-.  .-. //")
print("   ( o )`===\"""""""""`( o )( o )     o              `( o )( o )` ")
print("    '-'                 '-'  '-'                       '-'  '-'")
print("Merci d'avoir utiliser IP TOOLS de Mikcael.exe#8186")
time.sleep(4)