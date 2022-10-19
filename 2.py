"""

program should read an alphanumeric string say, “a6b5c3” , where a, b, c can be either 
*, +, -, number which should read from input. And should output evaluated expression 

Input: a6b5c3
a ? -
b ? +
c ? 5

Output : 547 (evaluated result of -6+553)


     """


s = input()
c = 0
for i in s:
    if i>='a' and i<='z' or i>='A' and i<='z':
        c+=1
for i in range(c):
    n = input().split(" ? ")
    s = s.replace(n[0],n[1])
try:
    print(eval(s))
except SyntaxError:
    print("Invalid expression")