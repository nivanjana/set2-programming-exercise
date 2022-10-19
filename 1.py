'''
Question 1

Implement a compression algorithm that accepts a string and compresses it. It compresses it by representing repeating characters as numbers. A compressed string starts and ends with the minus symbol. A space character is compressed to a dot symbol. 
Input                      Output

bookkeeper                 -bo2k2e2per-
iiiiiiiiiiiiiiiiiiii       -i20-
uuu    b                   -u3.4b-


Test Cases:

a)
Input
 
sizzlers winning assassins
 
Output
 
-siz2lers.win2ing.as2as2ins-


b)
Input

2122232425    hello       space!

Output

-212332425.4hel2o.7space!-

    
    '''

#code
def comprize(s):
    new = "-"
    i = 0
    while i<len(s):
        c=1
        if s[i]==' ' or s[i]=='\t':
            new+='.'
        else:
            new+=s[i]
        while i+1<len(s) and s[i+1]==s[i]:
            c+=1
            i+=1
        i+=1
        if c>1:
            new+=str(c)
    new+='-'
    return new


#main
s = input("\nEnter Input:")
ans = comprize(s)
print("\nYour Answer:",ans,"\n")
out = input("Enter Correct Output:")
if ans == out:
    print("Test case passed\n")
else:
    print("Test case failed:(")