#!/usr/bin/python3
#coding: utf8
import sys # Permet de prendre les arguments des commandes utilisateurs
import time # Permet d'utiliser l'heure POSX 
import function # Ajoute le fichier fonction

nameClient = u"" # Correspond à l'identifiant du client
ipClient = u"" # Adresse ip du client
nameTgs = u"" # Correspond à l'identifiant du serveur tgs
ticket = u"" # Contient le ticket de l'utilisateur

fileKeyName = u"cles.txt" # Fichier contenant les clés
bdd = [] # Contient les données du fichiers fileKeyName
client = [] # Donnée du client de la bdd
tgs = [] # Donnée du serveur tgs de la bdd
durationTicket = 3600 # Temps de validité du ticket

letterToSplit = u"-" # Sert à séparer l'argument par sa concaténation
numberDataUser = 3 # Nombre de données que l'utilisateur doit donner en argument
dataUser = u""
messageBadArg = u"L'argument doit être de la forme : IDc-ADc-IDtgs."


if len(sys.argv) != 2:
    print(messageBadArg)
    sys.exit()

dataUser = function.Split(sys.argv[1], letterToSplit)

if len(dataUser) != numberDataUser:
    print(messageBadArg)
    sys.exit()

nameClient = dataUser[0]
ipClient = dataUser[1]
nameTgs = dataUser[2]

# Prend les données pour vérifier les identifiants clients et serveur
bdd = function.SplitReadFile(function.ReadFile(fileKeyName), u' ')
client = function.VerifyCell(bdd, nameClient)
tgs = function.VerifyCell(bdd, nameTgs)

if not client or not tgs: # Si le client ou le serveur n'existe pas
    if client:
        print(u"Le serveur " + str(nameTgs) + " n'est pas dans la base de données.")

    else: # Si le serveur tgs existe
        print(u"Le client " + str(nameClient) + " n'est pas dans la base de données.")
    sys.exit()


print(u"Vous êtes le client : " + str(client[0]))
print(u"Vous souhaitez vous identifiez avec le serveur TGS : " + str(nameTgs) + u"\n")

function.FillArrayCara() # Remplis le tableau de caractère pour dé/chiffrer

ticket = function.CaesarCipher(tgs[1], str(sys.argv[1]) + str(letterToSplit) + str(int(time.time())) + str(letterToSplit) + str(durationTicket), 1)

print(u"Ticket TGS : " + str(ticket))
print(u"Ticket TGS chiffrer avec la clé du client : " + str(function.CaesarCipher(client[1], ticket, 1)))