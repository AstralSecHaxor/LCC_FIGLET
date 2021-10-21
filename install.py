#! /bin/python3
import os

#<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>#
#~~~~~~~~~~~~~INSTALAÇÃO~~~~~~~~~~~~#
os.system("clear")
os.system("figlet -f Varsity Clayy404")
print(" ")
os.system("apt update && pkg upgrade")

print("Instalando FIGLET.........")
os.system("apt install figlet")
os.system("clear")

print("Instalando TOILET.......")
os.system("apt install toilet")
print(" ")

print("Instalando COWSAY........")
os.system("figlet -f Varsity cowsay")
os.system("apt install cowsay")
print(" ")

print("Instalando NODE-JS.......")
os.system("figlet -f Varsity  NodeJs")
os.system("apt install nodejs")
print(" ")

print("Instalando FIGLET-cli.......")
os.system("npm install figlet")
os.system("figlet -f Varsity figlet CLI")
os.system("npm install -g figlet-cli")
os.system("cowsay Finished")
os.system("figlet -f small Done!")
print(" ")
os.system("figlet -f 4Max completo!")
