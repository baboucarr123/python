def wordcount(msg):
    space=0
    i=0
    while i<len(msg):
        if msg[i]==" ":
            space=space+1
        i=i+1
    print("we have found:", space +1)


    
wordcount("welcome to nbs")