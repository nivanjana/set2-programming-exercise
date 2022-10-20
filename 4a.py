'''

There’s a game in Squid Games where all the participants are given a roll of coins. Each coin will have a value (positive, negative, or zero). The participants can select any number of adjacent coins from the roll. Those who get the highest product value get to the next level. If you are participating in the game, can you pick the set of adjacent coins so that the product is the highest value?
Examples:
Roll contains coins: 6, -3, -10, 0, 2
Highest product: 180  (The coins are 6, -3, and -10)
Roll contains coins: -1, -3, -10, 0, 60
Highest product: 60  (The coin is 60)
Roll contains coins: -2, -40, 0, -2, -3
Highest product: 80 (The coins are -2 and -40)

Test Cases:

a)
Input
 
5
-2
-3
-5
0
-4
 
Output
15

b)
Input
 
5
-1
-3
-10
60
0
 
Output
1800
            '''



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