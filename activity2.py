def palindrome(r):
    e=len(r)-1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s=s+1
        e=e-1
    return True

r=('r','a','c','e','c','a','r')
if(palindrome(r)):
    print("The tuple is palindrome")
else:
    print("The tuple is not palindrome")