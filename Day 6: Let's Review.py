# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    s = input()
    even = ""
    odd = ""
    for j in range(len(s)):
        if j % 2 == 0:
            even = even + s[j]
        else:
            odd = odd + s[j]
    print(even,odd)
