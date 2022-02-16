bill=int(input("enter yourbill"))
paid=int(input("enter paid amount"))
balance= paid-bill
    
if balance>=50:
    fifty=int(balance/50)
    print("£50 notes",fifty)
    balance=balance-(fifty*50)
if balance>=20:
    twenty=int(balance/20)
    print("20 notes",twenty)
    balance=balance-(twenty*20)
if balance>=10:
    ten=int(balance/10)
    print("£10 notes",ten)
    balance=balance-(ten*10)
if balance>=5:
    five=int(balance/5)
    print("£5 notes",five)
    balance=balance-(five*5)
if balance>=2:
    two=int(balance/2)
    print("£2 notes",two)
    balance=balance-(two*2)
if balance>=1:
    print("£1 note",one)
    