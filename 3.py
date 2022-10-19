'''

Given 3 strings: first,  second, and third,  write a program to check whether the third string is a shuffle of first and second strings. 
The string is considered a shuffle only if the characters of the first and second string come in the third string in a way that maintains the left to the right ordering of the characters from each string.
Constraints to qualify as a valid shuffle:
– All characters in the first and the second strings should be present in the third string.
– Third string should contain all characters in the first string in the same order as they appear in the first string. Similarly, the third string should also contain all characters in the second string in the same order as they appear in the second string.

Example 1

Input: 
"abc" 
"def", 
"Adbefc"

Output: 1
 
Example 2

Input: 
"nyc"
"pak"
"npcayk"
Output: 0

Test Cases:

a)

Input
 
one
two
Twoone
 
Output
1
 
b)
 
Input
 
oneoneone
twotwotwo
Twoone
 
Output
0

            '''



s1 = input().lower()
s2 = input().lower()
s = input().lower()
k=0
j=0
for i in range(len(s)):
    if j<len(s1) and s[i]==s2[j]:
        j+=1
    if k<len(s2) and s[i]==s1[k]:
        k+=1
if j==len(s1) and k==len(s2):
    print(1)
else:
    print(0)
