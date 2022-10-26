from ast import operator

def operation(c1, c2, op):
    if op =='+':
        result = c2+c1
    elif op == '-':
        result = c2-c1
    elif op == '*':
        result = c2*c1
    elif op == '/':
        result = c2/c1
    else:
        result = c2**c1
    return result

s = input()
d = dict()
a = s
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z' or s[i]>='A' and s[i]<='Z':
        d[s[i]] = input("Enter value of {}: ".format(s[i]))
        a = a.replace(s[i],d[s[i]])

o = []
c = []
temp = []
i=0
try:
    while i<len(a):
        if a[i].isdigit():
            k = int(a[i])
            i+=1
            while i<len(a) and a[i].isdigit():
                k=k*10+int(a[i])
                i+=1
            c.append(k)
        else:
            if len(o)<=0:
                o.append(a[i])
            elif o[-1] in ('+','-') and a[i] in ['*','/','**','(']:
                o.append(a[i])
            elif a[i]==')':
                while o[-1]!='(':
                    op = o.pop()
                    c1 = c.pop()
                    c2 = c.pop()
                    c.append(operation(c1,c2,op))
                else:
                    o.pop()
            else:
                while (a[i] in ('+','-')) and (o[-1] in ['*','/','**','(']) and len(o)!=0:
                    temp.append(o.pop())
                else:
                    o.append(a[i])
                while len(temp)!=0:
                    o.append(temp.pop())
        i+=1
    if i>=len(a):
        while len(o)!=0 and len(a)>=2:
            op = o.pop()
            c1 = c.pop()
            c2 = c.pop()
            c.append(operation(c1,c2,op))
    if len(o)>0:
        if o[-1] in ('+','-'):
            print(str(o.pop())+str(c.pop()))
        else:
            print("Invalid Expression")
    else:
        print(c.pop())
except IndexError:
    print("Invalid Expression")
