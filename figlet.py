""" 
PROJETO [ ClayyFiglet ]

construção do script para Social-Black
"""
import os
from time import sleep as timeout
p ='\033[34m'
c ='\033[36m'
#==============================================#
def cabecario():
	os.system("clear")
	n = input(f"DIGITE SEU NOME DONZELA ═─⟩ ")
	os.system("clear")
	arquivo = open("banner")
	print(arquivo.read())
	arquivo2 = open("Desenho")
	print(arquivo2.read())
	print(f"""{p}●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n
Olá {n}, caso queira para o progresso digite [ CTRL + c ]\n
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●""")
cabecario()
    
#==============================================#
#construção do escript [ClayyFiglet]


a = input(f"""{c} \nDigite seu Nome/Nick  ═─⟩ """)
print ("="*30)

def banner():
    print(f"{c}Gerenciando banners..........\n")
#Fonte 1
    print("Fonte = 1Row \n")
    os.system(f"figlet -f 1Row {a}")
    print ("\n")
#Fonte2
    print("Fonte = 3-D \n")
    os.system(f"figlet -f 3-D  {a}")
    print("\n")
#Fonte 3
    print("Fonte = D-ASCII \n")
    os.system(f"figlet -f 3D-ASCII {a}")
    print ("\n")
#Fonte 4
    print("Fonte = 4Max \n")
    os.system(f"figlet -f 4Max {a}")
    print("\n")
#Fonte 5    
    print("Fonte = Varsity \n")
    os.system(f"figlet -f Varsity  {a}")
#Fonte 6
    print("Fonte = Big \n")
    os.system(f"figlet -f Big  {a}")
    print ("\n")
#Fonte 7
    print("Fonte = Alpha")
    os.system(f"figlet -f Alpha {a}")
    print("\n")
    
    
banner()    
