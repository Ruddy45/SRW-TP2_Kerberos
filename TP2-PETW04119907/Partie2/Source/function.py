import string # Sert juste à remplir le tableau des caractères possibles pour le chiffrement


arrayCara = [] # Tableau utilisé pour le chiffrement par décalage


# Lit un fichier
def ReadFile(_fileName):
    res = []
    try:
        with open(_fileName, "rt") as fileToRead:
            res = fileToRead.readlines()
            fileToRead.close()

    except FileNotFoundError: # Si le fichier n'existe pas
        print("Le fichier " + str(_fileName) + " est introuvable.")

    finally:
        return res


# Casse les chaines de caractères selon un caractère, Ici l'argument
def Split(_line, _split):
    _line = _line.split(_split, _line.count(_split))
    return _line


# Casse les données du fichier cles.txt pour avoir un tableau avec l'identifiant et la clé
def SplitReadFile(_data, _split):
    res = []
    for oneLine in _data:
        oneLine = oneLine.split(_split, oneLine.count(_split))
        oneLine[1] = oneLine[1].rstrip()
        res.append(oneLine)

    return res


# Concatenne le ticket quand il à pour caractère -
def Concaten(_tabToConcaten, _indexBegin, _letterToSplit):
    res = u""

    for i in range(_indexBegin, len(_tabToConcaten)):
        res += _tabToConcaten[i]

        if i < len(_tabToConcaten) - 1:
            res += _letterToSplit

    return res


# Vérifie si un champs est bien dans un tableau / base de données
# Pour le client et le tgs, retourne leurs noms et clés
# Avec arrayCara, on peut obtenir l'index d'un caractère
def VerifyCell(_bdd, _idToSearch):
    resCell = [] # Contiendra la cellule
    for oneCell in _bdd:
        if oneCell[0] == _idToSearch:
            resCell = oneCell
    
    return resCell


# Remplie le tableau avec les caractères utilisés pour le chiffrement
def FillArrayCara():
    letters = string.ascii_uppercase + string.ascii_lowercase # Lettre majuscules et minuscules
    letters += string.digits + u"@.,!?:;-=%" # Chiffres et symboles
    i = 0

    for i in range(0, len(letters)):
        arrayCara.append([letters[i], i])


# Chiffrement par décalage, _multiplier que la fonction chffre et déchiffre en même temps (-1 ou 1)
def CaesarCipher(_key, _msgToCipher, _multiplier):
    resCipher = u""
    iLetterMessage = 0 # Index correspondant à la lettre d'un caractère du message
    iLetterKey = 0 # Index correspondant à la lettre d'un caractère de la clé
    newIndexMsg = 0 # Nouvel index du message
    
    y = 0
    for oneCell in _msgToCipher: # Pour chaque caractère du message
        iLetterMessage = VerifyCell(arrayCara, oneCell)

        if y == len(_key):
            y = 0
        iLetterKey = VerifyCell(arrayCara, _key[y])

        newIndexMsg = iLetterMessage[1] + iLetterKey[1] * _multiplier
        if newIndexMsg < 0:
            newIndexMsg = len(arrayCara) - (newIndexMsg * (-1))
        newIndexMsg %= len(arrayCara)

        resCipher += arrayCara[newIndexMsg][0]
        y +=1
    

    return resCipher


# Affiche un tableau
def DisplayTab(_tabToDisplay):
    for oneCell in _tabToDisplay:
        print(str(oneCell))