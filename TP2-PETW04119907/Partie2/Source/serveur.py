#!/usr/bin/python3
#coding: utf8
import sys # Permet de prendre les arguments des commandes utilisateurs
import time # Permet d'utiliser l'heure POSX 
import function # Ajoute le fichier fonction

nameClient = u"" # Correspond à l'identifiant du client
ipClient = u"" # Adresse ip du client
nameServer = u"" # Correspond à l'identifiant du serveur V qui contient la ressource
nameV = u"V1"
ticket = u"" # Contient le ticket de l'utilisateur

fileKeyName = u"cles.txt" # Fichier contenant les clés
bdd = [] # Contient les données du fichiers fileKeyName
client = [] # Donnée du client de la bdd
serveur = [] # Donnée du serveur V de la bdd
durationTicket = 3600 # Temps de validité du ticket

letterToSplit = u"-" # Sert à séparer l'argument par sa concaténation
numberDataUser = 4 # Nombre de données que l'utilisateur doit donner en argument
dataUser = u""
messageBadArg = u"L'argument doit être de la forme : IDc-ADc-IDv-TICKETv."


if len(sys.argv) != 2:
    print(messageBadArg)
    sys.exit()

dataUser = function.Split(sys.argv[1], letterToSplit)

if len(dataUser) < numberDataUser:
    print(messageBadArg)
    sys.exit()

# Concaten les données supplémentaires, car la chaine à pu être cassé avec le charactère - (moins)
if numberDataUser < len(dataUser):
    dataUser[3] = function.Concaten(dataUser, numberDataUser - 1, letterToSplit)

nameClient = dataUser[0]
ipClient = dataUser[1]
nameServer = dataUser[2]
ticket = dataUser[3]

# Prend les données pour vérifier les identifiants clients et serveur
bdd = function.SplitReadFile(function.ReadFile(fileKeyName), u' ')
client = function.VerifyCell(bdd, nameClient)
serveur = function.VerifyCell(bdd, nameServer)

if not serveur: # Si le serveur n'existe pas
    print(u"Non, le serveur " + str(nameServer) + " n'est pas dans la base de données.")
    sys.exit()

serveur = function.VerifyCell(bdd, nameV)

print(u"Vous êtes le client : " + str(client[0]))
print(u"Vous souhaitez vous identifiez avec le serveur : " + str(nameServer) + u"\n")

function.FillArrayCara() # Remplis le tableau de caractère pour dé/chiffrer

# On compare les données du ticket V en le déchiffrant
ticket = function.CaesarCipher(serveur[1], ticket, -1)
dataUser = function.Split(ticket, letterToSplit)

# Si les données de l'utilisateur ne correspondent pas au ticket V
# Le nom du client, son adresse ou encore si le ticket est expiré
if nameClient != dataUser[0] or ipClient != dataUser[1] or nameV != nameServer or nameV != dataUser[2] or (int(dataUser[3]) + int(dataUser[4])) < int(time.time()):
    print(u"Non, le ticket n'est pas valide.")
    sys.exit()

print(u"OK")
sys.exit()