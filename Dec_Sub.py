####################################################################################################
# Dec_Sub.py
# Substitution decryption functions
# Written by - Ravi Padma
####################################################################################################

import random, sys
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def key(message):

    #message = 'zdjehypkhpoybpjfpevpasnxahfyoopehakhdspjfpwndktewfyhffpsepoxykxoyhjeyjwaejfpzpejnxjyupeyjwaejfpwnsejnxjyupeyjwaejfpampnxwyetnuyjwaejfpampnxxnnoyefkpeeyjwaejfppvnhfnxzpoypxyjwaejfppvnhfnxykhsptdoyjqyjwaejfpepaenknxoymfjyjwaejfpepaenknxtasbkpeeyjwaejfpevsykmnxfnvpyjwaejfpwykjpsnxtpevayswpfatprpsqjfykmzpxnspdewpfatknjfykmzpxnspdewpwpspaoomnykmtysphjjnfparpkwpwpspaoomnykmtysphjjfpnjfpswaqykefnsjjfpvpsyntwaeenxasoybpjfpvspepkjvpsyntjfajenupnxyjeknyeypejadjfnsyjypeykeyejptnkyjezpykmsphpyrptxnsmnntnsxnspryoykjfpedvpsoajyrptpmsppnxhnuvasyenknkoqauyktkppteznnbeaeaewnstkppteawfpjejnkpyxyjyejnbppvyjeptmp'
    #print(message)
    a=[]
    message = message.upper()
    for i in LETTERS:
        #print(i,message.count(i))
        a.append([message.count(i),i])

    a.sort(reverse=True)
    print("Character Count:",a)
    t=['E','T','AINOS','INOSA','NOSIA','OSAIN','SAINO','H','R','D','L','U','CM','MC','F','YW','WY','GP','PG','B','V','K','Q','JX','XJ','Z']
    b=[]
    x=0
    #print(t)
    for j in a:
        #print(j[0],j[1],t[x])
        b.append([j[0],j[1],t[x]])
        #w="t"+str(x)
        #print(w)
        x=x+1
    print("Mapping:",b)
    
    

def main(message):

    a=[]
    print()
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            message = f.read()
    mode = "D" #input("E for Encrypt, D for Decrypt: ")
    key = ''
    while checkKey(key) is False:
        #key = input("Enter 26 ALPHA key (leave blank for random key): ")
        #if key == '':
        for i in range(50000):
          key = getRandomKey()

          if(i == 800):
              key='akqushxcztnjgoleyvrdmpwfib'
              key=key.upper()
          print("Key:",key)
          if checkKey(key) is False:
            print('There is an error in the key or symbol set.')

          translated = translateMessage(message, key, mode)

          #print('Using key: %s' % (key))

          if len(sys.argv) > 1:
             fileOut = 'enc.' + sys.argv[1]
             with open(fileOut, 'w') as f:
               f.write(translated)
               print('Success! File written to: %s' % (fileOut))
          else: 
              #print('Result: ' + translated)
              res=comparedict(translated.upper())
              #a.append([])
              print("Plain Text:",translated.upper())
              print("Score",res)
              #for j in range(2):
                #print(i)
              a.append([res,key,translated.upper()])
                #a.append(res)
                #print(a)
        print("*" * 30)
        a.sort(reverse=True)
        for i in range(10):
            print("Score:",a[i][0])
            print("Final Key:",a[i][1])
            print("Final Plain Text:",a[i][2])
            

        
def comparedict(txt):
    #print('Comparedict:' + txt)
    file = open("dictionary.txt")

# reading the file as a list line by line
    lines = file.readlines()
    sco=0
    for line in lines:
        #print(line.strip())
        if(txt.find(line.strip()) > 0):
           #print("text" + txt)
         sco=sco+1 
    #print('score',sco) 
    return sco    

# closing the file
    file.close()

# Store the key into list, sort it, convert back, compare to alphabet.
def checkKey(key):

    keyString = ''.join(sorted(list(key)))
    return keyString == LETTERS

def translateMessage(message, key, mode):

    translated = ''
   
    charsA=key
    charsB=LETTERS

    # If decrypt mode detected, swap A and B
    if mode == 'D':
        charsA, charsB = charsB, charsA
    #print(charsA,charsB)
    for symbol in message:
        #print(symbol)
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            #print(symIndex)
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol

    return translated



def getRandomKey():
    randomList = list(LETTERS)
    random.shuffle(randomList)
    return ''.join(randomList)

if __name__ == '__main__':
    message = 'zdjehypkhpoybpjfpevpasnxahfyoopehakhdspjfpwndktewfyhffpsepoxykxoyhjeyjwaejfpzpejnxjyupeyjwaejfpwnsejnxjyupeyjwaejfpampnxwyetnuyjwaejfpampnxxnnoyefkpeeyjwaejfppvnhfnxzpoypxyjwaejfppvnhfnxykhsptdoyjqyjwaejfpepaenknxoymfjyjwaejfpepaenknxtasbkpeeyjwaejfpevsykmnxfnvpyjwaejfpwykjpsnxtpevayswpfatprpsqjfykmzpxnspdewpfatknjfykmzpxnspdewpwpspaoomnykmtysphjjnfparpkwpwpspaoomnykmtysphjjfpnjfpswaqykefnsjjfpvpsyntwaeenxasoybpjfpvspepkjvpsyntjfajenupnxyjeknyeypejadjfnsyjypeykeyejptnkyjezpykmsphpyrptxnsmnntnsxnspryoykjfpedvpsoajyrptpmsppnxhnuvasyenknkoqauyktkppteznnbeaeaewnstkppteawfpjejnkpyxyjyejnbppvyjeptmp'
    print("Cipher Text",message)
    key(message)
    main(message)