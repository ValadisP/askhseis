f=open("mytxt.txt","r")
#Θετω τα καλα και κακα συμφωνα
kk="FCKR"
kk+=kk.lower()
kl="QWTPSDGJLZXVBNM"
kl+=kl.lower() 

lex=f.read()
lex=lex.split()
#Για καθε γραμμα καθε λεξης βλεπω αν ειναι καλο ή κακο 
for wrd in lex:
    pk=0
    pl=0
    for letter in wrd:
        if letter in list(kl):
         pl=pl+1
        elif letter in list(kk):
         pk+=1
    if (pk > pl) :
     print (wrd,"κακη")
    else:
          print (wrd,"καλη")
        
    
