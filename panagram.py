def panagram(n):
    n=n.lower()                             #converted the string into lowercase
    p=set()                                 #declare empty set
    for i in n:
        if i.isalpha():                     #if the letters are alphabet 
            p.add(i)                        # add letters into set
    print(p) 
    if len(p)==26:                          #if length of set 26 : panagram
        print("panagram")
    else:
        print("not panagram")





if __name__=="__main__":
   word=input("Enter the word you want to check: ")
   panagram(word)