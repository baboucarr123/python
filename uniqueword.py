from hashlib import new


uniquewords=[]
def findunique(word):
    for w in uniquewords:
        if w==word:
            return False
    uniquewords.append(word)
    return True

def removeduplicates(msg):
    newmsg=""
    word=""
    counter=0
    while counter<len(msg):
        if msg[counter]==" ":
            if findunique(word):
                newmsg=newmsg+word+" "
            word=""
        else:
            word=word+msg[counter]
        counter=counter+1
    if findunique(word):
        newmsg=newmsg+word
    print(newmsg)

removeduplicates("hello hi hello hi shafeeq shafeeq hi")







