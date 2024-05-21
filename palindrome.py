def palindrome(n):
    
    n=n.lower()             #converted into lowercase
    k=n[::-1]               #reverse the word into variable k
    if n==k:                         #check the if condition where user enterd word and reversed word are same
        print(n,"is palindrome")
    else:
        print(n,"not palindrome")





if __name__=="__main__":
   word=input("Enter the word you want to check: ")
   palindrome(word)