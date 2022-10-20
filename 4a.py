n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
result = l[0]
for i in range(n):
    m = l[i]
    for j in range(i+1,n):
        result = max(result, m)
        m = m*l[j]
    result = max(result, m)
print(result)