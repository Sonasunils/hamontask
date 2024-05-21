def palindrome(n):
    
    # n=n.lower()                           #converted into lowercase
    # k=n[::-1]                             #reverse the word into variable k
    # if n==k:                              #check the if condition where user enterd word and reversed word are same
    #     print(n,"is palindrome")
    # else:
    #     print(n,"not palindrome")
    
    # 2nd method using for loop

    n=n.lower()
    l=len(n)                                #get length of the string
    s=""
    for i in range(l-1,-1,-1):
       
       s+=n[i]
    if s==n:                               #check the if condition where user enterd word and reversed word are same
        print(n,"is palindrome")
    else:
        print(n,"not palindrome")





if __name__=="__main__":
   word=input("Enter the word you want to check: ")
   palindrome(word)